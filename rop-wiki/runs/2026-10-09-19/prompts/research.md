(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/researcher.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-19
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 43. 데이터·관측성·배포 (K. 플랫폼 아키텍처·인프라)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- next_ref_id: ref-1367
- 새 출처 id 구간: ref-1367 ~ ref-1396 — 이 실행 전용으로 예약한 번호다(동시에 도는 다른 실행과 겹치지 않는다). 새 출처는 ref-1367 부터 순서대로 쓰고 ref-1396 를 넘기지 않는다. 기존 출처는 참고문헌 목록의 id 를 그대로 쓴다

## 입력

### runs/2026-10-09-19/target.json

```json
{
  "run_id": "2026-10-09-19",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 152,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 43,
    "area_name": "43. 데이터·관측성·배포",
    "category": "K. 플랫폼 아키텍처·인프라",
    "category_letter": "K"
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
  "selection_rationale": "CLI 지정 run_type=update, area=43"
}
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md

```markdown
---
title: "43. 데이터·관측성·배포"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [관측성, OpenTelemetry, MCAP, 무선 업데이트, FinOps]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-762, ref-1032, ref-1033, ref-1034, ref-1035, ref-1036, ref-1037, ref-1038, ref-1039, ref-1040, ref-766, ref-1041, ref-1042, ref-943, ref-1043, ref-1044]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 43. 데이터·관측성·배포

# 43. 데이터·관측성·배포

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]

## 3. 왜 중요한가

공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1032][^ref-1033][^ref-943][^ref-1043][^ref-766]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 왜 중요한가](../../topics/2026/2026-09-30-area43-s3.md)에 있다.

## 4. 핵심 개념과 용어

용어는 기록·관찰·배포·비용 순서로 둔다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 적용 사례는 병원의 운영 기록 기반 실패 분석과 물류창고의 배포 전 시뮬레이션 검증(벤더 주장) 두 건이다.

**현장 유형:** 병원

**사례:** 병원에서 약품 배송 로봇의 실패 원인을 로봇·승강기 기록으로 분석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 응급실 직원이 웹 애플리케이션으로 요청하면 배송 임무가 시작됐다. [사실][^ref-943] |
| 작업 대상 | 로봇이 옮겨 넘기는 약품. [사실][^ref-943] |
| 수행 자원 | 미확인(이번 조사에서 확인하지 못함) |
| 제약 | 미확인(이번 조사에서 확인하지 못함) |
| 완료·인계 | 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계하는 것을 배송 성공으로 정의했다. [사실][^ref-943] |
| 예외·성과 | 로봇 시스템 로그(1 Hz)·승강기 통신 로그·관찰자 기록지를 함께 모아 실패 원인을 분석했고, 승강기 가동률이 높을수록 실패가 많았다(저자 보고: 전체 성공률 87.03%, 실패 14건). [사실][^ref-943] |

고려대학교 구로병원은 2025-06-18~29 비응급 배송 임무 122건으로 자율 약품 배송 로봇을 실증했다(2026-03-31 발표). [사실][^ref-943] 로봇 시스템 로그는 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남겼고, 승강기 통신 로그는 승강기 상태·문·위치·로봇 명령을, 관찰자 기록지는 탑승객·화물·결과를 담았다. [사실][^ref-943]

저자 보고에 따르면 [승강기 가동률](../../glossary/elevator-operating-rate.md)(Elevator Operating Rate, EOR) 59% 미만일 때 성공률은 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었다. [사실][^ref-943] 서로 다른 주체가 낸 기록을 함께 모으는 수집·결합이 이 사례에서 이 영역이 맡는 부분으로 보인다. [추정][^ref-943] 성공률과 실패 건수의 분모가 원문 수치 사이에서 맞지 않는 부분은 11. 열린 질문에 올렸다.

**현장 유형:** 물류창고

**사례:** 물류창고에서 로봇 교통 관리·오케스트레이션 알고리즘 변경을 적용 전에 시뮬레이션으로 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(이번 조사에서 확인하지 못함) |
| 작업 대상 | 미확인(이번 조사에서 확인하지 못함) |
| 수행 자원 | 미확인(이번 조사에서 확인하지 못함) |
| 제약 | 미확인(이번 조사에서 확인하지 못함) |
| 완료·인계 | 미확인(이번 조사에서 확인하지 못함) |
| 예외·성과 | 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. [추정] 벤더 주장[^ref-1044] |

Ocado 는 초당 10회 로봇 통신 같은 실제 운영 데이터로 시뮬레이션 모델을 다듬는다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 배포 전 검증의 근거로만 쓰며, 시뮬레이션 자체는 [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)(가정한 미래를 실험)의 내용이다.

제조 공장·상업 시설·가정·실외 현장의 데이터·관측성·배포 사례는 이번 조사에서 찾지 못했다. 다중 로봇 컨테이너 오케스트레이션 연구와 서비스 로봇 언어 모델 계획 연구는 실험실·평가 실험이므로 적용 사례로 쓰지 않고 6. 대표 접근법과 기술에서 다룬다.

## 6. 대표 접근법과 기술

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1034][^ref-762][^ref-1032][^ref-1033][^ref-1036][^ref-1038][^ref-1039][^ref-1040][^ref-1037][^ref-1041][^ref-1042]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 모든 행은 2026-09-30 확인 기준이다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.

- Bédard·Lütkebohle·Dagenais, ros2_tracing(IEEE RA-L, 2022-07) — LTTng 기반 ROS 2 계측·추적 도구 모음으로, 로봇 내부 실행을 낮은 부담으로 기록하는 근거다. [사실][^ref-1032]
- Yu·Lee·Choi·Park, ros2probe(arXiv 프리프린트, 2026-06) — 관찰 도구가 대상을 교란하는 문제를 커널 선택 관찰로 줄인 연구로, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033]
- Zhang·Yu·Westerlund, Kubernetes 를 이용한 ROS 2 다중 로봇 시스템 복원력 연구(Sensors, 2025-08-14) — 컨테이너 자동 재시작으로 장애 중에도 위치 정확도를 유지한 실험실 결과다. [사실][^ref-1039]
- Bruno·Sim·Hagiwara, 서비스 로봇의 LLM 연쇄 기반 작업 계획(arXiv 프리프린트, 2026-09) — 클라우드 API 비용·지연을 동기로 로컬·클라우드 모델을 비교했다. [사실][^ref-1043]
- Lee 외, 혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증(Digital Health, 2026-03-31) — 로봇·승강기 로그와 관찰 기록을 함께 모아 실패를 분석한 국내 현장 자료다. [사실][^ref-943]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

공개 자료를 종합하면 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책, 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스, 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증, 클라우드·언어 모델 호출 비용의 계측·배분으로 보인다. [추정][^ref-1036][^ref-766][^ref-1034][^ref-1038][^ref-943][^ref-1039][^ref-1044][^ref-1037][^ref-1042] 이 가운데 보존 정책의 국내 근거는 2023-09-22 시행 판 고시 기준(현행 조문 미확인)이고, 배포 전 검증의 사례 근거는 벤더 주장이다. [추정][^ref-766][^ref-1044]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 기록·업데이트 상태를 받아 작업 단위로 모으고 색인하는 인터페이스 [추정][^ref-1032][^ref-1040] | 연계 대상: 로봇 운영체제·펌웨어 무선 업데이트, 로봇 내부 ROS 2 실행 추적 [추정][^ref-1032][^ref-1040] |
| 시설·설비 제어 | 승강기 통신 로그를 로봇 기록과 함께 받아 결합 [추정][^ref-943] | 연계 대상: 승강기 통신 로그 생성과 설비 제어 [추정][^ref-943] |

클라우드 청구 데이터를 만드는 일은 클라우드 사업자의 몫이며, ROP 는 그 데이터를 받아 모으는 쪽을 맡을 것으로 보인다. [추정][^ref-1042] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 열린 질문](../../topics/2026/2026-09-30-area43-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md) — 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,055자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md) — 자동 분리: 43. 데이터·관측성·배포 의 "4. 핵심 개념과 용어" 절(975자)을 옮겼다 (실행 2026-09-30-06)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1038]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
```

### docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md (요약)

```markdown
# 41. 플랫폼 아키텍처·외부 API

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **클라우드·현장 서버·로봇 역할 분담**: 어떤 판단과 데이터를 클라우드·현장 서버·로봇 가운데 어디에 둘지 정한다
- **플랫폼 기준 아키텍처**: 서비스 분리, 이벤트 구조, 제조사 중립성을 갖춘 플랫폼 구조를 정한다
- **외부 API·SDK 제공**: 다른 시스템과 개발자가 플랫폼을 부를 수 있는 API·웹훅·SDK·문서를 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’에서 왔다. 그 본문은 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]
```

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md (요약)

```markdown
# 42. 분산 시스템·통신·컴퓨팅 구조

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 네트워크**: 와이파이 로밍·5G·사설망, 지연·대역폭·음영 구역을 설계하고 점검한다
- **연결이 끊겨도 계속 운영**: 인터넷이나 서버가 끊겨도 현장에서 어디까지 계속 운영할지 정하고 구현한다
- **다현장 운영 구조**: 여러 현장을 한 플랫폼에서 나누어 운영하는 구조를 만든다
- **확장성·성능**: 로봇과 작업 수가 늘어도 처리 성능을 유지한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 [옛 분류원문]

> 옛 질문: 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [옛 분류원문]

## 2. 핵심 질문

인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
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

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (요약)

```markdown
# 37. 관제 화면·실행 기록

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
```

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
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

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md (요약)

```markdown
# 52. 통신 보호·위협 관리·감사

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **통신 보호**: 로봇·플랫폼·설비 사이 통신을 암호화하고 무결성을 지킨다(ROS 2 보안 등)
- **보안 위협 모델·취약점 관리**: 위협 모델을 세우고 취약점을 찾아 고친다(ROS 2 위협 모델, IEC 62443 등)
- **문서·대화 입력 보안**: 문서나 대화에 숨은 지시를 명령으로 실행하지 않게 막는다(프롬프트 주입 방지)
- **명령·승인 감사 기록**: 누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]
```

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
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

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1324건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 2026-09-25 | 예 |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 미확인 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 2026-09-25 | 아니오 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 2026-09-29 | 예 |
| ref-1032 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | https://arxiv.org/abs/2201.00393 | 2026-09-30 | 예 |
| ref-1033 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | https://arxiv.org/abs/2606.10746 | 2026-09-30 | 예 |
| ref-1034 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 2026-09-30 | 예 |
| ref-1035 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 2026-09-30 | 예 |
| ref-1036 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | https://opentelemetry.io/docs/specs/status/ | 2026-09-30 | 예 |
| ref-1037 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 2026-09-30 | 예 |
| ref-1038 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | https://github.com/szobov/ros-opentelemetry | 2026-09-30 | 예 |
| ref-1039 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 2026-09-30 | 예 |
| ref-1040 | Northern.tech (mendersoftware) | mender — README | 미확인 | https://github.com/mendersoftware/mender | 2026-09-30 | 예 |
| ref-1041 | FinOps Foundation | FinOps Phases | 미확인 | https://www.finops.org/framework/phases/ | 2026-09-30 | 예 |
| ref-1042 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 2025-06-03 | https://www.finops.org/insights/focus-1-2-available/ | 2026-09-30 | 예 |
| ref-1043 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | https://arxiv.org/abs/2609.29043 | 2026-09-30 | 예 |
| ref-1044 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies and innovation at scale | 2025-06-04 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 379개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
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
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
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
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
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
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
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
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
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
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
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
- management-of-change: 변경 관리 (Management of Change (MOC))
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
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
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
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
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
- remote-attestation: 원격 증명 (Remote Attestation)
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
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
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
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
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
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
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
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [43] 에 걸린 9건 / 전체 335건)

```markdown
- oq-210 [열림] 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? (영역 43, 38)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-212 [열림] 개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? (영역 43, 13)
- oq-213 [열림] 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? (영역 43, 57)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-215 [열림] 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? (영역 43, 63)
- oq-297 [열림] VDA 5050 의 지도 배포(downloadMap·enableMap·deleteMap)로 로봇마다 활성화된 지도 판과 Open-RMF 빌딩 맵·LIF 레이아웃의 판을 ROP 한 곳에서 대응시켜 관리하는 공개 구현이나 운영 절차가 있는가? (영역 16, 43, 57)
- oq-300 [열림] 플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가? (영역 43, 41, 32)
- oq-316 [열림] 로봇 플랫폼의 AI 구성요소가 EU AI Act 고위험 AI 로 분류되면 제12조 자동 사건 기록 요건을 플랫폼 실행 기록이 충족해야 하는가, 그 기록의 보관 주체는 플랫폼 사업자와 배포자 가운데 누구인가? (영역 47, 37, 43)
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

### runs/2026-10-09-18/research.md

```markdown
# 리서치 브리프 2026-10-09-18

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-18 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 42. 분산 시스템·통신·컴퓨팅 구조 |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 개정 전에 쓴 물류창고 시나리오 1건뿐이고 병원·상업 시설·제조 공장·실외·기타 현장 사례 없음(이번 재실행에서도 조사하지 못함)
- 섹션 5. 적용 사례 — 'VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인' 문장의 재확인 필요
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 의 연결(connection) 토픽 의미, 상태 보고 최소·최대 간격, 절전(HIBERNATING) 모드, 구역 허가 만료, 지도 사전 적재 같은 끊김 대비 장치가 정리되지 않음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 관제 쪽 통신 오류 탐지·시간 초과 처리 책임과 표준 범위 밖(외부 IT 인터페이스·사이버보안·운영 책임)의 근거가 약함
- 섹션 11. 열린 질문 — oq-038·oq-039·oq-206 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
2. oq-038·oq-206 로봇–관제 표준은 로봇과 관제·브로커의 연결이 끊긴 동안 로봇이 어디까지 계속 움직이고, 관제는 무엇을 실행된 것으로 간주해야 한다고 정하는가? (섹션 5·9·11 겨냥)
3. VDA 5050 3.0.0 은 연결 끊김을 어떻게 탐지·표시하고(연결 토픽, 유언 메시지, 절전 모드), 재연결 뒤 상태를 다시 세우는 수단을 무엇으로 두는가? (섹션 5·7 겨냥)
4. oq-039 VDA 5050 3.0.0 은 명령·상태 메시지의 전달 보장 수준과 보고 간격을 어떻게 정하며, 허용 지연·손실률 수치를 정하는가? (섹션 7·11 겨냥)
5. 클라우드 브로커와 현장 브로커 배치, 지도·구역 배포 방식은 외부망 단절 중 운영 범위에 어떤 영향을 주는가? (섹션 6·9 겨냥)
6. 로봇–관제 표준이 범위 밖에 두는 것(외부 IT 인터페이스, 사이버보안, 운영 책임 배분)은 무엇이고, ROP 의 직접 범위와 연계 대상은 어떻게 갈리는가? (섹션 9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 로봇–관제 통신이 무선망으로 이루어지며 연결 실패와 메시지 손실이 생길 수 있음을 전제로 하고, MQTT 를 JSON 형식과 함께 쓰며 MQTT 3.1.1 을 호환을 위한 최소 버전으로 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 통신 부담을 줄이기 위해 order·instantActions·state·factsheet·zoneSet·responses·visualization 토픽에 MQTT QoS 0(최선 노력)을, connection 토픽에 QoS 1(최소 한 번)을 쓰게 하고, 프로토콜 보안은 브로커 설정으로 다루되 이 지침에서는 정하지 않는다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행하며, 관제는 MQTT 가 비동기이고 무선 전송을 믿을 수 없으므로 이미 해제한 베이스(base)를 바꿀 수 없고 실행된 것으로 간주해야 하며 주문 취소(cancelOrder)도 같은 이유로 신뢰할 수 없는 것으로 본다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 3.0.0 의 connection 토픽은 브로커–클라이언트 사이 하트비트로 끊김을 탐지해 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리는 MQTT 프로토콜 수준의 연결 확인용이며, 모든 메시지를 retained 플래그로 보내고, 관제가 로봇의 건강 상태 확인에 쓰지 않도록 정한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f5 | [사실] | VDA 5050 3.0.0 에서 로봇 상태 메시지는 정해진 사건(주문 수신, 오류·운용 모드·노드 상태 변화 등)이 생길 때와 적어도 30초마다 보내고, 연속 상태 메시지 사이의 최소 간격은 로봇이 팩트시트의 protocolLimits.timing.minimumStateInterval 로 알리며, 관련 사건은 하나의 상태 갱신으로 묶어 통신량을 줄이도록 권한다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f6 | [사실] | VDA 5050 3.0.0 의 startHibernation 즉시 동작은 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 연결 상태를 HIBERNATING 으로 알리며 활성 주문을 지우고 움직이지 않게 하고, 배터리가 위급하거나 설정한 기상 시각(wakeUpTime)이 되면 로봇이 스스로 이 상태를 벗어날 수 있게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 의 RELEASE 구역은 관제의 허가를 받아야 들어갈 수 있고, 로봇은 응답을 제때 받지 못하면 들어가지 않으며, 관제는 허가에 만료 시각(leaseExpiry)을 붙일 수 있고, 이미 구역 안에서 허가가 만료·철회되면 로봇은 구역 정의의 releaseLossBehavior(STOP·CONTINUE·EVACUATE)에 따라 움직인다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f8 | [사실] | VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 토픽 구조가 있어 클라우드 기반 MQTT 브로커에서는 토픽 단계 구조를 개별 조정하게 허용하고, 로컬 브로커에는 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조를 제안하되 토픽 이름은 필수로 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f9 | [사실] | VDA 5050 3.0.0 에서 지도는 관제가 즉시 동작(downloadMap)으로 지시하면 로봇이 지도 서버에서 끌어오는(pull) 방식으로 배포되고, 정지 시간을 줄이려 지도를 미리 적재해 두었다가 enableMap 으로 따로 활성화하며, 다운로드가 실패·중단되면 동작 상태를 RETRIABLE 로 두고 관제 개입을 기다린다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f10 | [사실] | VDA 5050 3.0.0 은 플릿 관제의 최소 기능에 문·게이트·승강기 같은 주변 시스템과의 통신과 통신 오류의 탐지·해소를 넣고, 로봇의 기능으로 위치 추정·경로 실행·동작 실행·상태 연속 전송을 두어 통신 오류 대응을 관제 쪽 책임으로 배치한다. | ref-031 | 아니오 | medium | 2026-10-09 | 수행 자원 | — |
| f11 | [사실] | VDA 5050 3.0.0 은 주변 설비·기반 시설·외부 IT 시스템과의 인터페이스, 운영자·통합사·제조사·관제 공급자 사이의 운영 책임 배분, 보안 통신·데이터 보호의 사이버보안 조치를 범위 밖에 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [사실] | VDA 5050 3.0.0 의 waitForTrigger 동작에서 시간 초과 처리는 관제의 책임이며 필요하면 관제가 주문을 취소해야 하고, 로봇은 stateRequest 즉시 동작을 받으면 새 상태 메시지를 보낸다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f13 | [추정] | 이번에 읽은 VDA 5050 3.0.0 명세 앞부분은 MQTT 3.1.1 을 최소 버전으로 두고 연결 확인을 유언 메시지와 하트비트로만 서술하며 MQTT 5.0 의 세션 만료 같은 기능을 쓰는 방법은 다루지 않아, 페이지 5절의 해당 '미확인' 서술은 그대로 남는 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f14 | [추정] | VDA 5050 3.0.0 에서 주문·상태가 QoS 0 이고 connection 메시지가 retained 로 보내지며 stateRequest 즉시 동작이 있으므로, 재연결 뒤 관제는 connection 토픽의 ONLINE 전환을 받은 다음 stateRequest 나 다음 상태 메시지로 로봇 상태를 다시 세우고 끊긴 동안 해제된 베이스는 실행된 것으로 놓고 주문을 갱신하는 절차를 둘 수 있을 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f15 | [추정] | VDA 5050 3.0.0 은 상태 보고의 최대 간격(30초)과 팩트시트의 최소 간격만 두고 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간 수치를 정하지 않으므로, oq-039 는 이 표준만으로 답이 되지 않는 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | 제약 | — |
| f16 | [사실] | KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. | ref-300 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f17 | [추정] | VDA 5050 은 클라우드 브로커 사용을 허용하지만(f8) 브로커와 끊긴 로봇은 해제된 노드까지만 진행하므로(f3), 관제와 브로커를 클라우드에 두면 외부망 단절이 곧 로봇–관제 단절이 되어 해제 구간 뒤에서 로봇이 멈추고, 현장 서버에 두면 엣지 자율 운영 구조(f16)처럼 현장 내 배정을 이어 갈 수 있어, 관제·브로커의 배치가 단절 중 운영 범위를 정하는 핵심 결정인 것으로 보인다(oq-038·oq-206 부분 근거, 41. 플랫폼 아키텍처·외부 API 와 연결). | ref-031, ref-300 | 아니오 | low | 2026-10-09 | 제약 | — |
| f18 | [추정] | VDA 5050 의 구역 허가 만료(leaseExpiry)와 releaseLossBehavior 는 관제가 허가를 갱신하지 못하는 상황, 곧 관제 장애나 통신 단절 때 공용 구역 점유를 시간으로 제한하는 장치로 쓸 수 있을 것으로 보이나, 명세는 이를 통신 단절 대책으로 명시하지 않는다. | ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/kubeedge/kubeedge | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md | 5, 7, 9, 11 | 갱신(차등): 섹션 5 — 물류창고 시나리오의 제약·예외 행을 오늘 원문으로 재확인(f1·f3·f5), 연결 탐지·재연결 서술 보강(f4·f12·f14), MQTT 5.0 세션 만료 '미확인' 유지 근거(f13) / 섹션 7(주제 페이지로 분리된 절의 요약) — VDA 5050 의 QoS·보안 위임(f2), 연결 토픽 의미(f4), 상태 보고 간격(f5), 절전 모드(f6), 구역 허가 만료(f7), 클라우드 브로커 토픽 조정(f8), 지도 사전 적재(f9), KubeEdge 엣지 자율성 재확인(f16) / 섹션 9 — 통신 오류 탐지·해소와 시간 초과 처리를 관제(ROP) 쪽 책임으로(f10·f12), 외부 IT 인터페이스·사이버보안·운영 책임은 표준 범위 밖(f11) / 섹션 11 — oq-038·oq-206 부분 근거 f17, oq-039 미해결 근거 f15, 새 질문 1건(f18). 다음 실행 후보: 52. 통신 보호·위협 관리·감사(f2·f11), 27. 다중 로봇 경로·교통 관리 — MAPF(f7·f18). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 절전 모드 | Hibernation (VDA 5050 startHibernation / HIBERNATING) | VDA 5050 에서 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 주문을 지운 채 정지해 있다가 stopHibernation 이나 설정한 기상 시각에 정상 운용으로 돌아오는 통신 감축 상태다. |
| 보존 메시지 | MQTT Retained Message | 브로커가 토픽의 마지막 메시지를 보관했다가 나중에 구독한 클라이언트에게 곧바로 전달하게 하는 MQTT 발행 옵션으로, VDA 5050 은 연결 상태 메시지에 이를 쓰게 한다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 구역 허가 만료 시각(leaseExpiry)과 허가 상실 시 동작(releaseLossBehavior)을 관제 장애·통신 단절 대책으로 쓸 때 만료 시간과 동작 값을 어떤 기준으로 정하는지 공개한 현장 사례나 지침이 있는가? | 관련 영역: 42. 분산 시스템·통신·컴퓨팅 구조, 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f18 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 2 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - oq-038·oq-206 미해결: 외부망 단절 중 운영 범위를 정한 공개 운영 기준·사례 미확인(f17 은 추론)
    - oq-039 미해결: 허용 지연·손실률·로밍 중단 시간 수치를 정한 표준·측정 자료 미확인(f15)
    - oq-035·oq-040·oq-083·oq-310·oq-326 이번 재실행에서 미조사
    - ref-031 원문 텍스트가 앞 119,109자 발췌라 7장 메시지 명세 뒷부분(팩트시트 protocolLimits 세부 등) 미확인
    - ref-031 VDA 5050 3.0.0 발행일 미확인
    - ref-300 은 이번 실행에서 원문을 다시 열지 않음
    - 섹션 5 병원·상업 시설·제조 공장·실외·기타 현장 사례 미조사
- 범위 경계 위반 의심:
    - f3·f10: 위치 추정·경로 실행과 끊김 중 로봇 주행은 로봇 자체 지능·제어 쪽 연계 대상이며, ROP 몫은 해제 구간 설정·통신 오류 탐지·상태 재구성으로 한정해 서술해야 함
    - f2·f11: 브로커 보안·사이버보안 조치는 52. 통신 보호·위협 관리·감사 쪽이므로 이 영역에서는 '표준 범위 밖'이라는 사실만 씀
    - f16·f17: 엣지 플랫폼·클라우드 인프라 자체는 외부 연계 대상이며 배치 결정은 41. 플랫폼 아키텍처·외부 API 와 함께 다뤄야 함
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f13 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts/ref-031.txt, fetched_via inbox)와 기존 페이지가 인용한 참고문헌(ref-300 재인용)만으로 브리프를 다시 구성했다. 새 f13 은 표준(ref-031)만 근거로 한 [추정]이다. 벤더 문서(CJ대한통운 ref-307, FreightWaves 기사 ref-309 등)를 근거로 한 finding 은 이번 브리프에 하나도 없으므로 vendor_claim 이 필요한 finding 이 없다. 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1337~ref-1366 은 쓰지 않았다. 재사용 2건 중 ref-031 은 원문을 열었고(inbox), ref-300 은 원문 미열람으로 표시했다. 교차 확인 0건이며 모든 사실 finding 은 단일 출처라 신뢰도 medium 이하다. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·7·9·11절)만 다뤘다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-038·oq-206 은 f17, oq-039 는 f15. 현장 유형 사례 finding 은 없다(site_type 모두 null). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 MQTT·MQTT 유언 메시지·허가 만료 시각·CAP 정리·포그 컴퓨팅·5G 특화망은 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-10-09-17/research.md

```markdown
# 리서치 브리프 2026-10-09-17

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-17 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 41. 플랫폼 아키텍처·외부 API |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 6. 대표 접근법과 기술 — 연결이 끊겼을 때 로봇·관제가 어떻게 동작하는지, 메시지 전달 보장 수준(재전송·순서·중복)의 근거가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 의 버전 표기 규칙과 MQTT QoS 수준, Open-RMF 플릿 어댑터 API 의 폐기 예고, rmf-web API 서버의 기계 간(M2M) 인증 설정·권한 그룹 미구현(바뀐 출처) 서술 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) — 외부 API 전달 보장과 고객·현장별 권한 격리를 누가 맡는지 근거가 약함
- 섹션 11. 열린 질문 — oq-206·oq-207·oq-208·oq-300 의 부분 근거 미반영, oq-209·oq-267·oq-301 미조사
- 섹션 5. 적용 사례 (현장 유형 명시) — 상업 시설·가정·실외 사례 없음(이번 재실행에서도 조사하지 못함)
- 정정 요청 없음

## 조사 질문

1. 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]
2. oq-207 로봇 관제 플랫폼·상호운용 규격은 API 버전 관리와 하위 호환, 폐기 예고를 어떻게 공개하는가? (섹션 7·11 겨냥)
3. oq-208 로봇–관제 인터페이스와 플랫폼 외부 이벤트의 전달 보장(재시도·순서·중복 제거)은 어디까지 정해져 있는가? (섹션 6·9·11 겨냥)
4. oq-206·oq-300 연결이 끊기거나 중앙 서비스가 재시작될 때 로봇과 진행 중 작업은 어디까지 계속되는가? (섹션 6·11 겨냥)
5. 바뀐 출처: Open-RMF rmf-web API 서버의 인증·권한 서술은 지난 확인(2026-09-30) 이후 무엇이 바뀌었고, 외부 API 의 인증·격리 범위에 무엇을 뜻하는가? (섹션 7·9 겨냥)
6. oq-209·oq-301 국내 클라우드 로봇·통합관제 참조 구조 표준과 OpenAPI·AsyncAPI 기반 적합성 시험 도구가 있는가? (섹션 7·11 겨냥, 이번 재실행에서는 조사하지 못함)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 의미적 버전 관리를 써서 주 버전(x.0.0)은 새 필수 필드 도입 같은 하위 호환을 깨는 변경, 부 버전(3.x.0)은 선택 매개변수 추가 같은 새 기능, 수 버전(3.0.x)은 문서 오탈자 같은 작은 수정에 쓰고, MQTT 주제 경로에 'v' 를 붙인 주 버전(예 v3)을 넣게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 은 무선망의 연결 끊김과 메시지 손실을 전제로 order·instantActions·state·factsheet·zoneSet·responses·visualization 주제에 MQTT QoS 0(최선 노력)을, connection 주제에 QoS 1(최소 한 번)을 쓰게 하고, 로봇이 예기치 않게 끊기면 브로커가 유언(last will) 메시지로 다른 구독자에게 알리게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제(released)된 노드까지 주문을 수행하며, 관제는 MQTT 가 비동기이고 무선 전송을 믿을 수 없으므로 이미 해제한 base 구간을 바꿀 수 없고 실행된 것으로 간주해야 하며 주문 취소(cancelOrder)도 같은 이유로 신뢰할 수 없는 것으로 본다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 의 주문 갱신은 같은 orderId 에 orderUpdateId 를 늘려 보내며, 로봇은 같은 orderUpdateId 로 같은 내용이 다시 오면 무시하고 내용이 다르면 SAME_ORDER_UPDATE_ID, 더 낮은 orderUpdateId 면 OUTDATED_ORDER_UPDATE 경고를 보고해 재전송과 순서 뒤바뀜을 메시지 수준에서 걸러낸다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 주제 구조가 있으므로 MQTT 주제 단계 구조를 엄격히 정하지 않고 클라우드 브로커에서는 구조를 개별 조정하게 허용하되, 주제 이름(order·state 등)은 필수로 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 은 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스, 안전 요구사항, 교통 관리 로직, 운영자·통합사·제조사·관제 공급자 사이 운영 책임 배분, 사이버보안 조치를 범위 밖에 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 플릿 관제의 최소 기능으로 주문 배정, 경로 계산, 교착 탐지·해소, 에너지 관리, 교통 통제, 문·게이트·승강기 같은 주변 시스템과의 통신, 통신 오류 탐지·해소를 들고, 로봇의 기능으로 위치 추정·경로 실행·동작 실행·상태 연속 전송을 들어 판단 배치를 관제와 로봇으로 나눈다. | ref-031 | 아니오 | medium | 2026-10-09 | 수행 자원 | — |
| f8 | [추정] | 로봇–관제 인터페이스인 VDA 5050 은 버전 표기와 주문 갱신 번호로 재전송·순서 문제를 다루지만 대부분 주제에 QoS 0 최선 노력 전달을 쓰고 외부 IT 시스템 인터페이스를 범위 밖에 두므로, 41. 플랫폼 아키텍처·외부 API 에서 업무 시스템에 내보내는 웹훅·이벤트의 전달 보장(재시도·순서·중복 제거)은 ROP 의 외부 API 가 따로 정해야 하는 것으로 보인다(oq-208 부분 근거). | ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [사실] | Open-RMF 핵심 문서는 플릿 어댑터를 Full Control·Traffic Light·Read Only·No Interface 네 제어 수준으로 나누고, Full Control 에는 재사용 C++ API(파이썬 바인딩 포함)를 제공하며, Read Only 용 예비 ROS 2 메시지 API 는 향후 판에서 C++ API 로 대체되어 폐기될 예정이고 Traffic Light 용 재사용 API 는 아직 구현되지 않았다고 적는다. | ref-004 | 아니오 | medium | 2026-10-09 | — | — |
| f10 | [사실] | Open-RMF 의 교통 일정은 플랫폼 중립의 중앙 데이터베이스로, 배치된 모든 플릿 관리자가 예상 경로를 보고하고, 충돌이 예상되면 플릿 관리자들이 협상하며 시스템 통합사가 둔 제3자 판정자가 제안을 고르고, 긴급 작업은 의도적으로 충돌을 올려 협상을 강제할 수 있다. | ref-004 | 아니오 | medium | 2026-10-09 | — | — |
| f11 | [사실] | Open-RMF rmf-web API 서버는 사용자 신원을 스스로 관리하지 않고 OpenID Connect 신원 제공자가 발급한 JWT 접근 토큰을 독립 검증하며, OAuth 2.0 client_credentials(기계 간, M2M) 흐름에서 신원 제공자가 표준 클레임을 빼고 네임스페이스 붙은 클레임만 주는 경우를 위해 선택 설정 preferred_username_claim_namespace 를 둔다. | ref-762 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [사실] | rmf-web API 서버는 역할·동작·권한 그룹의 세 값으로 접근을 판정하지만, 자원의 권한 그룹을 정하는 방식이 아직 TODO 로 남아 있어 현재는 모든 자원이 기본 빈 그룹('')에 들어간다. | ref-762 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f13 | [사실] | rmf-web API 서버는 자체 사용자·역할·권한 DB 를 신원 제공자와 동기화하지 않으므로, rmf-server 에서 사용자를 지워도 로그인만 요구하는 반보호 API 접근은 막지 못하고 로그인 자체를 막으려면 신원 제공자에서 사용자를 지워야 한다. | ref-762 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | rmf-web API 서버는 최신 API 정의를 공개 문서 사이트와 실행 중인 서버의 /docs 경로에서 보여 주고, 역방향 프록시 뒤에서 쓸 때는 public_url 을 공개 주소로 설정하고 프록시가 경로 접두어를 제거하게 해야 한다. | ref-762 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [추정] | rmf-web API 서버의 권한 그룹 결정이 미구현이고(f12) 사용자 해지가 신원 제공자에 달려 있으므로(f13), Open-RMF 웹 API 를 ROP 외부 API 의 기반으로 쓰면 고객·현장별 자원 격리와 외부 계정 해지는 ROP 가 신원 제공자 연동과 권한 그룹 규칙으로 직접 채워야 할 것으로 보이며, 이는 51. 인증·권한·격리와 맞닿는다. | ref-762 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [추정] | FogROS2-FT 의 다중 클라우드 복제는 상태 없는(stateless) 로봇 서비스를 대상으로 하므로, 진행 중 작업 상태를 가진 관제 서비스가 재시작한 뒤 작업을 이어 가는 문제(oq-300)는 이 방법만으로 답이 되지 않는 것으로 보인다. | ref-1031 | 아니오 | low | 2024-12 | — | 원문 미열람 |
| f17 | [추정] | 이번에 읽은 VDA 5050 3.0.0 명세 범위와 Open-RMF 핵심 문서는 버전 표기 규칙과 '향후 판에서 폐기' 같은 예고 문구는 담지만 폐기 예고 기간이나 구판 지원 기간을 정하지 않아, 로봇 관제 플랫폼 외부 API 의 폐기 정책(oq-207)은 아직 근거가 부족한 것으로 보인다. | ref-031, ref-004 | 아니오 | low | 2026-10-09 | — | — |
| f18 | [추정] | VDA 5050 은 연결이 끊긴 로봇이 해제된 구간까지만 계속 수행하게 하고(f3) Open-RMF 는 교통 일정과 협상을 중앙 데이터베이스에 두므로(f10), 41. 플랫폼 아키텍처·외부 API 의 판단 배치 정책은 중앙 조율 서비스를 클라우드와 현장 서버 가운데 어디에 둘지와 함께 끊김 동안 로봇이 계속 갈 수 있는 해제 구간의 길이를 정해야 할 것으로 보인다(oq-206 부분 근거, 42. 분산 시스템·통신·컴퓨팅 구조와 연결). | ref-031, ref-004 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-1031 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 2024-12 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2412.05408 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md | 6, 7, 9, 11 | 갱신(차등): 섹션 6 — 끊김 동안 해제 구간까지 계속 수행(f3)과 중앙 교통 일정·협상(f10)을 판단 배치 근거로, QoS 수준(f2)·주문 갱신 번호(f4)·클라우드 브로커 주제 조정(f5)·관제/로봇 기능 분담(f7) 추가 / 섹션 7 — VDA 5050 행에 버전 규칙(f1)·QoS(f2)·범위 제외(f6), Open-RMF 행에 어댑터 API 폐기 예고(f9), rmf-web 행에 M2M 인증 설정(f11)·권한 그룹 미구현(f12)·사용자 비동기화(f13)·/docs 와 프록시 설정(f14) 반영(바뀐 출처) / 섹션 9 — 외부 이벤트 전달 보장(f8)과 고객·현장별 격리(f15)를 ROP 직접 범위로, 외부 IT 인터페이스·보안이 로봇–관제 표준 밖임(f6) / 섹션 11 — oq-206 부분 근거 f18, oq-207 부분 근거 f1·f9·f17(미해결), oq-208 부분 근거 f2·f4·f8(미해결), oq-300 부분 근거 f16, 새 질문 1건. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조(f2·f3·f18), 51. 인증·권한·격리(f11~f13·f15), 29. 명령·작업 실행의 신뢰성(f4·f8). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| MQTT 서비스 품질 수준 | MQTT Quality of Service (QoS) Level | MQTT 에서 메시지 전달 보장을 최선 노력(QoS 0)·최소 한 번(QoS 1)·정확히 한 번(QoS 2)의 세 수준으로 고르게 하는 설정이다. |
| 클라이언트 자격 증명 흐름 | OAuth 2.0 Client Credentials Grant (Machine-to-Machine) | 사람 사용자 없이 서비스나 기계가 자기 자격 증명으로 접근 토큰을 받아 API 를 부르는 OAuth 2.0 인가 방식이다. |

## 열린 질문

새로 생긴 질문:

- Open-RMF 웹 API 서버처럼 권한 그룹 자동 결정이 미구현인 오픈소스 관제 API 위에서 고객·현장별 자원 격리를 API 수준으로 구현한 공개 사례나 설계 문서가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 51. 인증·권한·격리 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 4 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - oq-209 미조사: 국내 TTA·KS 참조 구조 표준 검색을 하지 않음
    - oq-301 미조사: OpenAPI·AsyncAPI 기반 연동 적합성 시험 도구 검색을 하지 않음
    - oq-267 미조사: 과금 단위 비교 자료
    - 섹션 5 상업 시설·가정·실외 사례 미조사
    - ref-031 VDA 5050 3.0.0 발행일 미확인, 원문 텍스트는 앞 48,820자까지만 읽어 폐기 예고 기간 등 뒷부분 서술 미확인
    - f16 근거 ref-1031 은 이전 실행 확인 내용 재인용이며 원문 미열람
    - rmf-web README 의 M2M 클레임 설정(f11)이 지난 확인(2026-09-30) 이후 새로 들어갔는지는 변경 이력을 보지 않아 미확인
- 범위 경계 위반 의심:
    - f3·f7: 위치 추정·경로 실행 같은 로봇 기능과 끊김 때 로봇 동작은 로봇 자체 지능·제어 쪽 연계 대상이며, ROP 몫은 해제 구간 설정과 관제 기능 배치로 한정해 서술해야 함
    - f6: 사이버보안·안전 요구는 52. 통신 보호·위협 관리·감사와 M. 안전 쪽이므로 이 영역에서는 '표준 범위 밖'이라는 사실만 씀
    - f16: 클라우드 제공자 인프라는 외부 연계 대상이며 상태 연속성 논의는 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포와 함께 다뤄야 함
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: f8·f10·f23·f24 가 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts/ref-004·ref-031·ref-762, fetched_via inbox)와 이전 브리프 2026-09-30-05 의 재인용 1건(ref-1031)만으로 브리프를 다시 구성했다. 벤더 문서(MiR·Locus·InOrbit·NAVER)를 근거로 한 finding 은 이번 브리프에 없고, [사실] finding 은 모두 표준(ref-031) 또는 오픈소스 문서(ref-004·ref-762)만 근거로 한다. 따라서 vendor_claim 이 필요한 finding 이 없다. 검색 0회, 신규 출처 0건으로 예약 구간 ref-1397~ref-1426 은 쓰지 않았다. 재사용 4건 중 3건은 원문을 열었고(inbox), ref-1031 은 원문 미열람으로 표시했다. 교차 확인 0건이며 모든 사실 finding 은 단일 출처라 신뢰도 medium 이하다. 갱신(update) 실행이고 정정 요청이 없어 바뀐 출처(rmf-web API 서버)와 약한 절(6·7·9·11절)만 다뤘다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-206 은 f18, oq-207 은 f1·f9·f17, oq-208 은 f2·f4·f8, oq-300 은 f16. 현장 유형 사례 finding 은 없다(site_type 모두 null). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 MQTT·MQTT 유언 메시지·의미적 버전 관리·멱등성 키·웹훅·플릿 제어 수준은 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-06/research.md

```markdown
# 리서치 브리프 2026-09-30-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-06 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 43. 데이터·관측성·배포 |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 관측성, OpenTelemetry, MCAP, FinOps·FOCUS, A/B 분할 업데이트 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(운영 로그 기반 실패 분석)·물류창고(배포 전 시뮬레이션 검증) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 기록 형식, 추적·지표·로그 수집, 컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 비용 계측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — rosbag2·MCAP, ros2_tracing, OpenTelemetry, Mender, FOCUS 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
2. 로봇·플랫폼의 로그·이벤트·텔레메트리를 기록·저장하는 형식과 도구(rosbag2·MCAP, 플랫폼 기록 DB)는 무엇이며, 보존 기간을 정하는 국내 규제 근거는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
3. 플랫폼 관측성을 구현하는 표준·오픈소스(OpenTelemetry, ros2_tracing, 커널 기반 관찰)는 무엇이며 관찰 자체의 성능 부담은 얼마로 보고되는가? (섹션 6·7·8 겨냥)
4. 현장 서버·로봇·클라우드에 플랫폼 소프트웨어를 배포하고 되돌리는 방법(컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 배포 전 시뮬레이션 검증)은 무엇이며 어떤 결과가 보고되는가? (섹션 6·7·8 겨냥)
5. 클라우드와 언어 모델 호출 비용을 측정·할당·관리하는 기준(FinOps 주기, FOCUS 청구 데이터 명세, OpenTelemetry 생성형 AI 토큰 지표)은 무엇인가? (섹션 4·6·7 겨냥)
6. 병원·물류창고 등 현장에서 운영 데이터를 수집해 실패 원인을 분석하거나 소프트웨어 변경을 배포 전에 검증한 사례는 무엇인가? (섹션 5 겨냥)
7. 데이터·관측성·배포에서 ROP가 직접 맡을 것과 로봇 제조사·클라우드 사업자·법규에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Bédard·Lütkebohle·Dagenais 의 ros2_tracing(IEEE RA-L 7(3), 2022-07)은 저부하 추적기 LTTng 를 써서 ROS 2 의 실행 정보를 수집하는 계측·추적 도구 모음으로, ROS 2 추적 데이터를 운영체제 추적과 결합할 수 있고, ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f2 | [사실] | ros2_tracing 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목에 관한 정보가 충분하지 않다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f3 | [사실] | Yu·Lee·Choi·Park 의 ros2probe(arXiv 2606.10746, 2026-06)는 ROS 2 도메인에 구독자로 참여하는 관찰 도구가 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다고 보고, 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰하는 방식으로 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고, 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 메시지 손실 0을 보고했다. | ref-1039 | 아니오 | medium | 2026-06 | — | — |
| f4 | [사실] | ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식을 sqlite3 에서 MCAP 로 바꿨고, 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능이 더해졌다. | ref-1040, ref-1041 | 예 | high | 2023-05-23 | — | — |
| f5 | [추정] | Foxglove 는 MCAP 이 SQLite3 의 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고, zstd·lz4 압축을 고를 수 있으며, 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 주장한다. | ref-1041 | 아니오 | low | 2022-12-22 | — | 벤더 주장 |
| f6 | [사실] | OpenTelemetry 명세 상태 요약에 따르면 추적(tracing)은 API·SDK·프로토콜이 모두 안정(stable)이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표(metrics)는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일(profiles)은 프로토콜이 개발(development) 단계다. | ref-1042 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenTelemetry 생성형 AI 의미 규약 저장소의 토큰 지표 문서는 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터(gen_ai.client.inference.usage.*)와 호출별 입력·출력 토큰 히스토그램(gen_ai.client.inference.operation.*)을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 두며, 모든 지표가 개발(Development) 단계다. | ref-1043 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | 오픈소스 ros-opentelemetry 는 송신 측이 추적 문맥을 ROS 2 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 이어 붙이는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다. | ref-1044 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Zhang·Yu·Westerlund(Sensors, 2025-08)는 TurtleBot4 에 얹은 Jetson Nano 5대를 작업 노드로, 노트북 1대를 마스터로 둔 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB 상대 위치 추정을 운영했고, 오차 보정용 LSTM 파드 5개를 모두 종료시킨 경우에도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다고 보고했다. | ref-1045 | 아니오 | medium | 2025-08-14 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: 오픈소스 Mender 는 임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선(OTA) 업데이트 관리자로, 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 해 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있게 하며, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다. | ref-1046 | 아니오 | medium | 2026-09-30 | — | — |
| f11 | [사실] | 개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행) 제8조는 개인정보처리자가 개인정보취급자의 개인정보처리시스템 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관·관리하고, 월 1회 이상 점검하며, 위조·변조·도난·분실되지 않도록 안전하게 보관하게 한다. | ref-766 | 아니오 | medium | 2023-09-22 | 제약 | — |
| f12 | [사실] | FinOps 재단의 FinOps 프레임워크는 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보(Inform), 사용량 최적화와 요금 최적화를 찾는 최적화(Optimize), 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영(Operate)의 세 단계를 반복하는 방식으로 설명하며, 대상 기술 범주에 공용 클라우드·SaaS 와 함께 AI 서비스를 든다. | ref-1048 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | FinOps 재단의 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화(PricingCurrency 등), 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다. | ref-1049 | 아니오 | medium | 2025-05-29 | — | — |
| f14 | [사실] | Bruno·Sim·Hagiwara(arXiv 2609.29043, 2026-09)는 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다고 보고, 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높였으며 클라우드 모델(Claude Sonnet 4.6)과 함께 비교했다. | ref-1051 | 아니오 | medium | 2026-09 | 예외·성과 | — |
| f15 | [사실] | 고려대학교 구로병원의 자율 약품 배송 로봇 실증(Lee 외, Digital Health, 2026-03)에서 배송 임무는 응급실 직원이 웹 애플리케이션으로 요청하면 시작됐다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 시작 조건 | — |
| f16 | [사실] | 같은 병원 실증은 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 넘겨 간호사가 받는 것을 배송 성공으로 정의했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 완료·인계 | — |
| f17 | [사실] | 같은 병원 실증은 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자가 적은 수기 기록지(탑승객·화물·결과)를 함께 모아 분석했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 작업 대상 | — |
| f18 | [사실] | 같은 병원 실증에서 전체 배송 성공률은 87.03%, 승강기 가동률 59% 미만일 때 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었으며, 승강기 가동률이 높을수록 실패가 많았다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f19 | [추정] | Ocado 는 물류창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 초당 10회 로봇 통신 같은 실제 운영 데이터로 모델을 다듬으며, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. | ref-1052 | 아니오 | low | 2025-06-04 | 물류창고 / 예외·성과 | 벤더 주장 |
| f20 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다. | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에 대해, 데이터는 자기 기술형 기록 형식(MCAP)과 플랫폼 기록 DB 로 남기고(f4·f20), 상태는 OpenTelemetry 의 추적·지표·로그로 플랫폼 서비스를 관찰하면서 로봇 내부 실행은 저부하 추적·커널 필터로 교란 없이 보며(f1·f3·f6·f8), 배포는 컨테이너 오케스트레이션의 자동 재시작과 이미지 기반 A/B 롤백, 배포 전 시뮬레이션 검증을 조합하고(f9·f10·f19), 비용은 표준 청구 데이터(FOCUS)와 토큰 지표를 FinOps 주기로 관리하는 조합이 공개 자료의 공통 형태로 보인다(f7·f12·f13). | ref-1040, ref-762, ref-1038, ref-1039, ref-1042, ref-1044, ref-1045, ref-1046, ref-1052, ref-1043, ref-1048, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 미들웨어 기록만으로는 내부 병목을 알 수 없고(f2) 관찰 도구 자체가 시스템을 교란할 수 있으며(f3), 병원 실증처럼 실패 원인이 로봇·승강기 로그를 함께 모아야 드러나고(f17·f18), 클라우드 언어 모델 호출 비용이 반복 작업에서 누적되며(f14), 개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 지기 때문이다(f11). | ref-1038, ref-1039, ref-943, ref-1051, ref-766 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 43. 데이터·관측성·배포에서 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책(f6·f11), 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스(f4·f8·f17), 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증(f9·f19), 클라우드·언어 모델 호출 비용의 계측·배분(f7·f13)이다. | ref-1042, ref-766, ref-1040, ref-1044, ref-943, ref-1045, ref-1052, ref-1043, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 운영체제·펌웨어의 무선 업데이트와 로봇 내부 ROS 2 실행 추적(f1·f10)은 로봇 제조사에, 클라우드 청구 데이터 생성(f13)은 클라우드 사업자에, 승강기 통신 로그(f17)는 설비 제어 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 내는 기록·업데이트 상태·청구 데이터를 받아 모으는 인터페이스를 맡을 것으로 보인다. | ref-1038, ref-1046, ref-1049, ref-943 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 실행 기록을 보여 주는 37. 관제 화면·실행 기록(f17·f20), 로그로 원인을 찾는 38. 모니터링·이상 탐지·원인 분석(f2·f18), 성과 지표의 39. 운영 성과 측정·개선(f18), 컨테이너·DDS 통신의 42. 분산 시스템·통신·컴퓨팅 구조(f9), 기록 DB 를 두는 41. 플랫폼 아키텍처·외부 API(f20), 업데이트·버전의 57. 자산·소프트웨어 수명주기 관리(f10), 배포 전 검증의 54. 시험·형식 검증·벤치마크와 34. 시뮬레이션·예측용 디지털 트윈(f19), 접속기록의 53. 개인정보·영상 데이터와 52. 통신 보호·위협 관리·감사(f11), 비용의 3. 경제성·조달·사업 모델(f12·f13), 언어 모델 비용의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영·13. 대화형 기능의 신뢰·기반(f7·f14), 승강기 로그의 22. 설비·건물 시스템 연동(f17), 적용 현장인 63. 병원·의료(f15~f18)·61. 물류창고(f19)와 이어진다. | ref-943, ref-762, ref-1038, ref-1045, ref-1046, ref-1052, ref-766, ref-1048, ref-1049, ref-1043, ref-1051 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1038 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2201.00393 | 아니오 |
| ref-1039 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.10746 | 아니오 |
| ref-1040 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 아니오 |
| ref-1041 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | 벤더 문서 | medium | 2026-09-30 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 아니오 |
| ref-1042 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://opentelemetry.io/docs/specs/status/ | 아니오 |
| ref-1043 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 아니오 |
| ref-1044 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/szobov/ros-opentelemetry | 아니오 |
| ref-1045 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 아니오 |
| ref-1046 | Northern.tech (mendersoftware) | mender — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/mendersoftware/mender | 아니오 |
| ref-766 | 개인정보보호위원회 (국가법령정보센터) | 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호) | 2023-09-22 | 정부·연구기관 | high | 2026-09-30 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 아니오 |
| ref-1048 | FinOps Foundation | FinOps Phases | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.finops.org/framework/phases/ | 아니오 |
| ref-1049 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 미확인 | 표준 | medium | 2026-09-30 | https://www.finops.org/insights/focus-1-2-available/ | 아니오 |
| ref-943 | Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-1051 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.29043 | 아니오 |
| ref-1052 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies | 2025-06-04 | 벤더 문서 | medium | 2026-09-30 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 관측성·실행 추적 f1·f2, MCAP f4·f5(벤더 주장 병기), OpenTelemetry f6, 토큰 지표 f7, A/B 분할 업데이트 f10, FinOps·FOCUS f12·f13 / 섹션 5: 병원 — f15(시작 조건)·f16(완료·인계)·f17(작업 대상: 로봇·승강기 로그 정보)·f18(예외·성과), 물류창고 — f19(배포 전 시뮬레이션 검증, 벤더 주장 병기). 제조 공장·상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 기록 f4·f20, 관찰 f1·f3·f6·f8, 배포 f9·f10·f19, 비용 f7·f12·f13·f14 / 섹션 7: rosbag2·MCAP f4·f5, ros2_tracing f1, ros2probe f3, OpenTelemetry f6·f7, ros-opentelemetry f8, K3s f9, Mender f10, FOCUS f13, 개인정보 고시 f11 / 섹션 8: f1·f3·f9·f14·f15~f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3·f17·f18 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 관측성 | Observability | 시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다. |
| 오픈텔레메트리 | OpenTelemetry (OTel) | 추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다. |
| MCAP | MCAP | 여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다. |
| 핀옵스 | FinOps | 클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 38. 모니터링·이상 탐지·원인 분석 | 근거: f8 | 종류: 일반
- 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반
- OpenTelemetry 생성형 AI 토큰 지표가 개발 단계에서 이름이 바뀌고 있는데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 관련 영역: 43. 데이터·관측성·배포, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리 | 근거: f10 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - f1·f3·f14 는 논문 초록(또는 HTML 일부) 기준이며 본문 실험 조건 미확인
    - f7: 검색 결과 요약의 다른 문서들은 gen_ai.client.token.usage 히스토그램을 설명하지만, 열어 본 현재 저장소는 gen_ai.client.inference.usage.* 로 정의함. 이름 변경 시점과 이전 이름의 폐기 여부 미확인
    - f11 의 '5만 명 이상' 조건 문구는 검색 요약으로 보완했고 법령 페이지 요약에서는 1년/2년 구분만 확인
    - f13 FOCUS 1.2 명세 본문(PDF) 미열람, 발표 글만 열람
    - f8 ros-opentelemetry 라이선스·유지 주체 미확인(개인 관리 저장소)
    - ref-1049·ref-1052 제목 일부는 검색 결과 제목 기준
    - Zampetti 외 CPS CI/CD 인터뷰 연구(ACM TOSEM 2023)는 ACM 403·PDF 본문 추출 실패로 넣지 않음
    - Docker·Kubernetes 기반 ROS 설계 흐름 논문(ACM 10.1145/3594539)은 403 으로 넣지 않음
    - 실외이동로봇 운행안전인증에서 관제·소프트웨어 원격 업데이트 시 변경 인증 필요 여부는 KIRIA 안내 페이지에 없어 확인하지 못함
    - 제조 공장·상업 시설·가정·실외 현장의 데이터·배포 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3: ROS 2 내부 실행 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓰고, 이종 제조사 로봇 내부 추적은 f24 에서 연계 대상으로 구분함
    - f10: 로봇 운영체제·펌웨어 OTA 는 로봇 제조사 영역이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 언어 모델 계획 자체는 44. 로봇 기반 모델·언어 모델 계획의 내용이며 이 영역에는 비용·지연 근거로만 제안함
    - f17: 승강기 통신 로그 생성은 설비 제어 쪽이며 ROP 는 수집·결합만 맡는 것으로 f24 에서 구분함
    - f19: 시뮬레이션·디지털 트윈 자체는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 내용이며 이 영역에는 배포 전 검증 근거로만 제안함. 18. 실시간 세계 상태·데이터 일관성과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 22회/30, 신규 출처 15건/15(출처 상한 도달). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1032 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-04·2026-09-30-05)가 ref-1032~ref-1037 을 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1038~ref-1052 를 순서대로 썼다. 재사용 1건(ref-762, 이전 브리프 2026-09-30-05 재인용, 이번에 다시 열지 않음; 값은 그 브리프의 출처 표를 따랐고 참고문헌 목록 전체는 입력에 없음). 원문 열람: 신규 15건 모두 열었다(webfetch 11건, github_raw 4건). 논문 가운데 Zhang 외(ref-1045)·Lee 외(ref-943)는 PMC 본문을, 나머지는 초록 페이지를 열었다. 교차 확인 1건(f4: ROS 2 공식 릴리스 노트와 Foxglove 블로그). 벤더 문서만 근거로 한 f5·f19 는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에는 f21 로 답했고 결론은 '자기 기술형 기록 형식과 기록 DB + OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적 + 컨테이너 자동 재시작·A/B 롤백·배포 전 시뮬레이션 검증 + 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기'라는 추정이다. 현장 유형 사례는 병원(f15~f18, 국내 고려대학교 구로병원)·물류창고(f19, 벤더 주장)뿐이다. 국내 자료는 개인정보보호위원회 고시(ref-766)와 국내 병원 실증 논문(ref-943) 두 건이다. L. AI·학습 기술 관련 f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안했다. 용어집에 이미 있는 분산 추적·백 파일·무선 업데이트·서비스 수준 협약·감사 추적·모델 레지스트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### data/source_texts/ref-762.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Open-RMF API Server

This API server sets up the necessary endpoints with an Open-RMF deployment and enables the use of the web dashboard. The server comes with the capability of logging to databases, as well as handling authentication and permissions.

# Setup

If not already done so, [install dependencies](../../README.md#Install-dependencies), you can use
```bash
pnpm install -w --filter api-server...
```
to install dependencies for only this package.

# API

Check out the latest API definitions [here](https://open-rmf.github.io/rmf-web/docs/api-server), or visit `/docs` relative to your running server's url, e.g. `http://localhost:8000/docs`.

# Run the server

```bash
rmf_api_server
```

## Configuration

Config files are python modules that export a variable named `config`. See [default_config.py](api_server/default_config.py) for an example and list of the options available. All options are REQUIRED unless specified otherwise.

Configuration is read from the file specified in the env `RMF_API_SERVER_CONFIG`, if not provided, the default config is used.

e.g.
```bash
RMF_API_SERVER_CONFIG='my_config.py' rmf_api_server
```
To run the api-server with PostgreSQL, assuming it has been set up to listen on 127.0.0.1:5432 with user `postgres` and password `postgres`:
```
RMF_API_SERVER_CONFIG=api_server/psql_local_config.py rmf_api_server
```

## Supported databases

rmf-server uses [tortoise-orm](https://github.com/tortoise/tortoise-orm/) to perform database operations. Currently, the supported databases are

* PostgreSQL
* SQLite
* MySQL
* MariaDB

by default it uses a in-memory sqlite instance, to use other databases, install rmf-server with the relevalent extras

* PostgreSQL - postgres
* MySQL - mysql
* MariaDB - maria

.e.g.

```bash
pip3 install rmf-server[postgres]
```

Then in your config, set the `db_url` accordingly, the url should be in the form

```
DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME?PARAM1=value&PARAM2=value
```

for example, to connect to postgres

```
postgres://<user>:<password>@<host>/<database>
```

for more information, see https://tortoise-orm.readthedocs.io/en/latest/databases.html.

### PostgreSQL
If you would like to use PostgreSQL, you will also need to install and set it up. The defaults are for PostgreSQL to be listening on 127.0.0.1:5432.

#### Docker
We can use Docker to quickly bring up a PostgreSQL instance.

Install docker: `https://docs.docker.com/engine/install/ubuntu/`
Start a a database instance: `docker run -it --rm --name rmf-postgres --network=host -e POSTGRES_PASSWORD=postgres -d postgres`

To stop the instance: `docker kill rmf-postgres`

#### Bare Metal
Alternatively, we can install PostgreSQL 'bare metal'.
```
apt install postgresql postgresql-contrib -y
# Set a default password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"

sudo systemctl restart postgresql
# interactive prompt
sudo -i -u postgres
```
To manually reset the database:
```
sudo -u postgres bash -c "dropdb postgres; createdb postgres"
```

## Running behind a proxy

When running behind a reverse proxy like nginx, you need to set the `public_url` option to the url where rmf-server is served on. The reverse proxy also MUST strip the prefix.

For example, if rmf-server is served on https://example.com/rmf/api/v1, `public_url` must be set to `https://example.com/rmf/api/v1` and your reverse proxy must be configured to strip the prefix such that it forwards requests from `/rmf/api/v1/something` to `/something`.

## Running with RMF simulations

When running with rmf simulations, you need to set the env `RMF_SERVER_USE_SIM_TIME=true`. This is needed to ensure that times from the client are correctly converted to RMF's simulation time.

# Authentication and Authorization

## OpenID Connect

rmf-server does not manage user identities and access levels by itself, it uses an OpenID Connect compatible identity provider to perform authentication. Authorization however, is performed in-app by rmf-server.

### Access Token Format

OpenID Connect does not define the format of the access token, the canonical way for a resource server to validate an access token is to use the token introspection endpoint of the authentication server. In order to not have to connect to the identity provider for every request, rmf-server assumes the convention that the access token is a JWT that can be verified independently. Most modern identity providers like keycloak and auth0 follows this convention.

### Access Token Claims

The access token must include the `preferred_username` claim. It will be used to determine an user's authorization levels.

If your identity provider strips standard OIDC claims (such as `preferred_username`) from access tokens issued via the OAuth 2.0 `client_credentials` (M2M) flow and requires custom claims to use a collision-resistant namespaced name, set the optional `preferred_username_claim_namespace` config value to the namespace prefix used by your provider. The authenticator will then check `f"{namespace}preferred_username"` as a fallback when the bare `preferred_username` claim is absent.

This pattern aligns with [RFC 9068 §2.2.2](https://www.rfc-editor.org/rfc/rfc9068.html#section-2.2.2) (which requires that arbitrary attributes in JWT access tokens have "collision resistant" names) and [RFC 7519 §4.2](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.2) (which defines "Collision-Resistant Name" via Public Claim Names). [Auth0 enforces this policy explicitly](https://auth0.com/docs/secure/tokens/json-web-tokens/create-namespaced-custom-claims) for access tokens with a custom API audience — non-namespaced custom claims on standard OIDC names are silently dropped. Operators on other providers with comparable collision-avoidance policies may also benefit; leaving the value unset preserves the current behavior.

## Roles, Actions and Authorization Group

An user's permission to perform certain actions on a protected resource is determined by 3 values, role, action, and authorization group of the resource. A resource belongs to one authorization group and an user can belong to multiple roles. An user has access to perform an action on a resource if any of their roles has permission to perform the action on the authorization group which the resource belongs to. An admin always have permission to perform any action on any group.

For example, given the following permissions and users

Permissions:
| Role | Authz Group | Action |
| --- | --- | --- |
| role1 | group1 | task_submit |
| role2 | group2 | task_submit |
| role3 | group3 | task_submit |
| role4 | group1 | task_submit |
| role4 | group3 | task_submit |

Users:
| User | Roles | Is Admin |
| --- | --- | --- |
| user1 | role1 | false |
| user2 | role2, role3 | false |
| user3 | role4 | false |
| user4 | | true

`user1` will be able to submit a task that belongs to authorization group `group1`. `user2` can submit tasks belonging to `group2` and `group3`. `user3` can submit tasks in group `group1` and `group3`. `user4`, being an admin can submit tasks in any group.

The authorization group of a resource is determined automatically based on different factors according to the resource type. For example, a task's authorization group may be determined by the region where it takes place.

## Synchronization (or lack of) of User Data

rmf-server maintains its own database of users, roles and permissions. In order to keep compatibility with as many identitiy provider as possible and amount of code small, this database is never synchronized with the identity provider's database. Instead, rmf-server takes the following approach to keep things working even without a synchronized database.

* When an user first access any of the protected api, a new rmf-server user is automatically created, the  user will have no roles and no privileges.
  * rmf-server checks if the token is valid before creating the user. If it is valid, the user must exist in the identity provider.
* An admin can use the admin endpoints to perform various user management like
  * Create users
  * Create roles
  * Add/remove permissions to roles
  * Add/remove roles to users
* The admin endpoints only work on rmf-server's database and does not require delegation of any functions to the identity provider, as a result there are some cavaets
  * There is no endpoints to manage an user's authentication like reset user password, enable/disable users etc.
  * Endpoints that list/search users only includes users that is already added on to rmf-server.
* If an admin wishes to manage authorization for an user that exists in the identity provider, but not in rmf-server, they need to use the create user endpoint to create a new user with the same username.
* Deleting an user from rmf-server does not prevent them from accessing "semi-protected" apis (apis that require login but does not require any permissions). It also does not prevent them from logging into a frontend that connects to rmf-server (e.g. rmf dashboard).
  * This is because it does not delete the user from the identity provider and the next time they access any protected api, a new user will be automatically created.
  * Fully deleting an user so that they can no longer login should be done on the identity provider. There is no endpoint in rmf-server to forward deletion of an user to the identity provider because such behaviour may be unintuitive, undesirable and require specialized code paths for every provider.
* If the user is deleted from the identity provider, it will still exist in rmf-server.
  * This is harmless as the user will not be able to authenticate with the identity provider and get a valid token, so a "zombie" user will not be able to access any protected api.
* Since a new user is created with minimal privileges, and an admin is required to give users privileges (including the admin privilege), there is a problem.
  * This is worked around by adding a config to automatically make an user an admin on startup. Note that since there is no synchronization between the identity provider, there is no guarantee that such an user actually exists.

## TODO

A resource's authorizaion group is determined by it's contents. Exactly how they are determined for each type of resource is still either undecided or lacking information from RMF to be implemented, so currently every resource is put into a default empty group of `` (empty string).

## Database Migration

[`aerich`](https://github.com/tortoise/aerich) is a database migration tool for TortoiseORM. `aerich` requires a configuration file for initialization before doing any mutations, which can be found in `api_server.__main__.TORTOISE_ORM`.

Install `aerich`

```bash
pip3 install aerich
```

This migration example will be for PostgreSQL. First, setup `rmf-web` following [instructions](../../README.md). Then, run the `api-server` with `psql`,

```bash
# source RMF
cd ~/rmf-web/packages/api-server
pnpm run start:psql
```

In another terminal, activate the virtual environment manually and initialize `aerich`,

```bash
cd ~/rmf-web
source .venv/bin/activate
cd ~/rmf-web/packages/api-server

# First export the RMF_API_SERVER_CONFIG variable
export RMF_API_SERVER_CONFIG=psql_local_config.py

# Init aerich and save migration workspace to /tmp
aerich init -t api_server.__main__.TORTOISE_ORM --location /tmp/migrations
aerich init-db
```

You can check the current schema of a table. For example, using the `taskstate` table,

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Now, modify the `TaskState` class in the `api_server/models/tortoise_models/tasks.py` to add a new field:

```python
new_field = fields.CharField(255)
```

Don't forget to make necessary changes to `api_server/repositories/tasks.py` too, to allow the dashboard to use the newly added fields.

Now attempt a migration, and allow `aerich` to find the changes required,

```bash
aerich migrate
# aerich will generate the migration file with the version
# check file at /tmp/migration/models/
```

Perform database upgrade,

```bash
aerich upgrade
```

Now, inspecting the database schema, you will find "new_field" available in the schema

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Restart the `api-server` and the changes to the databse should be reflected.

## Running tests

### Running unit tests

```bash
pnpm test
```

By default in-memory sqlite database is used for testing, to test on another database, set the `RMF_API_SERVER_TEST_DB_URL` environment variable.

```bash
RMF_API_SERVER_TEST_DB_URL=<db_url> pnpm test
```

### Collecting code coverage

```bash
pnpm run test:cov
```

Generate coverage report
```bash
pnpm run test:report
```

## Live reload

```bash
uvicorn --reload api_server.app:app
```
````
