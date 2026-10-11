---
title: "49. 사람 근접 안전"
type: area
category: "M. 안전"
area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [속도·분리 감시, 보호 분리 거리, 구역별 속도 제한, 운용 구역, 실외이동로봇 운행안전인증, 사람 인지형 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-11
sources: [ref-1075, ref-1076, ref-470, ref-1077, ref-031, ref-980, ref-992, ref-1078, ref-1080, ref-1081, ref-1082, ref-1083, ref-1084, ref-1085, ref-869, ref-1464, ref-1466, ref-1467, ref-1468, ref-1469, ref-1470, ref-1471, ref-1472, ref-1473, ref-1474, ref-1475]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [M. 안전](index.md) › 49. 사람 근접 안전

# 49. 사람 근접 안전

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 왜 중요한가](../../topics/2026/2026-09-30-area49-s3.md)에 있다.

## 4. 핵심 개념과 용어

사람 근접 안전의 핵심 개념은 사람과 지켜야 할 분리 거리를 계산하는 방식과, 그 거리를 지키도록 플릿 관제가 내리는 구역·속도 제한을 표현하는 방식이다. [의견][^ref-1075][^ref-031]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area49-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 물류창고

**사례:** 로봇 구역에 들어간 직원 주변에서 로봇이 감속·우회·정지(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 로봇 구역에 들어가며 로보틱스 테크 조끼를 착용·활성화한다. [추정] 벤더 주장[^ref-1080] |
| 작업 대상 | 로봇 구역(공간)과 그 안에서 일하는 직원(사람). [추정] 벤더 주장[^ref-1080] |
| 수행 자원 | 조끼를 켠 직원과 그 신호에 반응하는 로봇. [추정] 벤더 주장[^ref-1080] |
| 제약 | 조끼를 켜면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다. [추정] 벤더 주장[^ref-1080] 감속 속도·거리 값은 미확인이다. |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(처리량 영향 자료 없음) |

이 사례는 아마존이 자사 풀필먼트 센터 운영을 설명한 글에 근거하며, 그 글의 발행일은 페이지 메타데이터 기준 2019-04-06 이다(벤더 문서, 독립 확인 없음, 확인일 2026-10-11). [추정] 벤더 주장[^ref-1080] 조끼 신호의 거리·지연·안전 등급은 여전히 확인하지 못했다. 이 영역은 제약 칸, 곧 사람 위치 신호를 받아 어느 로봇을 감속·정지시킬지 정하는 부분에 관여한다. [의견][^ref-1080]

창고를 대상으로 한 연구로는 Farrell 외(arXiv 2025-03-27)가 학습 기반 제어 장벽 함수(Control Barrier Function, CBF)를 [Open-RMF](../../glossary/open-rmf.md) 에 통합해 보행자를 포함한 정적·동적 장애물 회피를 평가한 것이 있다. [사실][^ref-1082] 출판판은 2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151, 쪽수 미확인)인 것으로 보인다(UC eScholarship 기록 기준). [추정][^ref-1082] 실험은 Freight·Jackal·Megarover 실물 로봇으로 했고, 로봇과 보행자 위치는 OptiTrack 모션 캡처로 측정했으며, 정적·동적 장애물 회피 단위 실험은 설정마다 10회 수행했다. [사실][^ref-1082] 플릿 실험 표(Table IV)는 열 이름(Four Robot Controls 1.0 m/s, Two Robot Controls 1.5 m/s) 기준으로 두 설정에서 보행자 0·1·2명 조건을 비교했고(논문 본문은 로봇 대수를 따로 명시하지 않는다), 표의 값은 Open-RMF 상위 계획기가 로봇을 일부러 세워 둔 시간을 뺀 것이다. [사실][^ref-1082] 따라서 표의 값은 단위 실험과 분모가 다르고 전체 임무 처리량으로 옮겨 읽을 수 없는 것으로 보인다. [추정][^ref-1082] 이는 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가다. [사실][^ref-1082]

**현장 유형:** 병원

**사례:** 병원 물류 로봇의 사람 보행 속도 수준 주행 평가(실제 병원 배치를 재현한 모의 병원 공간)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병상·복도·대기 공간·가구 등 실제 병원의 물리적 배치를 재현한 모의 병원 공간. [사실][^ref-1081] |
| 수행 자원 | 병원 물류용 HOSBOT 과 TIAGo 실물 로봇, 위치 측정용 Vicon 카메라 8대. [사실][^ref-1081] |
| 제약 | 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켰고, 속도 선정 근거로 사람 보행 하한 0.6~1.3 m/s 를 인용했다. [사실][^ref-1081] 이동 장애물은 사람이 아니라 정해진 경로를 고정 선속도·각속도로 원격조종해 움직인 두 번째 시험용 이동 로봇 베이스였다. [사실][^ref-1081] |
| 완료·인계 | 미확인 |
| 예외·성과 | 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 최고 속도에서 방향 오차가 커졌으며 정확도는 중간 속도에서 가장 높았다. [사실][^ref-1081] |

이 사례는 실제 병원 구조를 재현한 모의 병원 공간에서 실물 로봇으로 수행한 실험 평가이며, 실제 환자와 함께 운영한 결과가 아니다(Scientific Reports, 2024-08-07). [사실][^ref-1081] 이동 장애물이 원격조종 로봇이었으므로, 사람을 대상으로 안전거리를 검증한 시험과는 구별해 읽어야 할 것으로 보인다. [추정][^ref-1081] 시험 속도는 법정 사람 근접 속도가 아니지만, 로봇 속도를 사람 보행 속도에 맞춰 고른 점이 이 영역의 '언제 느려져야 하는가'와 이어진다. [의견][^ref-1081]

같은 병원 현장 유형에서, Tartu 대학병원 현장 시험 논문(Frontiers in Robotics and AI, 2022-08-23)은 TIAGo·Clearpath Jackal 이종 로봇을 RMF 로 관리하는 능력을 시험 환경에서 검증했고, 병원 안에서 여러 배송 로봇을 운용하는 것은 아직 하지 않은 향후 과제로 적었다. [사실][^ref-869]

**현장 유형:** 실외

**사례:** 배송 로봇의 보도·횡단보도 운행(실외이동로봇 운행안전인증 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배송 등 목적으로 자율주행·원격제어 로봇이 실외를 운행한다. [사실][^ref-980] 인증 신청 때는 횡단보도 통행방식과 통신장애·사고발생·혼잡상황 대응 시나리오를 담은 운행계획서를 낸다(시행규칙 2025-10-01 시행본 기준). [사실][^ref-1470] |
| 작업 대상 | 횡단보도를 포함한 실외 통행 공간. [사실][^ref-980] |
| 수행 자원 | 자율주행·원격제어 로봇과 관제장치의 조합(인증 단위). [사실][^ref-980] |
| 제약 | 최고 속도 15 km/h 이하·최대 질량 500 kg 이하이며, 시행규칙 제7조의4 는 이 두 기준(질량은 적재물 포함)을 정하고 세부사항을 고시에 맡긴다(2025-10-01 시행본, 확인일 2026-10-11). [사실][^ref-980][^ref-992][^ref-1470] 현행 고시(산업통상부고시 제2025-21호, 2025-11-24 시행) 별표 3 은 로봇과 적재물 질량 합계에 따라 최대 운행 속도를 230 kg 초과 500 kg 이하 5 km/h, 100 kg 초과 230 kg 이하 10 km/h, 100 kg 이하 15 km/h 로 나눈다(기준일 2026-10-11). [사실][^ref-1469] 현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)으로는 어린이·노인·장애인 보호구역에서 5 km/h 준수를 확인하고, 사람이나 장애물을 감지하면 안전하게 감속·정지·회피해야 하며 그 평가는 KS B 7320 의 장애물 감지와 회피 절을 따른다. [추정][^ref-1469] 같은 기준으로 보행 신호가 이미 켜진 때 도착한 로봇은 정지 상태로 기다렸다가 다음 신호에 횡단하고, 횡단 중 통신이 끊기면 횡단을 마친 뒤 안전한 곳에 정차한다. [추정][^ref-1469] 2023-07-28 기사는 당시 개정안 기준으로 질량 합계 230 kg 초과면 5 km/h, 100 kg 초과면 10 km/h, 그 이하면 15 km/h 이고 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단한다고 전했다. [사실][^ref-992] 이 값은 별표 3 원문 기준으로 알려진 현행 값과 같아 보이나, 2023 개정안과 현행 고시 사이의 중간 개정 이력은 확인하지 못했다. [추정][^ref-1469][^ref-992] |
| 완료·인계 | 미확인 |
| 예외·성과 | 주변 인식과 비상정지가 심사 항목이고, 인증 뒤 2년 주기 정기점검을 받는다. [사실][^ref-980] 현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)으로는 보행자 밀집 등으로 경로를 지날 수 없으면 로봇이 관제장치에 알리고 관리자가 조치할 수 있어야 한다. [추정][^ref-1469] |

이 사례는 특정 도입 현장이 아니라 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 따른 인증 요구를 여섯 항목으로 옮긴 것이다. [사실][^ref-980] 심사 항목 수는 인증기관 페이지(8개 항목)와 2023-07-28 기사(16가지)가 달라, 한쪽을 고르지 않고 11절 열린 질문으로 올렸다. [사실][^ref-980][^ref-992] 현행 고시 별표 3 의 상위 항목은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개로 인증기관 페이지의 8개 심사항목 이름과 같다. [사실][^ref-1469][^ref-980] 다만 인증기관은 같은 제도 안의 기관이라 독립 교차 확인이 아니며, 기사의 16가지가 어느 단위에 대응하는지는 이번에도 확인하지 못했다. 인증 대상에 관제장치가 포함된다는 점은 9절에서 ROP 범위와 겹칠 수 있는 경계로 다룬다.

제조 공장은 산업용 로봇 사업장 규정(7절)과 협동 작업셀 연구(6절)만 확인했고 현장 유형을 밝힌 적용 사례는 찾지 못했다. 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례도 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1077][^ref-031][^ref-1083][^ref-1085]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area49-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1084][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)에서 다룬다.

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area49-s7.md)에 있다.

## 8. 대표 연구와 자료

사람 근접 안전의 대표 연구는 분리 거리 계산(NIST), 창고·병원 주행 평가, 사람 인지형 배정, 보행자 편안함, 사회적 주행 데이터셋으로 나뉘며, 각 연구의 평가 조건(실물·모의 공간·시뮬레이션)을 함께 읽어야 한다. [의견][^ref-1075][^ref-1081][^ref-1083]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-10-11-area49-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하고, 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하며, 그 조정과 정지·재개 이력을 기록한다. [추정][^ref-031][^ref-1080][^ref-1082][^ref-1083] 구축자 의견으로는 어댑터 계약에서 '제한 없음'·'양수 속도 제한'·'통로 폐쇄'·'보호 정지'를 다른 명령으로 구분하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록하는 일도 여기에 든다. [의견][^ref-1464][^ref-1468][^ref-031] | 연계 대상: 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(로봇 제조사·시스템 통합자), Nav2 Collision Monitor 같은 로봇 측 로컬 회피 계층. [추정][^ref-1075][^ref-470][^ref-1077][^ref-1078] 연계 대상: 안전 레이저 스캐너의 감시 케이스 전환·다중 샘플링에 따른 응답시간 보정. [추정] 벤더 주장[^ref-1466] 연계 대상: 센서 데이터가 끊기면 로봇을 세우는 Collision Monitor 와 속도 제한을 적용하는 Speed Filter. [사실][^ref-1467][^ref-1468] 연계 대상: 사람 검출·추적 모듈([19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md) 쪽 기술). [사실][^ref-1474] |
| 시설·설비 제어 | 설비·로봇의 안전 설정값과 상태를 받아 계획에 반영하는 인터페이스. [추정][^ref-1078][^ref-1084] | 연계 대상: 울타리 같은 설비 안전 조치, 현장 배치의 위험성 평가(IMR 시스템 통합자). [추정][^ref-1078][^ref-1084] |
| 업종별 조건 | 실외 속도 상한·횡단보도 대기 같은 조건을 작업·경로 제약으로 반영한다. [추정][^ref-980][^ref-992] 구축자 의견으로는, 실외 로봇의 관제 역할을 맡을 때 운행계획서의 통신장애·혼잡 대응 시나리오와, 별표 3 원문 기준으로 알려진 보행자 밀집 알림·관리자 조치와 보호구역 5 km/h 를 구역별 속도 제한 정책과 알림 흐름으로 연결해 두어야 한다. [의견][^ref-1469][^ref-1470] | 연계 대상: 실외 인증 대상인 로봇·관제장치 조합의 적합성(운영 사업자). [추정][^ref-980] 연계 대상: 운행안전인증 신청과 운행계획서 제출. [사실][^ref-1470] ROP 사업자가 신청 주체인지는 확인한 조문에 없다. |

VDA 5050 명세는 스스로 안전 표준이 아니라고 밝히고 Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않는다고 밝히므로, ROP 가 내리는 구역·속도 제한과 사람 인지형 조정은 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다. [추정][^ref-031][^ref-1077] 사람 위치 신호에 따른 조정은 벤더 주장과 연구 평가에 기대고 있어 현장 효과는 아직 확인되지 않았다. [추정][^ref-1080][^ref-1082][^ref-1083] 6절에서 본 '0' 값의 의미 차이와 계획 반영까지만 하는 Open-RMF 속도 제한 처리를 보면, ROP 가 내린 제한이 실제 감속으로 이어졌는지는 계획 상태와 별도로 확인해야 할 것으로 보인다. [추정][^ref-1464][^ref-1467][^ref-1468]

사람 위치를 발행하는 공개 구현으로는 ROS 2 패키지 human_detection_fusion 이 있으며, 확인한 코드는 위치 발행까지만 다루고 플릿 감속·정지 명령이나 차량 감속 확인은 다루지 않는다. [추정][^ref-1474] 이 패키지는 YOLO 검출과 초광대역(Ultra-Wideband, UWB) 위치를 합쳐 사람 식별자별 위치를 `/humans/persons/{id}/position` 형태의 토픽(id 는 사람 식별자)에 ROS4HRI 의 hri_msgs 형식(PointOfInterest3DStamped)으로 발행한다(고정 커밋 2026-06-29 기준). [사실][^ref-1474] 같은 코드의 transformUWBPosition 함수는 UWB 좌표를 계획 좌표계로 바꾸다 변환 예외가 나면 경고를 남기고 입력 좌표를 그대로 돌려준다. [사실][^ref-1474] 호출부가 반환 좌표에 계획 좌표계 이름을 붙여 발행하므로, 변환이 실패하면 UWB 좌표계 값이 계획 좌표계 값으로 표시돼 나갈 수 있어 보인다(코드 경로 해석이며 실제 운용 오류나 상위 계층의 보정 여부는 확인하지 못했다). [추정][^ref-1474] 이 저장소의 KIRO 는 EU ARISE 1차 공개 모집의 실험 이름으로 한국로봇융합연구원과는 다르며, 저작권자는 그리스 연구기관 ATHENA RC, 라이선스는 AGPL-3.0 이다. [사실][^ref-1474] 구축자 의견으로는, 사람 검출·추적은 로봇 자체 지능·제어 경계의 연계 대상이고 ROP 몫은 그 위치를 받아 감속·정지로 잇는 인터페이스이며, 이 연계에서 측정 시각·좌표계·변환 성공 여부·만료 시각을 메시지에 명시하게 하고 위치 수신과 차량의 실제 감속 확인을 별도 단계로 시험해야 한다. [의견][^ref-1474][^ref-1080]

실외이동로봇 운행안전인증의 대상은 로봇과 관제장치의 조합이므로, ROP 가 실외 로봇의 관제 역할을 맡으면 인증 범위와 겹칠 수 있다. [추정][^ref-980] 인증 적합성을 운영 사업자의 몫으로 본 것도 확인된 규정이 아니라 추론이다. [추정][^ref-980]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1084][^ref-031][^ref-1083]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md)에 있다.

## 11. 열린 질문

이 영역의 열린 질문은 플릿 구역 제한의 안전 인정 조건, 실외 인증 심사 항목 수의 출처 충돌, 국내 실내 사람 근접 기준, 이종 플릿 공통 감속·정지 인터페이스이며, 2026-10-11 실행은 네 질문 모두 부분 근거만 더했고 해결하지 못했다. [의견][^ref-031][^ref-1469]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 열린 질문](../../topics/2026/2026-10-11-area49-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [49. 사람 근접 안전](human-proximity-safety.md) — seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계, 연결 16건, 열린 질문 4건), 각주 15건 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area49-s6.md) — 자동 분리: 49. 사람 근접 안전 의 "6. 대표 접근법과 기술" 절(1,762자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area49-s7.md) — 자동 분리: 49. 사람 근접 안전 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,599자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-09-30-area49-s8.md) — 자동 분리: 49. 사람 근접 안전 의 "8. 대표 연구와 자료" 절(1,128자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md) — 자동 분리: 49. 사람 근접 안전 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,041자)을 옮겼다 (실행 2026-09-30-10)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-10-11
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1077]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-11
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-10-11 (원문 미열람)
[^ref-1078]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 2019-04-06, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-10-11
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environment, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-10-11
[^ref-1082]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-10-11
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-11
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1085]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-10-11
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
[^ref-1466]: SICK (Martin Kidman), The perfect size of the protective field on an industrial autonomous vehicle, 2021-02-09, https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle, 접근일 2026-10-11
[^ref-1467]: Open Navigation (Nav2 documentation, Jazzy), Collision Monitor Node — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/, 접근일 2026-10-11
[^ref-1468]: Open Navigation (Nav2 documentation, Jazzy), Speed Filter Parameters — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/, 접근일 2026-10-11
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-11
[^ref-1470]: 법제처 국가법령정보센터, 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5, 2025-10-01, https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075, 접근일 2026-10-11
[^ref-1474]: ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험, human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18), 2026-06-29, https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp, 접근일 2026-10-11
