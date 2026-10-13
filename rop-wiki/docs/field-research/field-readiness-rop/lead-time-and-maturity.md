---
title: "리드타임·성숙도와 비용"
type: field-research
research: field-readiness-rop
level: study
hide: [toc]
search: {exclude: true}
related_areas: [1, 28, 39, 56, 62]
tags: [리드타임, 성공률, 무개입 성공, 개입률, 비용, 도입 일정, 성숙도]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-1572, ref-1573, ref-1574, ref-1575, ref-1576]
---

[홈](../../index.md) › [확장 아이디어](../../ideas/index.md) › [스터디](../index.md) › [현장 적용·운영 검증](index.md) › 리드타임·성숙도와 비용

# 리드타임·성숙도와 비용

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

"로봇이 일을 해냈다"를 숫자로 말하려면 언제부터 언제까지를 재는지, 사람이 도운 경우를 어떻게 세는지, 비용에 무엇을 넣는지를 먼저 정해야 한다. 이 페이지는 그 정의를 제안하고, 휴머노이드 도입 일정 같은 성숙도 주장을 공개 원문으로 어떻게 나눠 읽는지 정리한다.

## 1. 현장 문제

발표 관찰: 현장 적용의 성숙도를 "관제 → 협업 → 완전 조율"처럼 단계로 보는 관점이 제시됐다. 이 관점은 공인 성숙도 표준으로 확인되지 않았다. 발표자의 관점으로만 표시하고 외부 등급·인증·정량 점수로 바꾸지 않는다.

발표 관찰: 로봇 회사 인수, 전동 휴머노이드 공개, 양산·현장 투입 목표 연도가 언급됐다. 공개 원문과 대조해 보면 하나의 "양산일"로 합쳐 말하기 어려운 여러 사건이 섞여 있었다(2절).

## 2. 근거·적용 조건

**인수의 두 날짜.** [추정] 벤더 주장: 2020-12-11은 현대자동차그룹이 소프트뱅크그룹으로부터 보스턴 다이내믹스 지배지분(약 80%) 인수의 주요 조건에 합의했다고 거래 당사자가 공동 발표한 날이다. 이 발표에는 거래 종결이 2021년 6월 예상으로만 적혀 있다.[^ref-1572] [추정] 벤더 주장: 인수 완료 발표는 2021-06-21이다.[^ref-1573] "인수"를 말할 때 합의 발표와 완료 발표를 구별한다.

**전동 휴머노이드의 두 공개.** [추정] 벤더 주장: 완전 전동식 Atlas는 2024-04-17에 소개됐다.[^ref-1574] [추정] 벤더 주장: 제품 버전 Atlas는 2026-01-05에 공개됐고, 보스턴 본사에서 즉시 생산을 시작하며, 2026년 배치 물량은 모두 확정돼 현대 RMAC와 Google DeepMind로 출하할 예정이고, 추가 고객은 2027년 초로 계획한다.[^ref-1575]

**공정 투입 계획.** [추정] 벤더 주장: 현대자동차그룹의 CES 2026 발표는 공정별 검증을 거쳐 2028년부터 부품 서열 공정에 Atlas를 투입하고 2030년까지 부품 조립으로 넓히며, 2028년까지 연 3만 대 규모의 로봇 생산 체계를 갖춘다는 목표를 밝힌다.[^ref-1576]

이 다섯 가지는 서로 다른 사건이다. 생산 개시, 생산 능력 목표, 특정 공정 투입 계획을 하나의 "양산 연도"로 합치지 않는다. 모두 당사자 발표이며, 계획이 실현될지의 근거가 아니다. 발표에서 언급된 연도가 이 가운데 어느 것을 뜻했는지는 확인하지 못했다.

## 3. ROP 판단

[의견] 성과 지표는 아래처럼 정의한다. 분모와 기간은 측정을 시작하기 전에 고정한다.

| 지표 | 정의 | 해석할 때 주의 |
|---|---|---|
| 업무 리드타임 | 업무 시스템이 요청을 수락한 시각부터 품질 확인·인계를 거쳐 업무가 확정된 시각까지 | 대기·이동·실행·인계·검사·개입·재작업 상태를 겹치지 않게 나누고, 병렬 구간을 두 번 더하지 않는다 |
| 성공률 | 품질·기한·인계 조건을 모두 만족한 업무 수 ÷ 대상 업무 수 | 취소·중도 실패·미완료를 분모에서 어떻게 처리할지 미리 정한다 |
| 무개입 성공률 | 어떤 개입도 없이 완료한 업무 수 ÷ 대상 업무 수 | 원격 리셋과 원격 조작도 개입이다 |
| 개입률·부담 | 개입한 업무의 비율, 운영 시간당 개입 횟수, 사람이 쓴 시간 | 개입 횟수가 줄면서 대기 시간이 늘어난 것을 숨길 수 있다 |
| 복구 시간 | 고장 감지 → 제한된 업무 재개, 고장 감지 → 정상 복구를 따로 측정 | 평균만 보지 않고 꼬리 지연과 복구되지 않은 사례를 포함 |
| 점검 커버리지 | 정해진 주기 안에 품질 적합 측정을 얻은 대상 ÷ 필요한 대상 | 위치 방문률과 따로 본다 |
| 공용 자원 병목 | 승강기·문·작업대별 대기 분포, 점유, 고장, 사람 사용, 대기열 | 전체 평균 가동률만으로 개선 원인을 단정하지 않는다 |
| 비용 | 로봇·시설·통신·통합·검증·교육·운영·유지·개입·재작업·중단 비용 ÷ 품질 적합 완료량 | 시스템 전체 비용과 ROP의 기여를 따로 산정 |

[의견] 수작업이나 기존 운용과 비교하려면 같은 작업량·시간대·적재·품질 기준·자원 수를 맞춰야 한다. 발표의 성숙도 단계는 이 지표를 대신하지 않는다.

## 4. 제조사·설비·운영자 역할

[의견] 업무 소유자는 업무 확정 시각과 품질 기준을 정한다. 운영자는 개입 기록을 빠짐없이 남긴다. 재무·운영 담당은 비용 항목의 단가를 정한다. 제조사는 장비 가동 정보와 유지 비용 자료를 제공한다. ROP는 상태 전이 기록으로 리드타임 구간을 계산하고, 개입 유형을 구분해 지표를 낸다.

## 5. 대응·판단 기준

[의견] 비용은 아래 양식으로 채운다. 현장 견적과 운영 관측이 있어야 금액을 넣을 수 있고, 이번 조사는 금액을 확인하지 못했다.

- **초기 비용** = 조사 인건비 + 계측·교정 + 설비·치구·통신 공사 + 초기 통합·교육 + 검증·입회 + 계획된 운영 중단.
- **기간 비용** = 유지·청소·재교정 + 반복 개입 인건비 + 장애 대기·재작업·폐기 + 버전·현장 변경 회귀 시험 + 통신·플랫폼 운영비.
- **비교 단위** = 품질 적합 완료 작업당 비용과 서비스 마감 달성률.

[의견] 비용이 가장 적은 안이라도 안전·법규·품질 수용 조건을 통과하지 못하면 비교 후보에서 뺀다. 가동률·단가·고장 빈도는 낙관·기준·불리 조건으로 민감도를 보고, 근거 없이 "몇 개월이면 회수"를 제시하지 않는다.

## 6. 검증·한계

- 지표 정의와 비용 양식은 제안이다. 실제 운영 자료로 계산한 결과가 아니다.
- 인수·제품 공개·도입 계획은 모두 당사자 발표다. 재무 거래나 생산 실적을 독립 감사한 자료가 아니다.
- 발표에서 언급된 적용 현장 수와 성능 수치는 공개 근거가 없어 싣지 않았다. 공개 근거가 없다는 것이 적용 현장이 없다는 뜻은 아니다.

## 7. 연결 영역

- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md): 대기행렬·병목·프로세스 마이닝·업무 KPI. 이 페이지는 개입·인계·검사·재작업을 넣은 완료 시각과 비용 분모를 덧붙인다.
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md): 승강기 피크 대기·사람 점유·복구 분포.
- [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md): 확대 결정의 근거.
- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md)과 [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md): 휴머노이드의 공정 투입 계획.

## 8. 남은 질문

- 병목·개입·재작업까지 넣은 비용과 리드타임을 같은 작업 조건의 대조 운영으로 어떻게 비교하는가? (FR11)
- 발표에서 언급한 양산·투입 연도는 위 사건 가운데 무엇을 뜻했는가? 발표 원본 자료가 필요하다. (FR13)
- 발표의 성숙도 단계를 측정 가능한 기준으로 바꿀 수 있는가, 아니면 관점으로만 둘 것인가?

[^ref-1572]: SoftBank Group Corp. · Hyundai Motor Group, Hyundai Motor Group to Acquire Controlling Interest in Boston Dynamics from SoftBank Group, Opening a New Chapter in the Robotics and Mobility Industry, 2020-12-11, https://group.softbank/en/news/press/20201211_0, 접근일 2026-10-12
[^ref-1573]: Hyundai Motor Group (PR Newswire 배포), Hyundai Motor Group Completes Acquisition of Boston Dynamics from SoftBank, 2021-06-21, https://www.prnewswire.com/news-releases/hyundai-motor-group-completes-acquisition-of-boston-dynamics-from-softbank-301316206.html, 접근일 2026-10-12
[^ref-1574]: Boston Dynamics, An Electric New Era for Atlas, 2024-04-17, https://bostondynamics.com/blog/electric-new-era-for-atlas/, 접근일 2026-10-12
[^ref-1575]: Boston Dynamics, Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry, 2026-01-05, https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/, 접근일 2026-10-12
[^ref-1576]: Hyundai Motor Group, Hyundai Motor Group Announces AI Robotics Strategy to Lead Human-Centered Robotics Era at CES 2026, 2026-01-05, https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-announces-ai-robotics-strategy--to-lead-human-centered-robotics-era-at-ces-2026, 접근일 2026-10-12
