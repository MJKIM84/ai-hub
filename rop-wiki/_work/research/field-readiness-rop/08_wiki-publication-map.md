# 위키 반영 후보 지도 — 게시하지 않은 제안

조사 2026-10-13, 기준 main 9c4de24. **이 파일은 [의견]인 편집 제안**이며 docs/data/config/runs/pipeline/robot-simulator를 수정하거나 게시하지 않았다. 대상은 실제 본문 링크와 현재 번호를 대조했다. 분리 페이지의 옛 번호는 [01](01_existing-wiki-gap-matrix.md)을 따른다.

|이번 산출물|기존 대상 파일|대상 절|반영 후보|재사용·주의|
|---|---|---|---|---|
|03 B·05·07 FR01|[robot-ontology/heterogeneous-robot-registration.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/robot-ontology/heterogeneous-robot-registration.md)|§9·11|구성별 증거 ID·버전 변경 시 현장 승인 영향|4영역 등록 관문 재사용|
|03 B|[robot-ontology/robot-capability-and-task-representation.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/robot-ontology/robot-capability-and-task-representation.md)|§1·6·9·11|선언/실증/임시 제한 3종과 조건부 질의|oq-024와 연결; 환경 조건 아이디어를 신규로 주장하지 않음|
|03 B·07|[robot-ontology/ontology-based-system-and-robot-integration.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md)|§6·9·11|미측정·만료·불일치 구성의 확인 필요 반환|기존 능력→스킬→인터페이스 재사용|
|03 B·06 §4|[robot-ontology/ontology-verification-and-change-management.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/robot-ontology/ontology-verification-and-change-management.md)|§6·11|구성/환경 변경 영향·실측 검증과 형상검증 분리|온톨로지 논리 통과≠현장 성공|
|03 D|[integration/robot-and-vendor-fleet-manager-integration.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/integration/robot-and-vendor-fleet-manager-integration.md)|§6·9|기종/판/권한별 어댑터 계약·단절 상태 대조|Full/TrafficLight/ReadOnly 기존 조사 재사용|
|02·03 D|[integration/interoperability-standards-and-conformance.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/integration/interoperability-standards-and-conformance.md)|§6·7·11|6기술의 역할/보장 범위, PTT 미확인|인증·정지·업무 완료 보장으로 과장 금지|
|03 D/E·04 C10|[integration/facility-and-building-system-integration.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/integration/facility-and-building-system-integration.md)|§6·9·11|층/문/점유 신선도·세션·수동 복귀·인계 관문|최근 F-22와 2026-10-11 분리 페이지 우선|
|03 D/F|[platform-architecture-and-infrastructure/platform-architecture-and-external-api.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)|§6·9|업무/현장/로봇 판단 위치와 실행 권한|발표 L4~L1은 표준이 아닌 해석|
|03 D·05 무선|[platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)|§6·9·11|작업별 마감/단절/상태 나이·재연결 계약|단일 10ms·30초 등을 보편 요구로 전용 금지|
|03 E|[platform-architecture-and-infrastructure/data-observability-and-deployment.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)|§6·9·11|배포 소유권/상태 이관과 물리 고장 복구 분리|oq-210/213 재사용|
|03 E|[execution-collaboration-and-recovery/command-and-task-execution-reliability.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)|§6·9|명령/업무 ID·접수/완료·실물 대조|네트워크 exactly-once와 실물 수행 분리|
|03 E/F|[execution-collaboration-and-recovery/human-robot-collaboration.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md)|§9·11|원격 조작/리셋/물리 개입/수동 대체 기록|31영역; 발표 영상의 자율성 미확인|
|03 E·04|[execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)|§6·9·11|대체 투입→인계→품질→재개와 책임|기존 재계획 조사 재사용|
|06|[design-and-simulation/simulation-and-predictive-digital-twin.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md)|§6·9·11|사건 주입/원인 재현·광학/RF/접촉 충실도 구별|구현 지원은 코드 기준과 별도|
|06|[design-and-simulation/virtual-commissioning-and-real-situation-replay.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)|§6·9·11|5실패 유형별 모델·관측·보정·홀드아웃|실행/시험 통과 주장 없음|
|03 F·04 C08|[field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)|§6·9|방문/측정 품질·자산/원인·보전 후속 작업|센서 내부 성능 보장은 제조사/계측 담당|
|03 F·05 비용|[field-operations-and-monitoring/operational-performance-measurement-and-improvement.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)|§6·9·11|전체 리드타임·무개입 성공·재작업·비용 분모|숫자 성과는 현장 자료 뒤 별도|
|03 F|[planning-and-optimization/shared-resource-charging-and-energy-optimization.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)|§6·11|승강기 피크 대기·고장/사람 점유·복구 분포|기존 세션/뮤텍스 조사 재사용|
|04·05|[verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)|§6·9·11|조건별 측정 방법/담당/비용/수용 기준|기종별 한계/현행 법 적용 별도|
|03 E·05·07|[verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)|§6·9·11|제조사 재현 패키지·승인 범위·교육/롤백|운영 이관 완료 기준 보강|
|03 A/F·05 업종|[site-type-applications/manufacturing-plant.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/site-type-applications/manufacturing-plant.md)|§6·9|서열·오염·공정 침범·치구·품질|비공개 현장/수치 제외|
|03 A/F·05 업종|[site-type-applications/hospital-and-healthcare.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/site-type-applications/hospital-and-healthcare.md)|§6·9|감염/인수·유효 측정·승강기 공유|제조 성과 숫자 전용 금지|
|03 A/F·05 업종|[site-type-applications/commercial-facilities.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/site-type-applications/commercial-facilities.md)|§6·9|손님 혼재·서비스 피크·인력 대체|호텔/서비스 조건으로 한정|
|03 A/F·05 업종|[site-type-applications/home-and-apartment.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/site-type-applications/home-and-apartment.md)|§6·9|출입·프라이버시·관리 주체·재배송 비용|운영자/주민 조건 반영|
|03 A·07|[site-type-applications/outdoor.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/categories/site-type-applications/outdoor.md)|§9·11|실내외 경계의 광 변화·날씨·예외 인계|실내 승인으로 실외 성능 주장 금지|

## 트랙·열린 질문·출처의 후보 연결

- [manual-capability-ontology/ontology-draft.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/tracks/manual-capability-ontology/ontology-draft.md) §6: 구성 버전·환경 조건 질문에 03 B의 증거 분리/질의를 **제안**으로 연결한다. 기존 확정 개념을 자동 교체하지 않는다.
- [evaluation-and-verification.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/tracks/manual-capability-ontology/evaluation-and-verification.md) §3~6: 문서 정확도·조건 커버리지·현장 시험의 차이를 덧붙일 후보. 측정 결과가 없으므로 측정 완료 칸을 채우지 않는다.
- [question-backlog.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/tracks/manual-capability-ontology/question-backlog.md): q4-04/q5-05/q6-02에 질문을 좁혀 연결하는 후보. ID 새 발급/상태 변경은 하지 않았다.
- [open-questions.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/open-questions.md): oq-024/032/033/208/210/213 등과 FR 백로그를 대응한다. 정량·현장 증거 미확보 질문을 ‘답함’으로 바꾸지 않는다.
- [docs/references/](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/references/): sources.md의 실제 열람본과 실패 사유를 참고문헌 후보로 제공한다. 기존 ref-041 미열람 카드를 논문 사실의 근거로 승격하지 않는다.

## 공개 근거·발표·미확인의 편집 경계

|종류|반영 가능한 형태|제외/보류|
|---|---|---|
|직접 열람한 공개 표준·공식 문서|판·절·접근일·원문 구절과 적용 한계|성능 미시험·조건 밖 일반화|
|벤더 단독 문서|[추정] 벤더 주장: + 문서가 말하는 지원/계획|독립 실증·안전성 인증으로 승격|
|현행 법령|정확한 조문·시행일·적용 범위/예외|특정 건물 설계 승인/법률 판단으로 확대|
|발표 관찰|[발표 내 확인] 일반화한 실패 유형·조사 질문|원문·실명·현장명·비공개 수치|
|전사 미확인|확인해야 할 질문과 필요한 원전|PTT의 임의 복원·양산 연도 추측|
|코드 정적 관찰|기준 SHA·파일·함수·분기와 읽은 범위|실행 성공·실기체 성능·광학/RF 검증 주장|
|본 조사 제안|[의견]인 수용 기준·측정/비용 양식|공식 표준/인증 항목이라고 표시|

## 게시 전 검토 제안

[의견] 후속 위키 편집을 별도로 승인할 때 ① 기존 문장/절과 중복 여부 ② 원문 접근과 판 ③ 벤더 태그 ④ 발표 공개 범위 ⑤ 실증/정적 코드 구별 ⑥ 미확인 질문의 상태 ⑦ 링크/번호를 확인한다. 이번 draft PR은 **연구 폴더 산출물만** 검토하는 용도이며 위키 게시를 요청하지 않는다.
