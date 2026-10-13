---
title: "제조사 피드백 패키지"
type: field-research
research: field-readiness-rop
level: study
hide: [toc]
search: {exclude: true}
related_areas: [4, 7, 20, 38, 55, 56]
tags: [제조사 피드백, 재현 패키지, 회귀 시험, 롤백, 인수 관문, 개인정보 제거]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-1577, ref-1590]
---

[홈](../../index.md) › [확장 아이디어](../../ideas/index.md) › [스터디](../index.md) › [현장 적용·운영 검증](index.md) › 제조사 피드백 패키지

# 제조사 피드백 패키지

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

현장에서 실패가 나면 결국 제조사가 고쳐야 할 때가 많다. 그런데 "이 구간에서 자꾸 멈춰요"만으로는 제조사가 재현할 수 없고, 고친 뒤에도 무엇으로 다시 승인할지 정해져 있지 않으면 같은 일이 반복된다. 이 페이지는 현장 실패를 제조사에 넘길 때 묶어 보낼 자료와, 수정 뒤 다시 승인하는 관문을 정리한다.

## 1. 현장 문제

발표 관찰: 현장 문제를 제조사와 함께 풀면서 설정 조정·인식 옵션 변경을 거쳤다는 설명이 있었다. 어떤 자료를 주고받았는지, 수정 뒤 어떤 시험으로 확인했는지는 발표로 알 수 없었다.

발표 관찰: 발표에서 쓴 특정 설정 값(예: 좁은 경로를 엄격히 따르는 폭)은 비공개로 취급했다. 이 위키에도 싣지 않는다.

## 2. 근거·적용 조건

[추정] 벤더 주장: 한 제조사 SDK만 봐도 지면 마찰 힌트, 계단 모드, 계단 오류 시 자동 하강 해제, 경로 엄격 추종, 계단 하강 방향 선호, 회피 통로 폭처럼 현장 동작을 바꾸는 설정이 여럿 있고, 일부는 기본값·권장 범위가 주석에만 있거나 단위가 적혀 있지 않다.[^ref-1577][^ref-1590] 이 자료는 master 판 기준이며, 현장 펌웨어·SDK 판에서 같은 필드·기본값인지는 확인하지 못했다.

그래서 피드백 패키지에는 "무엇을 바꿨나"뿐 아니라 "어느 판에서, 어떤 단위·기본값으로"가 들어가야 한다. 같은 이름의 설정도 판이 바뀌면 의미나 기본값이 달라질 수 있다.

## 3. ROP 판단

[의견] 실패마다 아래 필드를 묶은 재현 패키지를 만든다. 값이 없는 필드는 추측하지 않고 "알 수 없음"으로 둔다.

| 필드 | 내용 |
|---|---|
| 상황 식별 | 사례 id, 기체·구역의 비식별 코드, 시간대·운영 단계, 업무 id |
| 구성 | 기체·센서·도구·펌웨어·SDK·설정·지도·어댑터·설비 인터페이스의 판 |
| 환경 | 바닥 상태·재질·기하·조명·무선·주변 움직임·적재와 하중 중심 |
| 기대·관측 | 정상 기대, 최초 실패 신호, 실제 물리 상태, 관제 상태, 사람 관찰 |
| 근거 | 시각 오차를 포함한 원시·처리 로그, 필요한 영상, 측정 방법과 보정 |
| 재현성 | 시도 수·실패 수, 실패하지 않은 조건, 다른 구성과의 대조, 관찰 기간 |
| 조치 | 설정·경로·시설·사람 대체의 변경 내용, 승인자, 변경 전후 검증 |
| 남은 위험 | 원인 확정 여부, 임시 제한, 적용 구역·기간, 재시험을 부르는 조건 |

[의견] 제조사에 보내는 패키지에는 여기에 기대 결과와 실제 결과, 발생률과 재현 실패 기록, 변경 전후 결과, 회귀 시험 목록, 되돌릴 수 있는 구성과 승인자를 더한다.

## 4. 제조사·설비·운영자 역할

[의견] 현장 통합자가 패키지를 만들고, 제조사가 재현·원인 분석·수정 판을 낸다. 수정 판을 현장에 넣을지는 현장 통합·안전 담당이 승인한다. 시설·네트워크 담당은 환경 쪽 원인을 같이 확인한다. ROP는 패키지가 가리키는 구성·증거 id를 [환경 조건을 반영한 로봇 능력](context-aware-capabilities.md)의 기록과 잇고, 수정 판이 들어오면 영향받는 승인을 "검토 필요"로 바꾼다.

[의견] 공개하거나 넓게 공유하는 사본에서는 로그의 얼굴·위치·계정·영업 수치를 지우고, 원본은 권한 있는 별도 보관소에 둔다. 이번 조사에서는 외부로 원본을 전달하지 않았다.

## 5. 대응·판단 기준

[의견] 수정 판이나 설정 변경을 다시 승인하려면 다음 증거가 있어야 한다.

1. 작업·기종·설정·구역·적재·시간대의 범위와 제외 조건.
2. 제조사 한계·법규·현장 품질 기준의 출처와 판.
3. 정상·경계·실패·복구·반증 시험의 입력과 기대값, 중단 조건.
4. 측정 불확실성, 표본과 관찰 기간, 실패를 포함한 결과, 시험하지 않은 영역.
5. 사람 대체·인계·품질·재개의 책임과 호출 경로.
6. 운영 비용, 유지 담당, 변경 감지, 재시험, 롤백 계획.

[의견] 감지를 둔하게 해서 실패가 줄어든 수정은 반증 시험(실제 장애물·사람 대조군)을 통과하기 전까지 승인하지 않는다. 판이 바뀐 뒤에는 이전에 통과한 시나리오를 회귀 시험으로 다시 돌린다.

## 6. 검증·한계

- 패키지 필드와 승인 관문은 제안이다. 실제 제조사와 주고받은 사례로 검증하지 않았다.
- 제조사마다 원시 데이터·로그 접근 권한이 다르다. 계약 단계에서 무엇을 받을 수 있는지 정해야 하며, 이번 조사는 계약 조건을 확인하지 않았다.
- 이 문서는 인수시험을 계획하기 위한 조사 결과이며, 시험 통과나 운영 승인 기록이 아니다.

## 7. 연결 영역

- [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md): 제조사 재현 패키지와 승인 범위·교육·롤백.
- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md): 구성 판과 재검증.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md): 제조사 관제가 노출하는 상태·오류.
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): 원인 분석용 기록.
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md).

## 8. 남은 질문

- 경로 엄격 추종·계단·마찰 설정이 현장에서 쓰는 판에서 정확히 어떤 단위·방향·기본값·부작용을 갖고, 시험 결과는 어떤가? (FR15)
- 서로 다른 제조사의 로그와 플랫폼 기록을 하나의 작업 id로 이어 원인 분석에 쓰는 방법은? (관련 oq-210)
- 제조사·시설·네트워크·업무 소유자가 수용 기준과 증거 보관 주체를 어떤 순서로 합의하는가?

[^ref-1577]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/spot/robot_command.proto (master, blob 183f8fa), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/spot/robot_command.proto, 접근일 2026-10-12
[^ref-1590]: Boston Dynamics (spot-sdk GitHub), spot-sdk — protos/bosdyn/api/graph_nav/map.proto (master, blob f37e496), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/graph_nav/map.proto, 접근일 2026-10-12
