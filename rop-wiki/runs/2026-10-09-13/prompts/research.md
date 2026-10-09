(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-13
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 33. 시나리오 모델·편집 (I. 설계·시뮬레이션)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1509
- 새 출처 id 구간: ref-1509 ~ ref-1538 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1509 부터 순서대로 쓰고 ref-1538 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-10-09-13/target.json

```json
{
  "run_id": "2026-10-09-13",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 146,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 33,
    "area_name": "33. 시나리오 모델·편집",
    "category": "I. 설계·시뮬레이션",
    "category_letter": "I"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=update, area=33"
}
```

### docs/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [시나리오 형식, OpenSCENARIO, Open-RMF, 장애 주입, 시나리오 라이브러리, 미션 기술 형식]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1086, ref-104, ref-079, ref-971, ref-528, ref-1087, ref-1088, ref-726, ref-1089, ref-815, ref-1090, ref-116, ref-1091, ref-1092, ref-046]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 왜 중요한가](../../topics/2026/2026-09-30-area33-s3.md)에 있다.

## 4. 핵심 개념과 용어

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [추정][^ref-1088][^ref-1086][^ref-528]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 다섯 사례는 모두 실제 현장 배치가 아니라 공개된 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오를 여섯 항목으로 정리한 것이며, 이 영역에서는 각 시나리오가 무엇을 어떤 단위로 담았는지를 본다. [사실][^ref-104][^ref-971][^ref-1087]

**현장 유형:** 상업 시설

**사례:** Open-RMF 예제 호텔·공항 터미널 월드의 다중 플릿 순찰·청소 시나리오(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 월드를 띄운 뒤 dispatch_clean·dispatch_patrol 같은 작업 명령을 따로 넣으면 작업이 생긴다. [사실][^ref-104] |
| 작업 대상 | 호텔 월드의 로비와 객실 2개 층 공간을 순찰(loop)·청소한다(예제 명령은 로비 청소). [사실][^ref-104] |
| 수행 자원 | 호텔 월드에는 로봇 플릿 3개(로봇 4대), 승강기 2대, 여러 문이 있고, 디스패처가 [플릿 어댑터](../../glossary/fleet-adapter.md)들 사이의 작업 입찰을 조율한다. [사실][^ref-104] |
| 제약 | 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에 선택적으로 군중 시뮬레이션과 사람이 모는 읽기 전용(read_only) 카트를 더해 순찰·배송·청소를 실행한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

rmf_demos의 시나리오는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 작업을 명령으로 따로 넣는 구조다(2026-09-30 확인). [사실][^ref-104] 호텔·공항 터미널 모두 시뮬레이션 예제 월드이며 실제 시설의 도입 사례가 아니다.

**현장 유형:** 병원

**사례:** Open-RMF 예제 클리닉 월드에서 두 층의 간호 스테이션 사이 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 순찰 명령(dispatch_patrol)으로 작업을 넣는다. 예제 명령은 1층과 2층의 간호 스테이션을 순찰 지점으로 지정한다. [사실][^ref-104] |
| 작업 대상 | 두 층에 걸친 간호 스테이션 사이의 순찰 경로(공간) [사실][^ref-104] |
| 수행 자원 | 역할이 다른 로봇 플릿 2개와 승강기 2대 [사실][^ref-104] |
| 제약 | 로봇이 승강기 2대가 있는 2개 층 시설에서 층을 오가며 순찰해야 한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

클리닉 월드는 병원형 시나리오 예제이며 실제 병원 배치 사례가 아니다. 이 월드는 승강기 2대가 있는 2개 층 시설이고, 로봇이 층을 오가며 순찰한다. [사실][^ref-104] 층간 이동이 승강기를 거친다는 점에서 이 예제는 설비를 시나리오 요소로 담는 예로 볼 수 있다. [추정][^ref-104]

**현장 유형:** 실외

**사례:** Open-RMF 예제 캠퍼스 월드의 배송 로봇 장거리 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 명령으로 장거리 순찰을 넣는다. [사실][^ref-104] |
| 작업 대상 | 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스 공간 [사실][^ref-104] |
| 수행 자원 | 여러 대의 배송 로봇 [사실][^ref-104] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

캠퍼스 월드는 실내 층 좌표 대신 지구 좌표로 공간을 주석한 실외 시나리오 예제다. [사실][^ref-104] 같은 예제 모음의 제조·물류 월드는 영상 데모뿐이라 사례로 세우지 않고 7절에서만 다룬다.

**현장 유형:** 가정

**사례:** BEHAVIOR-1K의 일상 가정 활동 라이브러리(벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고, 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상(강체·변형체·액체)을 OmniGibson 시뮬레이터에 구현했다. [사실][^ref-971] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 활동이 일상 가정 활동이라서 현장 유형을 '가정'으로 분류했으며, 장면에는 주택뿐 아니라 정원·식당·사무실도 들어 있다. [사실][^ref-971] 실제 가정 배치가 아니라 시뮬레이션 벤치마크다.

**현장 유형:** 제조 공장

**사례:** NIST ARIAC 전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립과 장애 주입(경진대회 시나리오)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 키팅과 모듈 조립 두 작업을 주문으로 받는다. [사실][^ref-1087] |
| 작업 대상 | 배터리 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 조립하는 모듈 [사실][^ref-1087] |
| 수행 자원 | 시나리오에 컨베이어·전압 시험기·진공 그리퍼가 들어 있고, 각각을 고장 대상으로 선언할 수 있다. [사실][^ref-528] |
| 제약 | 해당 없음 |
| 완료·인계 | 아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않는다. [사실][^ref-1087] |
| 예외·성과 | 컨베이어 고장(시작 시각·지속 시간), 전압 시험기 고장(시작·지속·대상 시험기), 진공 그리퍼 파지 실패(도구·몇 번째 파지인지), 긴급 주문(시작 시각·주문 id) 네 과제를 매개변수로 선언해 시각이나 발생 횟수 조건으로 주입한다. [사실][^ref-528] |

ARIAC는 경진대회용 시뮬레이션 시나리오이며 실제 공장 사례가 아니다. ARIAC는 장애와 긴급 요청을 매개변수로 선언해 시나리오에 주입한다. [사실][^ref-528] 예외를 시나리오 안의 선언으로 다루는 이 방식은 이 영역이 참고할 점으로 보인다. [추정][^ref-528]

물류창고 현장의 시나리오 예제·템플릿 사례는 이번 조사에서 찾지 못했다. 경로 찾기 벤치마크의 시나리오 파일과 VDMA 레이아웃 교환 형식은 현장 사례가 아니므로 7절에서 다룬다. 국내 자료도 찾지 못했다.

## 6. 대표 접근법과 기술

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md)에 있다.

## 8. 대표 연구와 자료

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-09-30-area33-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP는 시나리오 모델·현장 유형별 예제 라이브러리·편집기·형식 변환을 맡고, 물리·센서 시뮬레이션 엔진과 로봇 모델, 설비 제어, 도로 교통 시나리오 표준은 참조·변환해 묶는 연계 대상으로 두는 것으로 보인다. [추정][^ref-104][^ref-528][^ref-1092][^ref-1088]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 시나리오에 어떤 로봇을 어디에 둘지(로봇 구성)를 정하고 로봇 모델을 참조로 묶는다. [추정][^ref-104][^ref-1092] | 물리·센서 시뮬레이션 엔진과 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 시뮬레이터·로봇 제조사 쪽 연계 대상이다. [추정][^ref-1092] |
| 시설·설비 제어 | 승강기·문·컨베이어 같은 설비를 시나리오 요소로 선언하고 설비 장애를 시각·발생 조건으로 주입한다. [추정][^ref-104][^ref-528] | 컨베이어·작업셀 같은 설비 제어 자체는 설비 쪽 연계 대상이다. [추정][^ref-104][^ref-528] |
| 업종별 조건 | 도로 교통 시나리오 표준의 구조(정적·동적 분리, 매개변수화)를 참조 설계로 삼는다. [추정][^ref-1088] | 도로 교통 시나리오 표준(OpenSCENARIO·OpenDRIVE)은 자율주행 분야의 연계 대상이다. [추정][^ref-1088] |

ROP가 직접 맡을 범위는 네 가지로 보인다: 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 시나리오 모델, 현장 유형별 예제 라이브러리, 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택, 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환이다. [추정][^ref-104][^ref-528][^ref-079][^ref-1090][^ref-116][^ref-1092]

시나리오 모델에 판(버전)을 두는 것은 1절 리스트업이 정한 목표다. 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 공개 자료에서 찾지 못했으므로, 판 관리 규칙은 아직 근거 없이 설계해야 하는 부분이다. [추정][^ref-1088][^ref-046][^ref-104][^ref-079]

경계는 제품 전략에 따라 이동할 수 있다. 이종 제조사를 연결하는 ROP는 시뮬레이터·제조사·설비 쪽 기능을 직접 만들기보다 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. [추정][^ref-1092][^ref-104][^ref-528][^ref-1088] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-09-30-area33-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [33. 시나리오 모델·편집](scenario-model-and-editing.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건. 2차 수정: 4절 요약 태그 [추정]으로 정정, 5절 병원·제조 공장 사례 서술의 사실·추정 분리 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md) — 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,795자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md) — 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,571자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md) — 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(1,360자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md) — 자동 분리: 33. 시나리오 모델·편집 의 "4. 핵심 개념과 용어" 절(1,249자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장 태그를 [사실]에서 [추정]으로 정정 (실행 2026-09-30-12)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
```

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md (요약)

```markdown
# 34. 시뮬레이션·예측용 디지털 트윈

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시뮬레이션 엔진**: 로봇·설비·물품·사람을 물리·센서 수준에서 가상으로 재현한다(MuJoCo·Gazebo·Isaac Sim 등)
- **운영 정책·수요 변화 예측**: 배치·운영 정책·일의 양이 바뀔 때의 효과를 가상 환경에서 미리 본다
- **시뮬레이션 관측 모델**: 잡음·지연이 있는 관측을 만들어 시뮬레이션 시험이 현실의 불확실성을 반영하게 한다
- **시뮬레이션 자산 관리**: 로봇·물품·환경의 3D 모델과 물성 값을 출처·라이선스와 함께 관리해 시뮬레이션에 쓴다

이전 분류(2026-09-24)에서 이 페이지는 옛 22번 영역 ‘시뮬레이션·예측용 디지털 트윈’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [옛 분류원문]

> 옛 질문: 성수기 주문량이 늘면 어디가 먼저 막힐까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md (요약)

```markdown
# 35. 처리능력·규모·배치 설계

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]
```

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md (요약)

```markdown
# 36. 가상 시운전·실제 상황 재현

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실행 전 계획 검증**: 선언한 초기 조건에서 경로·자원·능력을 실제로 실행하지 않고 정적으로 검사한다
- **가상 시운전**: 실제 설치 전에 연동과 운영 정책을 가상 환경에서 시험한다
- **운영 기록 기반 재현**: 실제 운영 기록으로 시뮬레이션의 초기 상태와 사건을 다시 구성한다
- **시뮬레이션–현실 차이 관리**: 시뮬레이션 결과를 현실에 적용할 때 생기는 차이를 측정하고 보정한다
- **디지털 트윈 동기화**: 실시간 상태를 가상 모델에 계속 반영해 현재 상태 표현과 미래 실험을 잇는다

## 2. 핵심 질문

설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md (요약)

```markdown
# 14. 도면·BIM에서 지도 만들기

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md (요약)

```markdown
# 32. 예외 복구·재계획·업무 연속성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

고장·통신 단절·누락에 대한 복구와 제한 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **예외 복구**: 고장·통신 단절·물품 누락·긴급 요청에 재배정·우회·수동 처리·제한 운영을 결정한다
- **제한 운영·업무 연속성**: 일부 장비가 멈춰도 업무를 이어 가는 운영 수준과 절차를 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 20번 영역 ‘예외 복구·재계획·업무 연속성’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [옛 분류원문]

> 옛 질문: 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [옛 분류원문]

## 2. 핵심 질문

작업 중 로봇이 고장 나면 남은 일은 누가 어떻게 이어받는가? [분류원문]
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (요약)

```markdown
# 44. 로봇 기반 모델·언어 모델 계획

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/commercial-facilities.md (요약)

```markdown
# 64. 상업 시설

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/home-and-apartment.md (요약)

```markdown
# 65. 가정·공동주택

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
```

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1250건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 2026-09-25 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | https://github.com/open-rmf/rmf_demos | 2026-09-25 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | https://arxiv.org/abs/2603.15427 | 2026-09-25 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 2026-09-25 | 예 |
| ref-726 | Kästner, L. 외 | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | https://arxiv.org/abs/2206.05728 | 2026-09-25 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12-14 | https://arxiv.org/abs/2312.09067 | 2026-09-29 | 예 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | https://arxiv.org/abs/2403.09227 | 2026-09-29 | 예 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | https://arxiv.org/abs/2307.03325 | 2026-09-30 | 예 |
| ref-1087 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 2026-09-30 | 예 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | https://www.asam.net/standards/detail/openscenario-xml/ | 2026-09-30 | 예 |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | https://arxiv.org/abs/2409.12471 | 2026-09-30 | 예 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | https://www.behaviortree.dev/groot/ | 2026-09-30 | 예 |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | https://movingai.com/benchmarks/mapf/index.html | 2026-09-30 | 예 |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | http://sdformat.org/ | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 355개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
- failure-explanation: 실패 설명 (Failure Explanation)
- falsification: 반증 기반 시험 (Falsification)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- finops: 핀옵스 (FinOps)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- guidance-graph: 안내 그래프 (Guidance Graph)
- hallucination: 환각 (Hallucination)
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indirect-prompt-injection: 간접 프롬프트 주입 (Indirect Prompt Injection)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
- integrity-risk: 무결성 위험 (Integrity Risk)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- security-level-iec-62443: 보안 수준 (Security Level (SL, IEC 62443))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shift-handover: 교대 인수인계 (Shift Handover)
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
- software-in-the-loop: 소프트웨어 인 더 루프 (Software-in-the-Loop (SiL))
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- stakeholder-requirements-specification: 이해관계자 요구사항 명세 (Stakeholder Requirements Specification (StRS))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [33] 에 걸린 7건 / 전체 303건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-135 [열림] 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? (영역 9, 33)
- oq-233 [열림] 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? (영역 33, 34)
- oq-234 [열림] 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? (영역 33, 57)
- oq-235 [열림] ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? (영역 33, 32)
- oq-236 [열림] 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? (영역 33, 65)
- oq-256 [열림] 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? (영역 36, 19, 33)
```

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### runs/2026-10-09-10/research.md

```markdown
# 리서치 브리프 2026-10-09-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-10 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | N. 보안·개인정보 |

## 갭(비어 있거나 약한 섹션)

- N. 보안·개인정보 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 다른 16개 대분류의 연결이 정리되지 않았다
- 51. 인증·권한·격리 페이지는 이전 분류(2026-09-25) 기준이라 C. 채팅 기반 구성·운영, D. 공간·지도 모델, J. 현장 운영·관제의 40. 운영 절차·요청 창구, P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터와 잇는 근거가 페이지 안에 없다
- 51·52·53 페이지의 10절(다른 연구영역과의 연결)은 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- D. 공간·지도 모델 페이지는 N. 보안·개인정보와의 연결을 '근거 없음'으로 남겼다(지도 데이터의 접근 통제·개인정보)
- Q. 현장 유형별 적용 가운데 물류창고·상업 시설·기타 현장의 보안·개인정보 사례가 51·52·53 게시 페이지에 없다
- EU 사이버복원력법 보고 의무(2026-09-11 시행)와 EU 데이터법처럼 최근 시행된 규정이 게시 페이지에 반영되지 않았다

## 조사 질문

1. 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]
2. 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
3. 51. 인증·권한·격리의 명령 권한·장비 인증은 B. 로봇 온톨로지(4·6·7)·F. 연동(20·22)·G. 계획·최적화(25)·H. 실행·협업·예외 복구(29)·K. 플랫폼 아키텍처·인프라(41)의 어느 인터페이스와 이어지는가? (oq-056, oq-082, oq-100, oq-113 관련)
4. 52. 통신 보호·위협 관리·감사의 위협·감사 기록은 C. 채팅 기반 구성·운영(12·13)·E. 사물·사람·실시간 상태(18)·J. 현장 운영·관제(37·38·40)·L. AI·학습 기술(44·47)·M. 안전(48·50)·O. 검증·도입·수명주기(54·55·57)와 어디서 만나는가? (oq-144, oq-246, oq-248, oq-291 관련)
5. 53. 개인정보·영상 데이터의 수집·보관 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(17·19)·L. AI·학습 기술(45·47)·P. 거버넌스·법규·사회(58·59·60)와 어떻게 이어지는가? (oq-259, oq-285, oq-214 관련)
6. 보안 인증·규제(IEC 62443, ISO 10218 개정, EU 사이버복원력법, EU 데이터법, 국내 로봇 보안모델)는 A. 기획·사업(1·2·3)에 어떤 요구를 넘기는가?
7. N. 보안·개인정보의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며 한국 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 과학기술정보통신부와 한국인터넷진흥원(KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다. | ref-1373, ref-1111 | 아니오 | medium | 2026-03-05 | — | — |
| f2 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: KUKA 는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했으며, 발표문에는 인증 기관이 나오지 않는다. | ref-1375 | 아니오 | low | 2026-09-02 | — | 벤더 주장 |
| f3 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: IEC 62443 이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로, 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다. | ref-1105, ref-1375 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 52. 통신 보호·위협 관리·감사 페이지는 ROP 가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다. | ref-1114, ref-1107, ref-009 | 아니오 | low | 2026-09-30 | — | — |
| f5 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: VDA 5050 3.0.0 은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호해야 하며 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록·7. 온톨로지 검증·변경 관리, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이며, 교체 승인과 실패 때 되돌림 책임은 열린 질문(oq-113)으로 남는다. | ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다. | ref-1145, ref-588 | 아니오 | low | 2026-09-30 | — | 원문 미열람 |
| f8 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다. | ref-579, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f9 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: OWASP LLM01:2025 는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다. | ref-1106 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f10 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대규모 언어 모델을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다. | ref-1113, ref-1112 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f11 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR 의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard 는 최악의 탈옥 공격에서 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고했다. | ref-857, ref-700 | 아니오 | medium | 2025-03 | 제약 | 원문 미열람 |
| f12 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Open-RMF REST API 를 언어 모델 도구로 노출하는 MCP 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다. | ref-854, ref-857 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f13 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다. | ref-1110 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f14 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다. | ref-1372, ref-1141 | 아니오 | medium | 2026-09-14 | 가정 / 작업 대상 | — |
| f15 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050 이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP 가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다. | ref-1372, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Shen 외(2026-09, 프리프린트)는 ROS 2 에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2 를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다. | ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f17 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고 위치 스푸핑이 배정을 무너뜨린다는 연구가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다(oq-082). | ref-1374, ref-494 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f18 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 병원 운반 로봇 Zena RX 는 생체 인식과 직원 PIN 으로 잠금 칸을 연다고 제조사가 밝히고 공동주택 배달 로봇 도입 계획은 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다. | ref-1299, ref-1301 | 아니오 | low | 2026-10-09 | 병원 / 완료·인계 | 원문 미열람, 벤더 주장 |
| f19 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: ROS 규약 제안 REP-155(Draft)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다. | ref-1173 | 아니오 | medium | 2022-01-11 | — | 원문 미열람 |
| f20 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다. | ref-1368, ref-1369 | 아니오 | medium | 2025-08-29 | 상업 시설 / 예외·성과 | — |
| f21 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 미국 CISA 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG 를 제어하는 Home Base Server 에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(CVE-2022-1070, CVSS 9.8)과 인가 누락 취약점을 공개했다. | ref-1107 | 아니오 | medium | 2022-04-12 | 병원 / 예외·성과 | 원문 미열람 |
| f22 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API 의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP 가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다(oq-100). | ref-1368, ref-1107 | 아니오 | low | 2026-10-09 | 제약 | — |
| f23 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f24 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API 의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다(oq-246). | ref-031, ref-1105 | 아니오 | low | 2026-10-09 | — | — |
| f25 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 22. 설비·건물 시스템 연동: 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다(oq-056). | ref-1369, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f26 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다. | ref-494 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f27 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF: 제조사 관리 API 를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP 의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다. | ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f28 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치 중이라는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다. | ref-031 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f29 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다고 보도되었으므로, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다. | ref-1368, ref-1369 | 아니오 | low | 2026-10-09 | 상업 시설 / 예외·성과 | — |
| f30 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1304 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f31 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제(f17)와 구분된다. | ref-1304, ref-588 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f32 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다. | ref-1110 | 아니오 | medium | 2024-03 | — | 원문 미열람 |
| f33 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230 은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다. | ref-1109 | 아니오 | medium | 2026-08-27 | — | 원문 미열람 |
| f34 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 보안 신고 창구가 없어 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다. | ref-1368, ref-1369 | 아니오 | medium | 2025-09-05 | 상업 시설 / 예외·성과 | — |
| f35 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EU 사이버복원력법에 따라 2026-09-11 부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 ENISA 단일 보고 플랫폼으로 알려야 하며, 인지 후 24시간 안에 조기 경보, 72시간 안에 통지, 취약점은 시정 조치가 나온 뒤 14일 안에 최종 보고를 낸다. | ref-1367 | 아니오 | medium | 2026-09-11 | 예외·성과 | — |
| f36 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보이며, 플랫폼 사업자의 보고 의무 해당 여부는 열린 질문(oq-291)이다. | ref-1367, ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f37 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: Open-RMF 문서는 웹 대시보드를 TLS 로 제공하고 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다. | ref-405 | 아니오 | medium | 2026-10-09 | — | — |
| f38 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다. | ref-009, ref-010 | 아니오 | medium | 2026-10-09 | — | — |
| f39 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다. | ref-1372 | 아니오 | medium | 2026-09-14 | 가정 / 제약 | — |
| f40 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ L. AI·학습 기술의 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영: 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다. | ref-1138, ref-1342 | 아니오 | medium | 2026-05-06 | 실외 / 제약 | 원문 미열람 |
| f41 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. | ref-863 | 아니오 | medium | 2024-06-13 | — | 원문 미열람 |
| f42 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | 원문 미열람 |
| f43 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f44 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ M. 안전의 48. 안전·위험 관리: Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보인다. | ref-1114 | 아니오 | low | 2017 | 제조 공장 / 예외·성과 | 원문 미열람 |
| f45 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ M. 안전의 48. 안전·위험 관리: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f46 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다. | ref-010, ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f47 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다. | ref-010 | 아니오 | low | 2026-10-09 | 제약 | — |
| f48 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다. | ref-969 | 아니오 | low | 2025-10-31 | 가정 | 원문 미열람 |
| f49 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: EU 데이터법은 2025-09-12 부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자(보통 제조사)는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다. | ref-1376 | 아니오 | medium | 2026-10-09 | — | — |
| f50 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다(oq-259). | ref-1376, ref-588 | 아니오 | low | 2026-10-09 | — | — |
| f51 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다. | ref-1136, ref-588 | 아니오 | medium | 2024-10-14 | 실외 / 제약 | 원문 미열람 |
| f52 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·Q. 현장 유형별 적용의 61. 물류창고: 프랑스 개인정보 감독기관 CNIL 은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique 에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다. | ref-1370, ref-1371 | 예 | medium | 2024-01-23 | 물류창고 / 제약 | — |
| f53 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·J. 현장 운영·관제의 39. 운영 성과 측정·개선: 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP 가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다(oq-285). | ref-1370, ref-589 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | — |
| f54 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다. | ref-589 | 아니오 | medium | 2026-10-09 | 제약 | 원문 미열람 |
| f55 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ Q. 현장 유형별 적용의 67. 기타 현장: Pudu 관리 API 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 평가이며 확인된 사고는 아니다. | ref-1369, ref-1368 | 아니오 | low | 2025-09-05 | 기타 / 예외·성과 | — |
| f56 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ Q. 현장 유형별 적용의 63. 병원·의료: 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다. | ref-1146 | 아니오 | medium | 2026-03-16 | 병원 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_dds_security.html | 아니오 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_threat_model.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 2019-08 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_access_control_policies.html | 아니오 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.25690 | 예 |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | 업계 보고서 | medium | 2026-10-09 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 예 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 예 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 2024-11-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG | Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 예 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 2024-06-13 | 정부·연구기관 | medium | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 예 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | 기사 | low | 2026-10-09 | https://byline.network/2025/10/31-283/ | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 미확인 | 표준 | medium | 2026-10-09 | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ | 예 |
| ref-1106 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 예 |
| ref-1107 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 2022-04-12 | 정부·연구기관 | medium | 2026-10-09 | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 | 예 |
| ref-1109 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 2026-08-27 | 업계 보고서 | medium | 2026-10-09 | https://www.ies.co.uk/reference-library/machinery-regulation-guide | 예 |
| ref-1110 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 2024-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2403.09567 | 예 |
| ref-1111 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시 | 2026-03-06 | 기사 | low | 2026-10-09 | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 | 예 |
| ref-1112 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.00747 | 예 |
| ref-1113 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 2024-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2408.03515 | 예 |
| ref-1114 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 2017 | 논문 | medium | 2026-10-09 | https://files01.core.ac.uk/download/pdf/84891817.pdf | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 예 |
| ref-1136 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 2024-10-14 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=125844 | 예 |
| ref-1138 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용 | 2023-11-15 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 | 예 |
| ref-1141 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-10-09 | https://view.asiae.co.kr/article/2026091410054053414 | 예 |
| ref-1145 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 2026-09-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.03055 | 예 |
| ref-1146 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 2026-03-16 | 논문 | medium | 2026-10-09 | https://doi.org/10.1145/3776734.3794481 | 예 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 예 |
| ref-1299 | ST Engineering Aethon (Newswire 게재 보도자료) | ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals | 2024-04-29 | 벤더 문서 | low | 2026-10-09 | https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264 | 예 |
| ref-1301 | 경향신문 (곽희양) | 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 | 2020-07-03 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202007031130001 | 예 |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1342 | 메트로신문 | AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원 | 2026-05-06 | 기사 | low | 2026-10-09 | https://www.metroseoul.co.kr/article/20260506500296 | 예 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 예 |
| ref-1367 | European Commission (Shaping Europe's digital future) | CRA reporting | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 아니오 |
| ref-1368 | The Register | Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots | 2025-08-29 | 기사 | medium | 2026-10-09 | https://www.theregister.com/2025/08/29/pudu_robots_hackable/ | 아니오 |
| ref-1369 | Hackmag | Researcher finds a way to hack Chinese Pudu service robots | 2025-09-05 | 기사 | low | 2026-10-09 | https://hackmag.com/news/pudu-bugs | 아니오 |
| ref-1370 | Silicon UK | France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance | 2024-01-23 | 기사 | medium | 2026-10-09 | https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858 | 아니오 |
| ref-1371 | CNIL (Commission nationale de l'informatique et des libertés) | Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million | 2024-01-23 | 정부·연구기관 | medium | 2026-10-09 | https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million | 예 |
| ref-1372 | 바이라인네트워크 (곽중희) | 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어" | 2026-09-14 | 기사 | medium | 2026-10-09 | https://byline.network/2026/09/14-623/ | 아니오 |
| ref-1373 | 바이라인네트워크 | 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개 | 2026-03-06 | 기사 | medium | 2026-10-09 | https://byline.network/2026/03/6-340/ | 아니오 |
| ref-1374 | Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv) | Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics | 2026-09-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.08280 | 아니오 |
| ref-1375 | KUKA (Robotics Tomorrow 게재 보도자료) | KUKA is First to Achieve Security Level 2 Certification for Robotics Industry | 2026-09-02 | 벤더 문서 | low | 2026-10-09 | https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/ | 아니오 |
| ref-1376 | European Commission (Shaping Europe's digital future) | Data Act explained | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/data-act-explained | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1(1, 한국 보안모델), f2(3, 벤더 주장)·f3(3), f4(2) / B. 로봇 온톨로지: f5·f6(4·7, 인증서 교체, oq-113), f7(4, 개인정보 속성), f8(6, 명령 단위 권한) / C. 채팅 기반 구성·운영: f9(13), f10(12), f11(13·44), f12(12, 최소 권한), f13(12, 승인 감사 기록) — 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f14(16, 가정 지도 저장 위치)·f15(15·16) — D 페이지가 '근거 없음'으로 둔 N 연결을 채움 / E. 사물·사람·실시간 상태: f16·f17(18, 텔레메트리 위조, oq-082), f18(17, 벤더 주장), f19(19) / F. 연동: f20·f21·f22(20, oq-100), f23·f24(21, oq-246), f25(22, oq-056) / G. 계획·최적화: f26·f27(25·27) / H. 실행·협업·예외 복구: f28(29), f29(32) / I. 설계·시뮬레이션: f30(34), f31(34·36) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성(f16·f17)과 구분 / J. 현장 운영·관제: f32·f33(37, oq-248·oq-249), f17(38), f34·f35·f36(40, oq-291) / K. 플랫폼 아키텍처·인프라: f37(41), f38(42), f39(43, oq-214) / L. AI·학습 기술: f40(45·47, 원본 영상), f41(47), f11(44) / M. 안전: f42·f43(50, oq-102·oq-254), f44·f45(48) / O. 검증·도입·수명주기: f48(54), f47(55), f46·f6·f35(57) / P. 거버넌스·법규·사회: f49·f50(58, oq-259), f35·f51(59), f52·f53·f54(60, oq-285·oq-099) / Q. 현장 유형별 적용: f52(61 물류창고, 로봇이 아닌 스캐너 사례임을 밝힘), f44(62 제조 공장), f21·f56(63 병원·의료), f20·f29·f34(64 상업 시설), f14·f39·f48(65 가정·공동주택), f40·f51(66 실외), f55(67 기타 현장). 벤더 주장 f2·f18 은 [추정]과 '벤더 주장' 병기. 로봇 제어기·펌웨어 보안, 승강기 제어, 카메라 기기 쪽 처리는 '연계 대상'으로 짧게. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육, 5. 로봇 능력·작업 표현, 8~11. 채팅 영역. 다음 실행 후보: 51. 인증·권한·격리(이전 분류 기준) 10절에 f5·f20·f22·f37 반영, 52. 통신 보호·위협 관리·감사 7절에 f35(사이버복원력법 보고 의무) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 적극 악용 취약점 | Actively Exploited Vulnerability (EU Cyber Resilience Act) | 악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다. |
| 연결 제품 | Connected Product (EU Data Act) | 사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다. |
| 원격 증명 | Remote Attestation | 원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다. |

## 열린 질문

새로 생긴 질문:

- ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? | 관련 영역: 51. 인증·권한·격리, 20. 로봇·제조사 관제 연동, 54. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반
- 로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 18. 실시간 세계 상태·데이터 일관성, 38. 모니터링·이상 탐지·원인 분석 | 근거: f17 | 종류: 일반
- EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 53. 개인정보·영상 데이터 | 근거: f50 | 종류: 일반
- 작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 60. 노동·수용성·접근성, 39. 운영 성과 측정·개선 | 근거: f53 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 45 · 교차 확인: 2
- 예산 사용량: 검색 13회 · 신규 출처 10건
- 미확인 항목:
    - f20·f29·f34·f55 Pudu 사례는 연구자 블로그 공개를 옮긴 기사 두 건 기준이며 연구자 원문과 제조사 공식 공지는 열지 못함(교차 확인 아님)
    - ref-1371 CNIL 공지는 페이지가 '더 이상 제공되지 않음'으로 열려 검색 결과 요약 범위로만 사용
    - f39 접근권한 내역·접속기록 보관 기간 연장의 적용 대상과 근거 조항은 기사에 없어 미확인(oq-214)
    - f2 KUKA IEC 62443-4-2 SL2 인증은 벤더 주장, 인증 기관·인증서 미확인
    - MiR Fleet Enterprise 의 IEC 62443-4-2 정렬 주장은 PDF 본문을 추출하지 못해 쓰지 않음
    - ISO 10218-1:2025 사이버보안 조항 번호는 여전히 미확인(oq-102)
    - KISA 로봇 보안모델 고도화판·해설서의 요구 항목은 원문을 열지 못해 미확인(oq-250)
    - EU 사이버복원력법 규정 원문(제14조)은 열지 않고 집행위원회 안내 페이지만 확인
    - 재사용 출처 35건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f2·f3·f44: 로봇 제어기 보안 인증·제어기 취약점은 원문 19장 '로봇 자체 지능·제어' 경계의 제조사 몫이라 ROP 는 조달 요구·연결 대상 위협 근거로만 서술
    - f21·f25: 병원 플릿 서버의 방화벽·VPN, 승강기 조작은 시설·설비 제어 경계의 연계 대상이며 ROP 는 연결 계정 권한과 설비 명령 권한 분리로만 서술
    - f14·f18·f56: 로봇청소기 앱 인증·기기 저장, 잠금 칸 생체 인증, 기기 쪽 얼굴 가림은 제조사 기능이라 연계 대상이며 ROP 는 결과·상태 기록 쪽만 서술
    - f35·f49·f51·f52·f54: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며 ROP 는 기록·통보·데이터 흐름 규칙 제공 범위로만 연결
    - f52: CNIL 사례는 로봇이 아닌 작업자 스캐너 기록이라 claim 에 그 사실을 밝힘
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 51·52·53 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-08, 2026-10-09-09)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 35건 가운데 이번에 다시 연 것은 ref-031(github_raw) 1건이고 나머지 34건은 fetched false·source_unopened true). 신규 출처는 10건(ref-1367~ref-1376, 예약 구간 안)이며 ref-1371(CNIL 공지)을 뺀 9건은 원문을 열었다. 검색 13회/30, 신규 출처 10건/15. 교차 확인 2건(f42 ISO 10218 사이버보안, f52 CNIL Amazon 과징금). 벤더 주장 2건(f2·f18). 같은 정부 발표를 옮긴 기사 쌍(f1, f51)과 같은 연구자 공개를 옮긴 기사 쌍(f20 등)은 독립 출처로 보지 않아 교차 확인으로 세지 않았다. 한국 자료: 신규 ref-1372·ref-1373, 재사용 ref-589·ref-588·ref-969·ref-1111·ref-1136·ref-1138·ref-1141·ref-1301·ref-1342. 현장 유형: 물류창고(f52·f53, 로봇이 아닌 스캐너 사례)·제조 공장(f44)·병원(f18·f21·f56)·상업 시설(f20·f29·f34)·가정(f14·f39·f48)·실외(f40·f51)·기타(f55) 각 1건 이상. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f16·f17)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f30·f31)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역과 함께 제안했다. 열린 질문 oq-056·oq-082·oq-099·oq-100·oq-102·oq-113·oq-214·oq-246·oq-248·oq-249·oq-250·oq-259·oq-285·oq-291 에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 이전 대분류 연결 실행과 같이 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 아직 근거를 찾지 못한 연결은 page_proposals 의 rationale 에 적었다. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-10-09-09/research.md

```markdown
# 리서치 브리프 2026-10-09-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-09 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- M. 안전 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 48. 안전·위험 관리, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사와 다른 16개 대분류의 연결이 정리되지 않았다
- 48. 안전·위험 관리 페이지는 이전 분류(2026-09-26) 기준이라 C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, O. 검증·도입·수명주기의 56. 운영 이관·확대·교육, P. 거버넌스·법규·사회와 잇는 근거가 페이지 안에 없다
- 48·49·50 페이지의 10절(다른 연구영역과의 연결)은 49·50 이 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- 정지·재개 판단에 쓰는 VDA 5050 안전 상태·운용 모드의 원문 확인과, 관제 통신이 끊겼을 때의 정지 경로(oq-095) 근거가 약하다
- ANSI/A3 R15.08-3(사용자 의무)과 국내 로봇작업 특별교육처럼 운영·교육 쪽 근거(oq-265, oq-275)가 게시 페이지에 없다
- Q. 현장 유형별 적용의 64. 상업 시설에 사람 근접 안전 적용 사례가 없다

## 조사 질문

1. 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]
2. 48. 안전·위험 관리의 정지·재개 판단은 B. 로봇 온톨로지(6)·F. 연동(20·21·22)·H. 실행·협업·예외 복구(29·31·32)·K. 플랫폼 아키텍처·인프라(42)의 어떤 상태·명령·통신 경로에 기대는가? (oq-095, oq-229 관련)
3. 49. 사람 근접 안전의 구역·속도·사람 흐름 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(18·19)·G. 계획·최적화(25·27·28)·I. 설계·시뮬레이션(34·36)과 어떻게 이어지는가?
4. 50. 안전 표준·인증·사고 조사의 표준 개정·인증·사고 기록은 A. 기획·사업(1·2·3)·J. 현장 운영·관제(37·38·40)·N. 보안·개인정보(51·52·53)·O. 검증·도입·수명주기(54·55·56·57)·P. 거버넌스·법규·사회(58·59·60)와 어디서 만나는가? (oq-102, oq-252, oq-254, oq-265, oq-275 관련)
5. 언어 모델이 지시하는 로봇 계획의 안전 검사는 C. 채팅 기반 구성·운영(12·13)과 L. AI·학습 기술(44·47)의 '사람이 확인·승인한 계획만 실행' 원칙과 어떻게 맞물리는가? (oq-106, oq-144 관련)
6. M. 안전의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며, 한국 법령·인증·사고 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다. | ref-1419, ref-1084 | 아니오 | medium | 2026-09-17 | — | — |
| f2 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: R15.08 시리즈가 통합자와 사용자의 의무를 따로 두므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 역할에 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(oq-096). | ref-1419, ref-1084, ref-472 | 아니오 | low | 2026-10-09 | — | — |
| f3 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있다. ISO 10218-1/-2 개정판은 2025-02에 나왔고 EN ISO 판의 참조가 2026-09-07 EU 관보에 실렸다. ANSI/A3 R15.08-3 은 A3 판매 페이지 기준 2026-04-23에 발행됐고, ISO 13482 개정판은 2026-09-15 기준 FDIS 단계다. | ref-1116, ref-1420, ref-1117 | 아니오 | medium | 2026-09 | — | — |
| f4 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 한다. 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다. | ref-1424 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f5 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다. | ref-1424, ref-980 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f6 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동·H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 운용 모드 가운데 AUTOMATIC 은 관제가 로봇을 완전히 제어하는 상태, SEMIAUTOMATIC 은 관제가 제어하되 주행 속도를 HMI 가 조정하는 상태다. INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f7 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 6. 온톨로지 기반 시스템·로봇 연동의 '실행 시점 조건 판단'에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | 제약 | — |
| f8 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다. | ref-1419, ref-1116, ref-980 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f10 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 LLM 이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고 제어 합성으로 계획과의 충돌을 푼다. 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다. | ref-1338 | 아니오 | medium | 2026-03-03 | 제약 | 원문 미열람 |
| f11 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했다. GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다. | ref-1337 | 아니오 | medium | 2024-10-17 | 제약 | 원문 미열람 |
| f12 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·13. 대화형 기능의 신뢰·기반: 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더하면, 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보인다. 로봇 자체 안전 기능은 연계 대상으로 남는다. | ref-417, ref-1338 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f13 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: VDA 5050 3.0.0 의 BLOCKED 구역에는 로봇이 들어가서는 안 되며, 구역 안에 있는 로봇은 멈추고 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고한다. SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f15 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 지도에 붙은 진입 금지·속도 제한 구역은 VDA 5050 이 정한 교통 관리 규칙이며 안전 기능이 아니다. 따라서 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229). | ref-031, ref-470 | 아니오 | low | 2026-10-09 | 제약 | — |
| f16 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고, 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | 제약 | 원문 미열람 |
| f17 | [사실] | 연계 대상: M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Abdul Hafez 외(IJRR, 2025-05)는 무결성 위험 지표로 EKF 기반 SLAM 위치추정의 안전성을 정량화했다. 데이터 연관 오류가 위치를 크게 해칠 수 있고, 랜드마크 밀도가 지나치게 높으면 안전성이 오히려 떨어진다고 보고했다. | ref-161 | 아니오 | medium | 2025-05 | — | 원문 미열람 |
| f18 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있다. 이 가운데 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다. | ref-286 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f19 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이다. ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다. | ref-286 | 아니오 | low | 2026-10-09 | 제약 | — |
| f20 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고, 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다. | ref-1181 | 아니오 | low | 2024-07-12 | 병원 / 제약 | 원문 미열람 |
| f21 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보인다. 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다. | ref-1181, ref-1180 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f22 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f23 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동·N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐다. 사이버보안, 데이터 보호, 승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | — |
| f24 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 로봇의 승강기 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다. 개정 초안 내용이 최종판에 남았는지는 확인하지 못했다(oq-254). | ref-945, ref-1425, ref-1117 | 아니오 | low | 2026-10-09 | 제약 | — |
| f25 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만, 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다. | ref-567 | 아니오 | medium | 2025-04-04 | 시작 조건 | 원문 미열람 |
| f26 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 AMR·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이다. 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다. | ref-159 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f27 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 과 ISO 21423 같은 상호운용 표준이 안전 요구를 범위에서 빼므로, 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다. | ref-031, ref-159 | 아니오 | low | 2026-10-09 | — | — |
| f28 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다. | ref-1083 | 아니오 | medium | 2025-08-27 | 수행 자원 | 원문 미열람 |
| f29 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 데모에서는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-104 | 아니오 | medium | 2026-10-09 | 예외·성과 | 원문 미열람 |
| f30 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f31 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Reliability Engineering & System Safety 게재 연구(2023)는 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 확률 페트리넷(SPN)으로 모델링·분석했다. | ref-565 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f32 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f33 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업: ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095). | ref-031 | 아니오 | low | 2026-10-09 | 완료·인계 | — |
| f34 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f35 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. | ref-1125 | 아니오 | low | 2026-09-29 | 제조 공장 / 제약 | 원문 미열람 |
| f36 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 2023-11 농산물유통센터에서 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다. | ref-1124 | 아니오 | low | 2023-11-08 | 물류창고 / 예외·성과 | 원문 미열람 |
| f37 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 확인한 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다. | ref-1124, ref-1125, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f38 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. | ref-1303 | 아니오 | medium | 2020-11-20 | 예외·성과 | 원문 미열람 |
| f39 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다. | ref-406 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | — |
| f40 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했다. 최고 속도에서는 방향 오차가 커졌다. | ref-1081 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | 원문 미열람 |
| f41 | [추정] | 연계 대상: M. 안전의 50. 안전 표준·인증·사고 조사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Wind River 인터뷰(2014)는 IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용하고, 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했다. 그러나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다. | ref-1312 | 아니오 | low | 2014-11-20 | — | 원문 미열람 |
| f42 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다. | ref-1120 | 아니오 | medium | 2022-05-13 | 예외·성과 | 원문 미열람 |
| f43 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 OSHA 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다. | ref-1122 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f44 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보인다. 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252). | ref-1120, ref-1122, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f45 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Ferrando 외(2020)의 ROSMonitoring 은 ROS 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다. | ref-1426 | 아니오 | medium | 2020-12-03 | — | — |
| f46 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보인다. 다만 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다. | ref-1426, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f47 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 그 결과 위험 감소 조치의 유지, 변경 관리, 직원 교육과 안전 작업 절차를 요구한다. | ref-1419, ref-1421 | 예 | medium | 2026-10-04 | — | — |
| f48 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보인다. 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265). | ref-1419, ref-1421 | 아니오 | low | 2026-10-09 | — | — |
| f49 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 모든 로봇에 무선 안전 비상정지를 보낸다. 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다. | ref-1422 | 아니오 | low | 2023-05-18 | 물류창고 / 예외·성과 | 벤더 주장 |
| f50 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 은 안전 표준이 아니고, 연결이 끊긴 로봇은 받은 주문을 이어 수행한다. 따라서 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고, ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095). | ref-031, ref-1422 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f51 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다. | ref-621 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f52 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법무법인 태평양 해설에 따르면 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고, 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다. | ref-1341 | 아니오 | medium | 2025-09-30 | 예외·성과 | 원문 미열람 |
| f53 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영: AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보인다. 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). | ref-621, ref-417 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f54 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | — |
| f55 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 에 따라 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다. | ref-1116 | 아니오 | medium | 2026-09-18 | — | — |
| f56 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1304 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f57 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제와 사람 위치·영상 데이터 처리도 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | — |
| f58 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보았다. 이에 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다. | ref-563 | 아니오 | medium | 2025-02 | 기타 / 제약 | 원문 미열람 |
| f59 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했다. KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다. | ref-1423 | 아니오 | medium | 2023-11-21 | 제약 | — |
| f60 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 해석에 따르면 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보인다. 고용노동부의 적용 지침은 확인하지 못했다(oq-275). | ref-1423 | 아니오 | low | 2026-10-09 | — | — |
| f61 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다. | ref-1419 | 아니오 | medium | 2026-09-17 | — | — |
| f62 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 두 영역을 잇는 것으로 보인다(oq-093, oq-282). | ref-1419, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f63 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다. | ref-1079 | 아니오 | medium | 2023-06-29 | — | 원문 미열람 |
| f64 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: ANSI/A3 R15.08-2(2023-10)는 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다. | ref-472, ref-1084 | 아니오 | medium | 2023-10 | — | 원문 미열람 |
| f65 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다. | ref-980, ref-1118 | 아니오 | medium | 2023-11-17 | 실외 / 제약 | 원문 미열람 |
| f66 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정한다. 같은 조는 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다. | ref-562 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f67 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. | ref-1214 | 아니오 | medium | 2024-04-07 | 실외 / 작업 대상 | 원문 미열람 |
| f68 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 61. 물류창고: 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다고 설명한다. | ref-1080 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | 원문 미열람, 벤더 주장 |
| f69 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ Q. 현장 유형별 적용의 65. 가정·공동주택: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를, 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다. | ref-1121 | 아니오 | medium | 2021-06-29 | 가정 / 예외·성과 | 원문 미열람 |
| f70 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 66. 실외: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/86749.html | 예 |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 2025-05 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649241287797 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/83545.html | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-10-09 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2502.20693 | 예 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 예 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-621 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-10-09 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2306.16740 | 예 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | low | 2026-10-09 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 예 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 예 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.19731 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-10-09 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 아니오 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | 표준 | medium | 2026-10-09 | https://iss.rs/en/project/show/iso:proj:83498 | 예 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | medium | 2026-10-09 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 예 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 예 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-10-09 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 예 |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202311081103001 | 예 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | 기사 | low | 2026-10-09 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-10-09 | https://iliad-project.eu/concluding-iliad/ | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2404.05050 | 예 |
| ref-1303 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 2020-11-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2011.10294 | 예 |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1312 | Wind River (Engblom, J. 인터뷰, Buchwieser, A.) | Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser | 2014-11-20 | 벤더 문서 | low | 2026-10-09 | https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser | 예 |
| ref-1337 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv) | Jailbreaking LLM-Controlled Robots | 2024-10-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-1338 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv) | Safety Guardrails for LLM-Enabled Robots | 2025-03-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-1341 | 법무법인 태평양(BKL) AI팀 | AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 | 2025-09-30 | 업계 보고서 | medium | 2026-10-09 | https://www.bkl.co.kr/law/insight/newsletter/6248 | 예 |
| ref-1419 | ANSI (American National Standards Institute) Blog | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 2026-09-17 | 표준 | medium | 2026-10-09 | https://blog.ansi.org/?p=190868 | 아니오 |
| ref-1420 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-09 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 아니오 |
| ref-1421 | Robotics 24/7 | A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available | 2026-10-04 | 기사 | medium | 2026-10-09 | https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available | 아니오 |
| ref-1422 | FORT Robotics (A3 Case Studies 게재) | Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs | 2023-05-18 | 벤더 문서 | low | 2026-10-09 | https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs | 아니오 |
| ref-1423 | 법제처 (네플라 위키 게재본) | [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련) | 2023-11-21 | 정부·연구기관 | medium | 2026-10-09 | https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k | 아니오 |
| ref-1424 | 메트로신문 (한용수) | 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막 | 2023-11-16 | 기사 | medium | 2026-10-09 | https://www.metroseoul.co.kr/article/20231116500208 | 아니오 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 아니오 |
| ref-1426 | Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS) | ROSMonitoring: A Runtime Verification Framework for ROS | 2020-12-03 | 논문 | medium | 2026-10-09 | https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/ | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1·f2(2, oq-096), f3(1), f4·f5(3, 실외 보험) / B. 로봇 온톨로지: f6·f7(6, 실행 시점 조건에 운용 모드·안전 상태), f8(4) / C. 채팅 기반 구성·운영: f9(12), f10·f11·f12(13), 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f13·f14·f15(16, oq-229), f16(15, oq-170), f17(15, 연계 대상) / E. 사물·사람·실시간 상태: f18·f19(18), f20·f21(19) / F. 연동: f22·f23·f24(22, oq-254), f25(20), f26·f27(21) / G. 계획·최적화: f28(25), f29(28), f30·f31(27) / H. 실행·협업·예외 복구: f32·f33(29·31, oq-095), f34(32), f35·f36·f37(32·40) / I. 설계·시뮬레이션: f38(34·36), f39·f40(34), f41(36, 연계 대상) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현(f18·f19)과 구분 / J. 현장 운영·관제: f42·f44(37, oq-252), f43·f45·f46(38), f47·f48(40, oq-265) / K. 플랫폼 아키텍처·인프라: f49(벤더 주장)·f50(42, oq-095) / L. AI·학습 기술: f51·f52·f53(47, oq-106) / N. 보안·개인정보: f54·f57(51·52, oq-102), f56(52), f23·f57(53) / O. 검증·도입·수명주기: f45·f63(54), f58(55), f52·f59·f60(56, oq-275), f61·f62(57, oq-093·oq-282) / P. 거버넌스·법규·사회: f2·f64(58), f4·f55·f65·f66(59), f67(60) / Q. 현장 유형별 적용: f36·f49·f68(61 물류창고), f35(62 제조 공장), f20·f40(63 병원·의료), f39(64 상업 시설, 시뮬레이션 예제), f69(65 가정·공동주택), f4·f67·f70(66 실외), f58(67 기타 현장). 벤더 주장 f49·f68 은 [추정]과 '벤더 주장'을 병기하고, 연계 대상 f17·f41 과 로봇 자체 안전 기능·승강기 모드 제어·SLAM 은 '연계 대상'으로 짧게 쓴다. 상호운용 규격(VDA 5050·ISO 21423)은 안전 표준이 아니라는 점(f13·f26)을 유지한다. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설의 실제 현장 사례. 다음 실행 후보: 48. 안전·위험 관리(이전 분류 기준) 10절에 f32·f33·f47·f61·f54 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 변경 관리 | Management of Change (MOC) | 설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다. |
| 안전 상태 보고 | Safety State (VDA 5050 safetyState) | VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다. |
| 무선 안전 비상정지 | Wireless Safety-rated Emergency Stop | 관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이다. |

## 열린 질문

새로 생긴 질문:

- 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? | 관련 영역: 48. 안전·위험 관리, 42. 분산 시스템·통신·컴퓨팅 구조, 29. 명령·작업 실행의 신뢰성 | 근거: f49 | 종류: 일반
- ISO 13482 개정 초안(ISO/DIS 13482:2024)의 승강기 협동 로봇 요구(부속서 H)는 국내 KS B 7317 과 어떻게 대응하며, 이 요구가 최종판에 남았는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 22. 설비·건물 시스템 연동 | 근거: f23 | 종류: 일반
- 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? | 관련 영역: 48. 안전·위험 관리, 38. 모니터링·이상 탐지·원인 분석, 54. 시험·형식 검증·벤치마크 | 근거: f46 | 종류: 일반
- 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 66. 실외 | 근거: f5 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 48 · 교차 확인: 2
- 예산 사용량: 검색 11회 · 신규 출처 8건
- 미확인 항목:
    - EU 기계류 규정 (EU) 2023/1230 원문(ref-555)을 EUR-Lex 에서 두 번 열었으나 빈 본문이 돌아와 실질적 변경 정의·부속서 III 1.1.9 를 확인하지 못함(finding 으로 내지 않음)
    - Intertek 의 'EN ISO 13482:2026' 표기는 페이지가 403 으로 열리지 않아 쓰지 않음(ref-1117 의 FDIS 단계와 충돌 가능성 미확인)
    - 대한민국 정책브리핑(ref-991)은 ECONNRESET 으로 열지 못해 보험 의무 교차 확인 실패(f4 단일 출처)
    - 법무법인 지평 PDF 는 본문 추출 실패로 쓰지 않음
    - f49·f68 벤더 주장은 독립 출처로 확인하지 못함
    - f3 의 R15.08-3 발행일은 A3 판매 페이지 기준(2026-04-23)이며, 공개 발표(2026-10-04)와 날짜가 다름
    - ISO 10218-1:2025 사이버보안 요구의 조항 번호는 확인하지 못함(oq-102)
    - 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육의 교육 내용·시간은 확인하지 못함
    - 재사용 출처 40건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f17: SLAM 위치추정 안전성은 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작
    - f41: 기능안전 인증과 시뮬레이션 인정은 인증 기관·제조사 몫이라 '연계 대상: '으로 시작
    - f18·f19·f22·f24: 승강기 모드 제어와 탑승 안전은 시설·설비 제어 경계의 연계 대상이며, ROP 는 확인·요청 범위로만 서술
    - f9~f12·f32·f49: 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능은 로봇 제조사·통합자 몫의 연계 대상이며, ROP 는 상태 수신과 작업 보류·재개로만 서술
    - f4·f5·f55·f59·f65·f66: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며, ROP 는 인증·운행 조건을 제약으로 반영하는 범위로만 연결
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 48·49·50 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-07, 2026-10-09-08)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 40건, 이번에 다시 연 것은 ref-031(github_raw)·ref-1116(webfetch) 2건이고 나머지 38건은 fetched false·source_unopened true). 신규 출처는 8건(ref-1419~ref-1426, 예약 구간 안)이고 모두 원문 페이지를 열었다. 다만 ref-1419·ref-1420·ref-1425 는 유료 표준의 공식 소개 자료여서 표준 본문은 보지 못했다. 검색 11회/30, 신규 출처 8건/15. 교차 확인 2건(f47 R15.08-3 사용자 의무, f54 ISO 10218 사이버보안). 벤더 주장 2건(f49·f68). 한국 자료: 신규 ref-1423(법제처 해석)·ref-1424(기사), 재사용 ref-562·ref-945·ref-980·ref-1118·ref-1124·ref-1125·ref-1181·ref-1341. 현장 유형: 물류창고·제조 공장·병원·상업 시설(시뮬레이션 예제)·가정·실외·기타 각 1건 이상이며, 상업 시설의 실제 현장 사례는 찾지 못했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f18·f19)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f38·f39)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f51~f53)은 적용 대상인 48. 안전·위험 관리와 함께 제안했다. 열린 질문 가운데 oq-095(f32·f33·f50), oq-254(f23·f24, 초안 기준), oq-265(f47·f48, 이행 주체 미확인), oq-275(f59·f60, 지침 미확인), oq-102(f54, 조항 미확인), oq-229(f15)에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)를 따라 '5'로 매겼다 [가정]. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-09-30-12/research.md

```markdown
# 리서치 브리프 2026-09-30-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-12 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 33. 시나리오 모델·편집 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 시나리오 기술 언어, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 장애 주입 선언, 반증 기반 시험 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(호텔·공항)·병원(클리닉)·실외(캠퍼스)·가정(가정 활동)·제조 공장(배터리 생산) 시나리오 예제와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 확률적 시나리오 언어, 건물 주석 편집기, 행동 트리·BPMN 같은 미션 형식, LLM 기반 환경·시나리오 생성 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ASAM OpenSCENARIO, SDFormat, VDMA LIF, Open-RMF rmf_demos·traffic-editor, BEHAVIOR-1K·BDDL, NIST ARIAC, MovingAI MAPF 벤치마크, Groot2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131·oq-135 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]
2. 로봇 시뮬레이션·자율 시스템 시험에서 쓰는 시나리오 기술 형식·언어는 무엇이며 환경·개체·작업·사건·장애를 어떻게 나누어 담고 판(버전)을 어떻게 관리하는가? (섹션 4·6·7 겨냥)
3. 현장 유형별(호텔·병원·공장·가정·실외·물류창고) 시나리오 예제·템플릿 라이브러리로 공개된 것은 무엇이고 각각 무엇을 담는가? (섹션 5·7 겨냥, 한국 자료 우선)
4. 사람이 화면에서 시나리오·워크플로·미션을 그리고 고치는 편집기와 미션 기술 형식(행동 트리·상태 기계·BPMN 등)은 무엇이며 비교 연구는 무엇을 말하는가? (섹션 6·7·8 겨냥)
5. 언어 모델로 시뮬레이션 환경·시나리오를 자동 생성하는 연구는 무엇을 입력으로 받아 무엇을 만들고 어떻게 평가했는가? (섹션 6·8 겨냥, 9. 채팅으로 시나리오 구성과의 연결)
6. oq-131 플릿 관제 실행 기록을 시나리오 사양으로 바꾸는 공개 형식·변환 규칙, oq-135 시나리오 구성 시 되물어야 할 항목의 표준 목록이 있는가? (섹션 11 겨냥)
7. 33. 시나리오 모델·편집에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·로봇 제조사·설비 쪽에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Vin 외의 Scenic 3.0(CAV 2023)은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어 Scenic 에 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, 선형 시간 논리(LTL)로 쓰는 시간 요구사항을 더해 반증(falsification) 기반 시험에 쓸 수 있게 했다. | ref-1135 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | ASAM OpenSCENARIO XML 은 주행·교통 시뮬레이터의 동적 내용(차량·보행자 등 여러 개체의 동기화된 기동)을 계층 구조의 XML 파일(.xosc)로 기술하는 표준으로, 2026-05-19 에 1.4.0 판이 나왔고, 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화할 수 있게 한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f3 | [사실] | ASAM 은 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO XML 은 그 위의 동적 내용만 담게 나누며, 병행 표준 OpenSCENARIO DSL 은 대규모 검증용, XML 은 예측 가능한 정밀 시나리오용으로 역할을 구분한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f4 | [사실] | Open-RMF 의 rmf_demos 는 호텔 월드로 로비와 객실 2개 층, 승강기 2대, 여러 문, 로봇 플릿 3개(로봇 4대)가 층을 오가며 순찰(loop)·청소 작업을 하는 다중 플릿 시나리오를 예제로 제공한다. | ref-104 | 아니오 | medium | 2026-09-30 | 상업 시설 / 수행 자원 | — |
| f5 | [사실] | rmf_demos 의 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 여러 플릿과 설비·이용자의 상호작용을 보이며, 선택적으로 군중 시뮬레이션을 켜고 사람이 직접 모는 읽기 전용(read_only) 카트를 함께 두고 순찰·배송·청소 작업을 실행한다. | ref-104 | 아니오 | medium | 2026-09-30 | 상업 시설 / 제약 | — |
| f6 | [사실] | rmf_demos 의 클리닉 월드는 승강기 2대가 있는 2개 층 시설에서 역할이 다른 로봇 플릿 2개가 층을 오가며 간호 스테이션 사이를 순찰하는 병원형 시나리오 예제다. | ref-104 | 아니오 | medium | 2026-09-30 | 병원 / 제약 | — |
| f7 | [사실] | rmf_demos 의 캠퍼스 월드는 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스에서 여러 배송 로봇이 장거리 순찰을 하는 실외 시나리오 예제이고, 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다. | ref-104 | 아니오 | medium | 2026-09-30 | 실외 / 작업 대상 | — |
| f8 | [사실] | rmf_demos 에서 시나리오는 월드(건물 구성·차선·승강기·문·충전 위치)를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣는 구조이며, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다. | ref-104 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f9 | [사실] | Open-RMF 의 traffic-editor 는 시설 지도 위에 벽·문(여닫이·미닫이·양문)·층·승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, 층 정렬용 기준점을 그려 넣는 GUI 편집기로, 결과를 .building.yaml 파일로 저장하고 building_map_generator 가 이를 물리 시뮬레이션 월드로 자동 생성한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f10 | [사실] | Stanford 등의 BEHAVIOR-1K(arXiv 2403.09227, 예비판 CoRL 2022)는 '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(BDDL)로 형식 명세하고, 주택·정원·식당·사무실 등 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상, 강체·변형체·액체를 다루는 OmniGibson 시뮬레이터 위에 구현한 활동 라이브러리다. | ref-971 | 아니오 | medium | 2024-03 | 가정 / 작업 대상 | — |
| f11 | [사실] | NIST ARIAC 문서의 시나리오는 전기차 배터리 생산 시설로, 배터리 셀 4개를 트레이에 담는 키팅과 셀 4개와 상하 케이스로 모듈을 조립하는 두 작업을 주문으로 받고, 우선순위가 높은 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않게 정한다. | ref-1140 | 아니오 | medium | 2026-09-30 | 제조 공장 / 작업 대상 | — |
| f12 | [사실] | NIST ARIAC 는 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(시작·지속·대상 TESTER), 진공 그리퍼 파지 실패(TOOL·몇 번째 파지인지 GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID) 네 가지 민첩성 과제를 매개변수로 선언해, 장애와 긴급 요청을 시각 또는 발생 횟수 조건으로 시나리오에 주입한다. | ref-528 | 아니오 | medium | 2026-09-30 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Kästner 외의 Arena-Bench(RA-L 2022)는 동적 환경의 시나리오·월드 생성 도구와 평가 지표를 갖춘 벤치마크 모음으로, 3차원 환경에서 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오로 비교하고 실물 로봇 배치까지 보였다. | ref-726 | 아니오 | medium | 2022-06 | — | — |
| f14 | [사실] | Shcherbyna 외의 Arena 4.0(arXiv 2409.12471)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다. | ref-1143 | 아니오 | medium | 2024-09 | — | — |
| f15 | [사실] | Yang 외의 Holodeck(CVPR 2024)은 GPT-4 가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하는 방식으로 오락실·스파·박물관 같은 상호작용 가능한 환경을 자동 생성하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했고 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다. | ref-815 | 아니오 | medium | 2023-12 | — | — |
| f16 | [추정] | 행동 트리 편집기 Groot2 는 끌어놓기로 트리를 만들며 XML 을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다. | ref-1145 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [사실] | Filippone·Pettinari·Pelliccione(IEEE TSE, arXiv 2603.15427)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·표현력·도구 지원 측면에서 비교하며, 미션을 명세하는 표준이나 널리 받아들여진 형식이 없고 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다고 지적했다. | ref-116 | 아니오 | medium | 2026-03 | — | — |
| f18 | [사실] | Moving AI 연구실의 MAPF 벤치마크는 도시·게임·창고형·무작위·미로·방 등 격자 지도 36개마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 모두 1,800개의 시나리오 파일을 공개한 재사용 가능한 시나리오 라이브러리다. | ref-1147 | 아니오 | medium | 2026-09-30 | — | — |
| f19 | [사실] | SDFormat(Simulation Description Format)은 로봇 시뮬레이터·시각화·제어용으로 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo 에서 시작했고 Open Source Robotics Foundation 이 Apache 2.0 으로 관리한다. | ref-1148 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰는 비구속적 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받아 만들어졌다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f21 | [추정] | 확인한 형식들은 공통으로 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃, OpenDRIVE 도로망)과 동적 내용(작업 명령, OpenSCENARIO 스토리보드, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하며, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 두지만 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다. | ref-1148, ref-079, ref-046, ref-1141, ref-104, ref-528, ref-971 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 공개 형식은 분야별로 나뉘어(자율주행 OpenSCENARIO, 가정 활동 BDDL, 시설 다중 로봇 Open-RMF 건물 파일과 작업 명령, 제조 ARIAC 과제 설정, MAPF .scen) 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 찾지 못했고 미션 기술에도 표준이 없으며(f17), 재사용은 매개변수화·카탈로그(f2), 확률 분포 표본 추출(f1), 현장 유형별 예제 월드(f4~f7), 대규모 활동·시나리오 라이브러리(f10·f18), 언어 모델 생성(f14·f15)으로 이루어지는 것으로 보인다. | ref-1141, ref-971, ref-104, ref-528, ref-1147, ref-116, ref-1135, ref-1143, ref-815 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 계획기·정책을 같은 조건에서 비교하려면 고정된 시나리오 파일이 있어야 하고(f13·f18), 장애·긴급 요청을 시나리오에 선언해야 예외 대응 시험을 반복할 수 있으며(f12), 매개변수화가 없으면 조건별 시나리오 파일이 불어나고(f2), 비전문가가 미션과 환경을 정의해야 하는데 공통 형식이 없기 때문이다(f17). | ref-726, ref-1147, ref-528, ref-1141, ref-116 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 확인한 자료를 종합하면 33. 시나리오 모델·편집에서 ROP가 직접 맡을 범위는 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 버전 있는 시나리오 모델(f8·f12·f21), 현장 유형별 예제 라이브러리(f4~f7), 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택(f9·f16·f17), 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환(f9·f19)으로 보인다. | ref-104, ref-528, ref-079, ref-1145, ref-116, ref-1148 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 로봇 기구학·센서 모델(SDFormat 로봇 기술, f19)은 시뮬레이터·로봇 제조사 쪽에, 컨베이어·작업셀 같은 설비 제어(f7·f12)는 설비 쪽에, 도로 교통 시나리오 표준(f2·f3)은 자율주행 분야에 속하므로, ROP 는 이들을 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. | ref-1148, ref-104, ref-528, ref-1141 | 아니오 | low | 2026-09-30 | — | — |
| f26 | [추정] | 이 영역은 시나리오를 대화로 만드는 9. 채팅으로 시나리오 구성(f14·f15)과 11. 채팅으로 실제 상황 시뮬레이션 재현, 시나리오를 실행하는 34. 시뮬레이션·예측용 디지털 트윈(f19), 기록 재생·재현의 36. 가상 시운전·실제 상황 재현(f16), 규모 산정의 35. 처리능력·규모·배치 설계, 건물·레이아웃 주석의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f9·f20), 군중·보행자의 19. 사람·보행자 모델(f5·f14), 승강기 연동의 22. 설비·건물 시스템 연동(f4·f6), 미션 형식의 24. 작업·워크플로 모델링(f17), 장애 주입의 32. 예외 복구·재계획·업무 연속성(f12), 경로 시나리오의 27. 다중 로봇 경로·교통 관리 — MAPF(f18), 언어 모델 생성의 44. 로봇 기반 모델·언어 모델 계획(f15), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f13·f18), 적용 현장인 62. 제조 공장(f11·f12)·63. 병원·의료(f6)·64. 상업 시설(f4·f5)·65. 가정·공동주택(f10)·66. 실외(f7)와 이어진다. | ref-1143, ref-815, ref-1148, ref-1145, ref-079, ref-046, ref-104, ref-116, ref-528, ref-1147, ref-1135, ref-726, ref-1140, ref-971 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1135 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.03325 | 아니오 |
| ref-104 | Open-RMF (open-rmf/rmf_demos) | rmf_demos — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-079 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Traffic Editor | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.09227 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Challenges | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1140 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 아니오 |
| ref-1141 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | high | 2026-09-30 | https://www.asam.net/standards/detail/openscenario-xml/ | 아니오 |
| ref-726 | Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv) | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2206.05728 | 아니오 |
| ref-1143 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.12471 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-1145 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.behaviortree.dev/groot/ | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1147 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://movingai.com/benchmarks/mapf/index.html | 아니오 |
| ref-1148 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | http://sdformat.org/ | 아니오 |
| ref-046 | VDMA (Intralogistics-2X-LIF) | Layout Interchange Format (LIF) — README | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f23(왜 중요한가), f22(핵심 질문 답, 추정) / 섹션 4: 확률적 시나리오 언어·반증 f1, 매개변수화·카탈로그 f2, 정적 환경과 동적 내용 분리 f3·f21, 장애 주입 선언 f12, 미션 기술 형식 f17 / 섹션 5: 상업 시설 — f4(호텔, 수행 자원)·f5(공항 터미널, 제약: 군중·수동 카트), 병원 — f6(클리닉, 제약: 층간 승강기), 실외 — f7(캠퍼스, 작업 대상: WGS84 공간), 가정 — f10(일상 활동 라이브러리), 제조 공장 — f11(배터리 생산 작업 대상)·f12(장애 주입 예외·성과). 물류창고는 f18 격자 지도와 f20 레이아웃 형식뿐이고 실제 현장 사례는 찾지 못함을 명시 / 섹션 6: 확률적 언어 f1, 건물 주석 편집 f9, 월드+작업 명령 구조 f8, 미션 형식 비교 f17, 행동 트리 편집·재생 f16(벤더 주장 병기), 언어 모델 기반 환경 생성 f14·f15 / 섹션 7: ASAM OpenSCENARIO f2·f3, SDFormat f19, VDMA LIF f20, Open-RMF rmf_demos·traffic-editor f4~f9, BEHAVIOR-1K·BDDL f10, NIST ARIAC f11·f12, MovingAI MAPF f18, Arena f13·f14, Groot2 f16 / 섹션 8: f1·f10·f13·f14·f15·f17 / 섹션 9: f24(직접 범위), f25(연계 대상) / 섹션 10: f26 — 9, 11, 14, 15, 19, 22, 24, 27, 32, 34, 35, 36, 44, 54, 62, 63, 64, 65, 66 / 섹션 11: 기존 oq-131·oq-135(미해결)와 open_questions_new 4건. 다음 실행 후보: 9. 채팅으로 시나리오 구성 페이지에 f14·f15, 36. 가상 시운전·실제 상황 재현 페이지에 f12·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 오픈시나리오 | ASAM OpenSCENARIO | ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다. |
| 행동 영역 정의 언어 | Behavior Domain Definition Language (BDDL) | BEHAVIOR 벤치마크가 가정 활동을 시뮬레이션된 물리 상태와 연결된 논리 술어로 형식 명세하는 데 쓰는 도메인 특화 언어다. |
| 시뮬레이션 기술 형식 | Simulation Description Format (SDFormat) | Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다. |
| 반증 기반 시험 | Falsification | 시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다. |

## 열린 질문

새로 생긴 질문:

- 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 관련 영역: 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f21 | 종류: 일반
- 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 65. 가정·공동주택 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f10 BDDL 이 활동을 초기 조건·목표 조건 쌍으로 정의한다는 세부 구조는 검색 요약에만 있어 claim 에 넣지 않음
    - f1 Scenic 이 한 프로그램에서 표본 추출로 여러 장면을 만든다는 설명과 로봇 적용 사례(암석 지대)는 검색 요약에만 있어 넣지 않음
    - f15 Holodeck 3D 자산 수(약 5만 개)는 검색 요약에만 있어 넣지 않음
    - f13 Arena 시나리오 편집기의 끌어놓기 배치·보행자 웨이포인트 기능은 검색 요약에만 있어 넣지 않음
    - f16 Groot2 기능은 제품 페이지뿐이며 독립 출처로 교차 확인하지 못함
    - f2 OpenSCENARIO XML 1.4.0 명세 본문은 열지 않았고 공식 소개 페이지 기준
    - oq-131 미해결: 플릿 실행 기록을 시나리오로 바꾸는 공개 형식은 찾지 못함(찾은 JoyAI-Sim arXiv 2606.16776 은 탁상 조작 과제 재구성이라 제외)
    - oq-135 미해결: 시나리오 구성 시 되물을 항목의 표준 목록은 이번 조사에서 찾지 못함(검색하지 못함)
    - 물류창고 실제 현장의 시나리오 예제·템플릿 사례와 국내 자료는 찾지 못함
    - Bourr·Tiezzi 의 BPMN→X-Klaim 변환(arXiv 2311.04126)은 철회된 논문이라 제외
    - Moskovskaya 외 안내 로봇 LLM 시나리오 생성(arXiv 2509.10317)은 대화 행동 대본 의미의 시나리오라 제외
- 범위 경계 위반 의심:
    - f19: SDFormat 의 로봇 기구학·센서 기술은 로봇 제조사·시뮬레이터 쪽 내용이므로 형식 참조 근거로만 쓰고 f25 에서 연계 대상으로 구분함
    - f2·f3: OpenSCENARIO 는 자율주행 도로 시나리오 표준이므로 ROP 직접 범위가 아니라 참조 설계 사례로만 제안함
    - f7·f12: 컨베이어·작업셀 설비 제어는 설비 쪽 연계 대상이며 시나리오에 장애를 선언하는 방식만 근거로 씀
    - f8·f21: 시나리오는 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 섞지 않음
    - f14·f15: 언어 모델 기반 생성은 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획)과 9. 채팅으로 시나리오 구성에도 연결하도록 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1135~ref-046, 예약 구간 안)로 출처 상한에 도달해 물류창고 실제 현장 시나리오와 국내 자료, oq-135 조사를 더 하지 못했다. 재사용 출처 없음: NIST ARIAC 는 공통 규칙상 ref-008 이지만 입력 참고문헌 요약에 ref-008 의 등록 URL·제목이 없어 이번에 연 개별 문서 페이지(challenges·scenario)를 새 id(ref-528·ref-1140)로 적었다. 같은 URL 이면 퍼블리셔가 합치고, 다르면 ref-008 과의 관계를 검증에서 확인해 주기 바란다. 원문 열람: 15건 모두 열었다(webfetch 10건, github_raw 5건). 논문은 모두 초록 페이지 기준이다. VDMA LIF 지침 PDF 는 본문 추출에 실패해 공식 저장소 README 로 대신했다. 교차 확인 0건: 각 형식·사례가 한 출처에만 기술되어 있어 finding 신뢰도는 medium 이하로 두었다. Groot2 기능(f16)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에는 f22 로 답했고 결론은 '공개 형식은 분야별로 나뉘고 공통 표준은 없으며, 재사용은 매개변수화·표본 추출·예제 라이브러리·언어 모델 생성으로 이루어진다'는 추정이다. 현장 유형 사례는 상업 시설(f4·f5)·병원(f6)·실외(f7)·가정(f10)·제조 공장(f11·f12)이며 물류창고는 격자 지도 벤치마크(f18)와 레이아웃 교환 형식(f20)만 있고 현장 사례는 찾지 못했다. 국내 자료는 한국어 검색 2회에서 이 영역에 맞는 것을 찾지 못했다(찾은 한국지능시스템학회 시뮬레이터 리뷰는 시나리오 정의를 다루지 않아 제외). 기존 열린 질문 oq-131·oq-135 는 해결 근거가 없어 해결 제안하지 않았다. 용어집에 이미 있는 행동 트리·BPMN·HTN·레이아웃 교환 형식·가상 시운전·시나리오 재구성·미션 명세 패턴은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |

A vertex is a fundamental component of multiple annotations.
Walls, measurements, doors, floor polygons and traffic lanes are created from two or more vertices.
To create a vertex, click on the vertex icon in the `Toolbar` and then click anywhere on the canvas.
The default attributes of a vertex are its coordinates along with an empty name field.
Additional attributes may be added by first selecting the vertex (which will turn it red), and then clicking the `Add` button in the figure.
Short descriptions of these are presented below:
* **is_holding_point:** if true and if the waypoint is part of a traffic lane,
  the `rmf_fleet_adapter` will treat this as a _holding point_ during path
  planning, i.e., the robot is allowed to wait at this waypoint for an indefinite
  period of time.
* **is_parking_spot:** robot's parking spot. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L73-L76)
* **is_passthrough_point:** waypoint which the robot shouldnt stop. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L63-L68)
* **is_charger:** if true and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will treat this as a charging station.
* **is_cleaning_zone** indicate if current waypoint is a cleaning zone, specifically for `Clean` Task.
* **dock_name:** if specified and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will issue an `rmf_fleet_msgs::ModeRequest` message with
  `MODE_DOCKING` and `task_id` equal to the specified name to the robot as it approaches this waypoint. This is used when the robot is executing their custom docking sequence (or custom travel path).
* **spawn_robot_type:** the name of the robot model to spawn at this waypoint in
  simulation. The value must match the model's folder name in the assets
  repository. More details on the robot model and plugin required for simulation
  can be found in [Simulation](simulation.md)
* **spawn_robot_name:** a unique identifier for the robot spawned at this
  waypoint. The `rmf_fleet_msgs::RobotState` message published by this robot
  will have `name` field equal to this value.
* **pickup_dispenser** name of the dispenser workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **dropoff_ingestor** name of the ingestor workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **human_goal_set_name** The `goal_sets.set_area` name, used by crowd simulation. For more info about `crowd_sim`, please see the [Crowdsim section] (https://osrf.github.io/ros2multirobotbook/simulation.html#crowdsim) of the Simulation Chapter for more details.

![Vertex attributes](images/traffic_editor/add_vertex.png)

Each vertex is stored in the `tutorial.building.yaml` file as a list of x-coordinate, y-coordinate, elevation, vertex_name and a set of additional parameters.

```yaml
  vertices:
    - [1364.76, 1336.717, 0, magni1_charger, {is_charger: [4, true], is_parking_spot: [4, true], spawn_robot_name: [1, magni1], spawn_robot_type: [1, Magni]}]
```
### Adding a measurement
|                    Icon                    |
|:------------------------------------------:|
| ![Measurement icon](images/traffic_editor/icons/measurement.svg)|

Adding a measurement sets the scale of the imported 2D drawing, which is essential for planning and simulation accuracy.
Scalebars or reference dimensions in the floor plan aid with the process. Often, you can draw the measurement line directly on top of a reference scale bar in a drawing.
With the editor in _Building_ mode, select the _Add Measurement_ tool and click on two points with known dimensions.
A pink line is rendered on the map with two vertices at its ends at the selected points.

Note:
A measurement line may be drawn by clicking on existing vertices.
In this scenario, no additional vertices are created at its ends.

Selecting the line populates various parameters in the Properties window of the `Sidebar`.
Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.
Currently, you must save the project and restart `traffic-editor` to see the changes reflected (todo: fix this...).

![Measurement properties](images/traffic_editor/add_measurement.png)

The above process adds two `vertices` and a `measurement` field to the `tutorial.building.yaml` file as seen below.
For the measurement field, the first two elements represent the indices of vertices representing the ends of
the line.
The `distance` value is stored in a sub-list of parameters.

```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
    measurements:
      - [1, 0, {distance: [3, 8.409]}]
    vertices:
      - [2951.728, 368.353, 0, ""]
      - [2808.142, 1348.9, 0, ""]

lifts:
  {}
name: building
```

### Adding a wall
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Wall icon](images/traffic_editor/icons/wall.svg)| `w` |

To annotate walls in the map, select the _Add Wall_ icon from the `Toolbar` and click on consecutive vertices that represent the corners of the wall.
The process of adding wall segments is continuous, and can be exited by pressing the `Esc` key.
Blue lines between vertices are rendered on the map which represent the drawn walls.
If the corner vertices are not present, they will automatically be created when using this tool.
Meshes of the annotated walls are automatically generated during 3D world generation using `building_map_generator`.
By default, the walls are of thickness of 10cm and height 2.5m.
The `wall_height` and `wall_thickness` attributes may be
modified [in the source code](https://github.com/open-rmf/rmf_traffic_editor/blob/main/rmf_building_map_tools/building_map/wall.py#L16-L17).

Wall texture options are available [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) in the source code.

![Annotating walls](images/traffic_editor/add_wall.png)

Walls are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices of the wall segment along with an empty parameter set.
```yaml
    walls:
      - [3, 4, {}]
      - [4, 5, {}]
      - [5, 6, {}]
      - [6, 7, {}]
      - [6, 8, {}]
      - [8, 9, {}]
```

### Adding a floor
|                    Icon                    |
|:------------------------------------------:|
| ![Floor icon](images/traffic_editor/icons/floor.svg)|

Flooring is essential for simulations as it provides a ground plane for the robots to travel over.
Floors are annotated using the _Add floor polygon_ tool from the `Main Toolbar` in _Building_ edit mode.
To define a floor, select consecutive vertices to create a polygon that accurately represents the flooring area as seen below.
These vertices will need to be added manually prior to this step.
Once created, save the project and reload.
Selecting the defined floor highlights its texture attributes. Similarly, [default list of available textures](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) is available in the source code.

![Highlighting floor's textures](images/traffic_editor/add_floor.png)

Certain scenarios may call for floors with cavities, for example, to represent elevator shafts.
The _Add hole polygon_ tool may be used for this purpose.
Additionally, the shape of a drawn polygon (floor or hole) may be modified using the _Edit polygon_ tool.
Clicking on the tool after selecting an existing polygon enables the user to modify vertices of the polygon.

Each polygon is stored in the `tutorial.building.yaml` file in the format below:
```yaml
    floors:
      - parameters: {texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [11, 10, 14, 15, 13, 12]
```

### Adding a door
|                    Icon                    |
|:------------------------------------------:|
| ![Door icon](images/traffic_editor/icons/door.svg)|

A door between two vertices can be added in _Building_ edit mode by selecting the _Add door_ tool from the `Main Toolbar`, and clicking on vertices representing the ends of the door.
Selecting an annotated door highlights its properties as seen in the figure below.
Presently, four door `types` are supported: "hinged", "double_hinged", "sliding" and "double_sliding".
The `motion_degrees` parameter specifies the range of motion in the case of hinged doors while the `motion_direction` dictates the direction of swing.
In order for the door to work in simulation, a `name` must be given to the door.

![Door type properties](images/traffic_editor/add_door.png)

Doors are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices along with the set of parameters that describes the door.

```yaml
 doors:
      - [24, 25, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, 1], name: [1, D001], type: [1, double_sliding]}]
```

### Adding a traffic lane
One of the most important tools in the `traffic_editor` GUI is the _Add lane_ tool.
The allowable motions of each fleet operating in the facility is conveyed through its respective Graph which consists of waypoints and connecting lanes.
In this approach, we assume that robots travel along effectively straight-line paths between waypoints.
While this may be perceived as an oversimplification of paths taken by robots that are capable of autonomous navigation, in practice the assumption holds fairly well given that these robots mostly travel along corridors or hallways and seldom in unconstrained open spaces.
For example, even in theoretically unconstrained spaces like building lobbies or shopping-mall atriums, it is likely that the site operator would prefer for the robots to operate in a "traffic lane" on the edge of the space, in order to not impede typical human traffic flows.

The `traffic` tab in the `Sidebar` has a default of nine Graphs for nine different fleets. To annotate lanes for a graph, say Graph 0, select the Graph from the `traffic` tab and click the _Add lane_ tool.
Lanes for this graph can be drawn by clicking vertices to be connected.
If a vertex is not present, it will automatically be added. Properties may be assigned to each vertex as described in the preceding section.
To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint.

![Graphs' lane colors](images/traffic_editor/add_lane.png)

Each Graph has a unique color for its lanes, and their visibility may be toggled using the checkbox in the `traffic` tab.
A lane that is defined between two waypoints may be configured with these additional properties:
* **bidirectional:** if `true`, the `rmf_fleet_adapter` will plan routes for its
  robot assuming the lanes can be traversed in both directions. Lanes that are
  not bidirectional have arrows indicating their directionality (indigo lanes in
  figure above). A handy shortcut is that when a lane segment is selected, you can
  press the `b` key to toggle between unidirectional and bidirectional motion along that lane.
* **graph_idx**: the Graph number a lane corresponds to
* **orientation**: constrain the lane to make the robot travel in `forward` or `backward` orientation. This can be useful for the final lane segment approaching a docking point or charger, for example.

While lifts that move between levels are now supported in the `traffic_editor`, the **demo_mock_floor_name** and **demo_mock_lift_name** properties were originally engineered to showcase shared lift access in a single floor demonstration environment with a "mock" lift that receives lift commands and transmits lift states but does not actually move between any different floors in a building.
However, as there may be interest in such functionality for testing single-floor hardware setups that seek to emulate multi-floor scenarios, these properties were retained.

* **demo_mock_floor_name**: name of the floor that the robot is on while
  traversing the lane
* **demo_mock_lift_name**: name of the lift that is being entered or exited
  while the robot traverses the lane

To further explain these properties, consider this representation of a
navigation graph where numbers are waypoints and letters are lanes:
```
1 <---a---> 2 <---b---> 3

Waypoint 1 is on floor L1
Waypoint 2 is inside the "lift" named LIFT001
Waypoint 3 is on floor L3
The properties of edge "a" are:
    bidirectional: true
    demo_mock_floor_name: L1
    demo_mock_lift_name: LIFT001
The properties of edge "b" are:
    bidirectional: true
    demo_mock_floor_name: L3
    demo_mock_lift_name: LIFT001
```

If the robot is to travel from waypoint 1 to waypoint 3, the `rmf_fleet_adapter` will request for the "mock lift" to arrive at L1 when the robot approaches waypoint 1.
With confirmation of the "lift" at L1 and its doors in "open" state, the robot will be instructed to move into the "lift" to waypoint 2.
Once the "lift" indicates that it has reached L3, the robot will exit along lane b toward waypoint 3.

Note: when annotating graphs, it is highly recommended to follow an ascending sequence of graph indices without skipping intermediate numbers. Drawn lanes can only be interacted with if their associated Graph is first selected in the `traffic` tab.

The annotated Graphs are eventually exported as `navigation graphs` using the `building_map_generator` which are then used by respective `rmf_fleet_adapters` for path planning.

Lanes are stored in the following format in `tutorial.building.yaml`.
The data structure is a list with the first two elements representing the indices of the two vertices of the lane and a set of parameters with configured properties.
```yaml
    lanes:
      - [32, 33, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 2], orientation: [1, forward]}]
```

### Deriving coordinate-space transforms

Coordinate spaces are confusing!
For historical reasons, the GUI internally creates traffic maps by annotating images, so the "raw" annotations are actually encoded in pixel coordinates of the "base" floorplan image, in pixel coordinates, with +X=right and +Y=down, with the origin in the upper-left of the base floorplan image.
However, during the building map generation step, the vertical axis is flipped to end up in a Cartesian plane, so the vast majority of RMF (that is, everything downstream of traffic-editor and the building map generators) uses a "normal" Cartesian coordinate system. (As an aside -- the next version of traffic-editor is intended to be more flexible in this respect, and will default to a normal Cartesian coordinate system (not an image-based coordinate system), or even global coordinates (lat/lon). Although preliminary work is underway, there is not a hard schedule for this next-gen editor at time of writing, so the rest of this chapter will describe the existing `traffic-editor`.)

Although `traffic-editor` currently uses the upper-left corner of the base floorplan image as the reference frame, maps generated by robots likely will have their origin elsewhere, and will likely be oriented and scaled differently.
It is critical to derive the correct transform between coordinate frames in `traffic_editor` maps and robot maps as
`rmf_fleet_adapters` expect all robots to publish their locations in the RMF coordinate system while the `rmf_fleet_adapters` also issue path requests in the same frame.

To derive such transforms, the `traffic_editor` GUI allows users to overlay robot maps on a floor plan and apply scale, translation and rotation transformations such that the two maps align correctly.
The user can then apply the same transformations to convert between robot map and RMF coordinates when programming interfaces for their robot.

The robot map can be imported by clicking the `Add` button from the `layers` tab in the `Sidebar`.
A dialog box will then prompt the user to upload the robot map image.
The same box contains fields for setting the scale for the image along with applying translations and rotation.
Through visual feedback, the user can determine appropriate values for these fields.
As seen in the image below, importing the robot-generated map into the GUI has it located and oriented
differently than the floor plan.
With the right transformation values, the two maps can be made to overlap.

![Overlap robot-generated map](images/traffic_editor/coordinate_transform.png)

### Adding fiducials
|                    Icon                    |
|:------------------------------------------:|
| ![Fiducial icon](images/traffic_editor/icons/fiducial.svg)|

For maps with multiple levels, fiducials provide a means to scale and align different levels with respect to a reference level.
This is crucial for ensuring dimensional accuracy of annotations across different levels and aligning the
same for simulation.
Fiducials are reference markers placed at locations which are expected to be vertically aligned between two or more levels.
For example, structural columns may run through multiple floors and their locations are often indicated on floor plans.
With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived between the two levels.
This transformation can then be applied to all the vertices and models in the newly defined level.

To begin, add two or more non-collinear fiducials to the reference level with unique `name` attributes using the _Add fiducial_ tool (left image in figure below).
In the newly created level, add the same number of fiducials at locations that are expected to be vertically aligned with matching names as the reference level (right image in figure below).
Saving and reloading the project computes the transformation between the levels which is evident from the Scale
and X-Y offsets for the new level as seen in the `levels` tab.
This level is now ready to be annotated.

![Adding fiducials](images/traffic_editor/add_fiducial.png)

For each level, fiducials are stored in a list of their X & Y coordinates along with their name.
```yaml
    fiducials:
      - [936.809, 1323.141, F1]
      - [1622.999, 1379.32, F2]
      - [2762.637, 346.69, F3]
```

### Adding a lift
Lifts are integral resources that are shared between humans and robot fleets in multi-level facilities.
To add a lift to a building, click the `Add` button in the `lifts` tab in the `Sidebar`.
A dialog box with various configurable properties will load.
It is essential to specify the Name, Reference level and the X&Y coordinates (pixel units) of its cabin center.
A yaw (radians) may further be added to orient the lift as desired.
The width and depth of the cabin (meters) can also be customized.
Lifts can be designed to have multiple cabin doors which may open at more than one level.
To add a cabin door, click the `Add` button in the box below the cabin image.
Each cabin door requires a name along with positional and orientational information.
Here, the X&Y coordinates are relative to the cabin center.

![Configuring lift properties](images/traffic_editor/add_lift.png)

The configured lift is stored in the `tutorial.building.yaml` file as described below:
```yaml
lifts:
  LF001:
    depth: 2
    doors:
      door1:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: 1
        y: 0
      door2:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: -1
        y: 0
    level_doors:
      L1: [door1]
      L2: [door2]
    reference_floor_name: L1
    width: 2
    x: 827
    y: 357.7
    yaw: 1.09
```

After adding the lift, we would also wish to let our robots to transverse through the lift.
To achieve that, the user needs to create vertices/waypoints which are located within the lift cabin on each floor.
Once done, connect the waypoint within the lift cabin to other vertices via __add_lane__.

### Adding environment assets
Levels may be annotated with thumbnails of models available for simulation using the __Add model__ tool in __Building__ edit mode.
Selecting this tool opens a dialog box with a list of model names and matching thumbnails which can be imported to the map.
Once on the map, their positions and orientations can be adjusted using the _Move_ and _Rotate_ tools. Sample models are provided [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor_assets/assets/thumbnails/images/cropped/OpenRobotics)

The [thumbnail_generator documentation](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor#generating-custom-thumbnails) contains instructions on expanding the list of thumbnails for other models.

> Note: If no models are shown on the __add models__ window, Go to "Edit -> Preference", then indicate the thumbnail path. (`e.g. $HOME/rmf_ws/src/rmf/rmf_traffic_editor/rmf_traffic_editor_assets/assets/thumbnails`)

![Model name and thumbnails dialog](images/traffic_editor/add_model.png)

## Conclusion
This chapter covered various capabilities of the `traffic_editor` which are useful for annotating maps of facilities while adhering to a standardized set of semantics.
Examples of other traffic editor projects can be found in the [rmf_demos](https://github.com/open-rmf/rmf_demos) repository.
Running physics based simulations with RMF in the annotated sites is described in the [Simulation](simulation.md) chapter.
````

### data/source_texts/ref-528.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
.. _CHALLENGES:

==========
Challenges
==========

The agility challenges test teams' ability to adapt to unexpected situations and system failures during competition runs. Successfully handling these challenges is crucial for maintaining high performance and achieving competitive scores.

The competition incorporates challenges to test the robustness of team systems. Teams should be able to recognize when a challenge is occurring and properly handle the situation. There are four possible challenges that can occur during a run:

* **Conveyor Malfunction** - Inspection conveyor stops operating
* **Voltage Tester Malfunction** - One or both voltage testers stop providing data
* **Vacuum Tool Malfunction** - Vacuum gripper fails to grasp objects
* **High Priority Order** - Urgent kit request with time constraints

Conveyor Malfunction
====================

When the conveyor malfunction challenge occurs, the inspection conveyor will pause its motion. In addition, the cell feed will pause, so no new cells can be added during the challenge.

.. list-table:: Conveyor Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins (minimum: 0)
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts (minimum: 1)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring the conveyor status topic (:ref:`reference <inspection_challenge_anchor>`)
2. **Pausing the inspection system** to avoid conflicts
3. **Waiting for recovery** by monitoring the status topic until it reports operational status
4. **Resuming operations** once the conveyor and cell feed return to normal

Voltage Tester Malfunction
==========================

When the voltage tester malfunction occurs, one or both voltage testers will stop publishing data.

.. list-table:: Voltage Tester Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts
   * - ``TESTER``
     - int
     - Which voltage tester is affected (1 or 2)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring voltage tester topics for data availability (:ref:`reference <inspection_challenge_anchor>`)
2. **Adapting operations** to avoid using the affected voltage tester(s)
3. **Monitoring for recovery** by watching the status topic until operational status is restored
4. **Continuing progress** using any operational voltage testers to maintain productivity
5. **Resuming full operations** once all voltage testers return to operational status

Vacuum Tool Malfunction
=======================

When the vacuum tool malfunction occurs, a specified vacuum gripper will fail during grasp attempts.

.. list-table:: Vacuum Tool Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``TOOL``
     - int
     - Which vacuum tool is affected (1 or 2)
   * - ``GRASP_OCCURRENCE``
     - int
     - Which grasp attempt will fail (minimum: 1)

.. note::

  **TOOL**: Refers to the :ref:`vacuum gripper tools <vacuumtools_msg>` VG_2 and VG_4 available to assembly robot 2.

.. note::

  **GRASP_OCCURRENCE**: Specifies which attempt at grasping will fail. For example, if set to 3, the first two grasp attempts will succeed normally, but the third attempt will fail and require retry.

Teams are expected to handle this challenge by:

1. **Detecting the failure** by monitoring the response from the grasp service (:ref:`reference <vacuum_tool_challenge_anchor>`)
2. **Repositioning the gripper** by moving it away from the target object
3. **Retrying the grasp** with proper positioning and approach

High Priority Order
===================

When a high priority order is requested, an internal timer starts tracking completion time. Teams should minimize the time taken to submit this urgent kit request.

.. list-table:: High Priority Order Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the high priority order is announced
   * - ``ID``
     - string
     - Unique identifier for the high priority order

Teams are expected to handle this challenge by:

1. **Detecting the request** by monitoring the high priority order topic (:ref:`reference <high-priority-anchor>`)
2. **Switching cell feed** to begin feeding NiMH cells
3. **Building the kit** using four NiMH cells with proper voltage specifications
4. **Delivering the kit** by moving the AGV to the shipping location
5. **Submitting the order** using the high priority submission service with the correct order ID (:ref:`reference <high-priority-anchor>`)
6. **Restoring normal operations** by switching cell feed back to Li-ion batteries
7. **Resuming standard tasks** to continue regular production

Configuration Example
======================

For complete challenge configuration examples showing all challenge types with valid parameters, see the :ref:`Challenges Configuration Reference <challenges_config_example>`.
```
