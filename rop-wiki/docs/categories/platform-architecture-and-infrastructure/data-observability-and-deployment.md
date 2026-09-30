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
