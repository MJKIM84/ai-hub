# 리서치 브리프 2026-10-12-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-06 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 46. 예측·학습 기반 최적화 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 물류창고 사례 74행 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 이 원문의 미래형·지표 차이(이동 시간 대 배치 효율)를 반영하지 못함. 병원 사례가 초록 기준이라 평가 조건(층·기간·시뮬레이션)과 수치가 없음. 국내 학습 기반 배정 사례·연구가 없음(oq-224)
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area46-s6) — '학습 실패 시 고전 정책 복귀' 가 일반론이고, 대체 정책 호출·예측 가중치 조정의 평가 근거가 없음. 2026년 학습 기반 LMAPF(RL-RH-PP JAIR, SJRL)와 최신 고전 기준선(PUSH)의 조건 비교 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 지도·통신 한계 없음, League of Robot Runners 행이 SILLM 저자의 2023 우승 해법 비교만 근거로 함(2026 시즌 평가 구성·결과 없음), SILLM 공식 구현 없음, ISO 13381-1 서지(발행일·소관 SC) 불완전
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area46-s8) — SILLM '최고 탐색 기반 기준선보다 16.0%' 가 지도별 예외(WPPL 우세 3개 지도)·계획 시간·훈련 비용 없이 실림, Garces 외 '구체 수치는 초록에 없다', SPO '학술지 게재 연도 미확인'
- 섹션 9. 책임 경계 — 158행 '수요 예측 경계는 아직 정하지 않았다'(oq-223), 배터리 SoC 물리 모델 추정과 학습 예측의 구분, WCS 통합 제어 발표와 학습 기반 배정의 구분 없음
- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area46-s4) — 예지 정비·충전 상태 항목이 인계 값의 종류(SoC 변화·이상 클래스·예지)를 구분하지 않음
- 섹션 11. 열린 질문(분리 2026-09-30-area46-s11) — oq-220~oq-224 가 id 없이 실려 있고 부분 근거가 없음. 정정 요청 없음(target.json corrections 비어 있음)

## 조사 질문

1. 학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
2. 학습 기반 지속형 MAPF 의 평균 개선율(SILLM 16.0% 등)은 지도·밀도·계획 예산·훈련 비용 조건에서 어떻게 달라지며, 최신 대회(LoRR 2026)와 고전 기준선(PUSH)은 어떤 조건으로 평가하는가? (섹션 6·7·8 겨냥)
3. oq-220 학습 기반 배정·경로 정책의 개선을 실제 운영 현장에서 제3자가 측정한 자료가 있는가, 시뮬레이션·혼합 현실·회사 주장은 각각 무엇을 보여 주는가? (섹션 5·8·11 겨냥)
4. oq-222 학습·예측 정책이 실패하거나 요청 분포가 바뀔 때 대체 정책 호출과 예측 가중치 조정은 어떻게 설계·평가되는가? (섹션 6·8·11 겨냥)
5. oq-221 배터리 잔량·이상 분류·예지 출력은 어떤 조건에서 나오며 플릿 일정에 어떤 값으로 인계되는가? (섹션 4·9·11 겨냥)
6. oq-223·oq-224 상위 수요예측과 ROP 작업 요청의 경계는 어떻게 나누며, 국내 학습 기반 배정 연구·산업 발표는 무엇을 보여 주는가? (섹션 5·9·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | POGEMA 벤치마크의 분포 밖(Out-of-Distribution) 지표는 학습에 쓴 지도와 장애물 구조가 다른 Cities-tiles 지도 묶음(Cities 지도를 잘라 고친 것)으로 계산한다. | ref-1056 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | POGEMA 저자는 한계로 에이전트 간 통신이 현재 환경에서 분리(disentangled)되어 있지 않다고 밝혀, 통신 지연·손실을 따로 평가하는 구조가 아니다. | ref-1056 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | League of Robot Runners 2026 공식 평가는 7개 지도에 걸친 12개 인스턴스로 이루어지고, 인스턴스별 로봇(에이전트) 수 범위는 50~10,000이며, 평가 서버는 GPU 인스턴스(AMD EPYC 7R13 32 vCPU·128 GiB·Nvidia A10G)와 CPU 인스턴스(같은 CPU 32 vCPU·64 GiB)로 나뉜다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | LoRR 2026 본선 최종 결과는 2026-09-02 공지로 발표됐다(2026-07-23 공지는 8월 7일 발표 예정이라 했고 2026-08-10 공지로 지연을 알림). Combined Track 1위는 Team No Man's Sky(Task Scheduling Track 1위·Line Honours 도 같은 팀)이고, 2026-05-26 AAMAS Prize(Combined Track)는 Team SmartPath 로 별도 집계다. 수상 표에는 팀별 알고리즘(학습 사용 여부) 분류가 없다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [의견] | 대회 순위는 팀별 최종 제출 코드에서 학습을 어디에 썼는지 확인하기 전에는 학습 대 고전 방법의 승률로 바꾸지 말고, 인용할 때 시즌·트랙·인스턴스 구성·CPU/GPU 조건을 함께 적는 것이 맞다고 본다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | SILLM 논문 Table III(대형 지도·에이전트 10,000, 8회 평균 처리량)에서 WPPL 이 SILLM 보다 높은 지도가 6개 중 3개(Sortation 44.28 대 43.98, Warehouse 42.83 대 42.24, Random-1 54.38 대 53.74)이고, SILLM 은 Paris(31.00 대 23.74)·Berlin(30.52 대 20.35)·Random-2(44.37 대 37.30)에서 높았다. 단계당 평균 계획 시간은 SILLM 0.349초, WPPL 4.143초였다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [추정] | 초록의 '최고 탐색 기반 기준선 대비 16.0%'는 Table III 대형 지도 6종에서 WPPL 대비 지도별 처리량 비율을 평균한 값(재계산 약 16.05%)과 일치하므로, 모든 지도에서 16% 앞섰다는 뜻이 아니라 지도별 비율의 평균으로 읽는 것이 맞아 보인다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | SILLM 공식 부록은 지도마다 SILLM 모델 훈련에 12시간 미만이 걸렸다고 적으며, 훈련 서버는 72 vCPU AMD EPYC 9754·RTX 4090D(24GB) 4장·메모리 240GB였다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | SILLM 공식 저장소(DiligentPanda/Scalable-Imitation-Learning-for-LMAPF) README 는 Backward Dijkstra·정적 안내(Static Guidance)·동적 안내(Dynamic Guidance) 버전을 별도 브랜치(static_guidance, dynamic_guidance)로 관리하며, Backward Dijkstra 는 정적 안내 설정에서 map_weights_path 를 비운 것과 거의 같다고 설명한다. | ref-1638 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | 공식 저장소의 1-GPU 예시 설정 파일(…sortation_small_a600_s500_none_annotated_1gpu.yaml)은 max_dagger_iterations 를 100으로 두지만 논문은 모방 학습을 12회 반복했다고 적어, 공개 예시 설정과 논문 실험 설정은 같은 것이 아니다. | ref-1638, ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [의견] | 학습 기반 경로 방법의 평균 개선율을 인용할 때는 지도별 우열, 단계당 계획 시간, 지도별 훈련 비용, 공개 구현의 브랜치·설정 파일을 함께 적어야 하며, 10,000 에이전트 시뮬레이션을 실물 플릿 규모로 읽지 않는 것이 맞다고 본다. | ref-199, ref-1638 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | RL-RH-PP(강화학습 안내 롤링 호라이즌 우선순위 계획, JAIR 85, 2026-03-24 게재)의 기준선 비교는 서로 다른 시드의 보류(held-out) 평가 환경 16개 평균이며, 800단계 창고 시뮬레이션(Amazon 풀필먼트 모사·Symbotic 모사 지도)에서 모든 해법에 계획 단계당 CPU 1초를 주고 시간 초과 해에는 같은 수리 기법을 적용했다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [사실] | RL-RH-PP 논문 Table 3 의 Symbotic 모사 지도에서 에이전트당 처리량은 80대일 때 RH-PBS 20.83 이 RL-RH-PP 18.38 보다 높았고, 100대(15.38 대 14.04)·120대(11.31 대 1.76)에서는 RL-RH-PP 가 높았다. 같은 표의 WPPL 은 16.29·13.73·10.05 였다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [사실] | RL-RH-PP 는 에이전트 밀도마다 정책을 처음부터 따로 학습했고, 가장 긴 훈련(120대)은 RTX 6000 Ada GPU 한 장으로 약 4일 걸렸다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | LSMART 는 처리량과 함께, 계획 실패 때 대체(fail) 정책을 부른 횟수를 계획기 호출 횟수로 나눈 비율을 평가 지표로 쓴다. | ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | LSMART 의 대체 정책 비교에서는 지도와 계획 창 조건에 따라 LRGW 또는 PIBT 가 가장 높은 처리량을 냈으며, 한 대체 정책이 모든 조건에서 최선은 아니었다. | ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | 2026-08 프리프린트 PUSH(Path Updates over Staggered Horizons)의 비교 실험은 1,000단계 실행·단계당 1초 계획 예산·무작위 5회 평균으로, AMD Threadripper 3990X·192GB 메모리 장비에서 수행했다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | PUSH 비교에서 RHCR 를 뺀 알고리즘은 시간 초과 시 계획 못 한 에이전트가 직전 단계 경로를 따르고, RHCR 는 K단계마다 K초를 받되 시간 초과 시 K단계 동안 PIBT 로 실행한 뒤 RHCR 로 돌아간다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [의견] | PUSH 는 학습 요소가 없는 고전 탐색 알고리즘이므로 이 영역에서는 학습 정책을 평가할 때 맞춰야 할 고전 기준선의 예산·실패 처리 조건을 보여 주는 대조 사례로만 다루고, 학습 성과 근거로 쓰지 않는 것이 맞다고 본다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [사실] | SJRL(탐색 보조 에이전트–환경 공동 강화학습, 2026-08 프리프린트)은 지도마다 256대로 정책을 학습해 같은 지도에서 32~320대(32대 간격)로 평가하며, 일반화는 초기 상태·목표·에이전트 수에 대해 보고 지도 간 일반화는 다루지 않는다. 각 평가는 512단계다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f21 | [사실] | SJRL 의 물리 로봇 검증은 실물 로봇 8대와 가상 로봇 248대를 섞은 혼합 현실 창고 환경에서 이루어졌다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | SJRL 저자는 비교한 모방학습 방법들을 회전 동작을 포함한 LMAPF-R2 문제 모델에 맞게 고치는 일을 향후 과제로 남겨, 비교 방법들의 문제 모델이 같지 않다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [추정] | Amazon Robotics 의 DeepFleet 보고서(arXiv v3, 'Unpublished technical report')는 학습에서 제외한 7개 창고 층의 7일 자료에서 로봇 궤적을 60초 앞까지 반복 추론해 실제 궤적과 비교하는 오프라인 예측 평가를 보고한다. | ref-1053 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f24 | [추정] | DeepFleet 보고서 Table 2 에서 로봇 중심(RC) 모델의 혼잡 지연 오차(CDE)는 3.40%로 네 구조 가운데 가장 낮았다(RF 9.60%, GF 14.22%, IF 186.56%). 이는 예측한 혼잡 지연과 실제의 상대 오차이며 이동 시간 절감률이 아니다. | ref-1053 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f25 | [추정] | Amazon 의 DeepFleet 10% 수치는 표현이 엇갈린다: About Amazon 발표(2025-07-01)는 핵심 요약에서 '이동 효율을 10% 높일 것(will improve)', 본문에서 '이동 시간을 10% 개선/줄여'라고 쓰고, Amazon Science 블로그(2025-08-11)는 '로봇 배치 효율을 10% 높이고 있다'고 쓴다. 비교 기간·대상 현장·분모는 공개하지 않아, 위키의 '이동 효율을 10% 높였다' 서술은 고쳐야 한다. | ref-916, ref-1054 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f26 | [의견] | 예측 정확도(궤적·혼잡 오차), 오프라인 결정 손실, 온라인 운영 개선은 서로 다른 승인 지표로 두고, 운영 개선 수치는 개입 시점과 비교 플릿을 확인한 뒤에만 성과로 반영하는 것이 맞다고 본다. | ref-1053, ref-916 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | Garces 외의 병원 배정 평가는 BIDMC 서관 입원 병동 4개 층(층당 병상 약 25~30)의 2024-06-24~2025-06-29 요청 이력에서 층마다 수요 높음·중간·낮음 주를 2주씩 골라 층당 42일, 정책당 168개 층-일을 하루 12시간(오전 6시~오후 6시) 시뮬레이션한 것이며, 나머지 이력은 학습·검증에 썼다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 시작 조건 | — |
| f28 | [사실] | Garces 외의 방법에서 예측 신뢰도 가중치는 표본 추출한 미래(예측) 요청에만 적용되고, 이미 관측된 요청과 예약 요청은 항상 가중치 1을 받는다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 제약 | — |
| f29 | [사실] | Garces 외 Table 3 의 수요 높음 조건(요청 36,948건)에서 제안 방법과 탐욕 배정을 포함한 대부분 정책의 거절 건수는 0이었고, Token Passing 과 Token Passing with Task Swaps 만 28건을 거절했다. 저자는 처리 건수만으로는 강한 정책들을 구분할 수 없어 대기 시간으로 비교했다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 예외·성과 | — |
| f30 | [사실] | Garces 외는 수요 높은 주에서 제안 방법이 일별 평균 대기 시간의 중앙값을 약 5%, 일별 95분위 대기 시간의 중앙값을 약 10% 줄였고, 두 지표의 75분위와 최댓값은 기준선 대비 15% 넘게 줄였다고 보고했다. 모든 수요 구간에서 가장 크고 일관된 개선은 95분위 대기 시간 지표에서 나왔다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 예외·성과 | — |
| f31 | [의견] | 분포 이동에 대응해 예측 가중치를 낮추는 장치와, 계획 실패·시간 초과 때 고전 정책으로 돌아가는 트리거는 따로 설계·기록하고, 이미 시작한 작업과 아직 시작하지 않은 배정을 구분해 다루는 것이 맞다고 본다. | ref-1062, ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f32 | [사실] | Pookkuttath 외의 실시간 진동 분류 정확도 91%는 Snail 청소 로봇에서 모바일 앱의 요청(request-based) 표본 방식으로 모은 시험 표본 100개(Table 5)로 계산한 값이며, 클래스별 정확도는 88.7~93.5%였다. | ref-1057 | 아니오 | medium | 2026-10-12 | 기타 / 예외·성과 | — |
| f33 | [사실] | ISO 13381-1:2025 는 ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행(단계 60.60)됐고 23쪽이다. | ref-1060 | 아니오 | medium | 2026-10-12 | — | — |
| f34 | [사실] | Open-RMF rmf_battery 의 SimpleMotionPowerSink 는 로봇이 궤적을 따라 가감속하는 데 드는 에너지로 배터리 충전 상태(SoC) 변화를 추정하고, SimpleDevicePowerSink 는 탑재 장치의 소비 전력으로 SoC 변화를 추정하는 물리 모델 API 이며 학습 모델이 아니다. | ref-1642 | 아니오 | medium | 2026-10-12 | — | — |
| f35 | [의견] | 배터리·고장 쪽 인계 값은 물리 모델의 SoC 변화 추정(Open-RMF rmf_battery, 28. 공용 자원·충전·에너지 최적화 맥락), 학습 모델의 현재 이상 클래스(진동 분류), 고장까지 남은 시간 같은 예지 출력을 서로 다른 값으로 구분해 넘기고, 이 영역은 학습·예측으로 얻은 값만 다루는 것이 경계로 맞다고 본다. | ref-1642, ref-1057, ref-1060 | 아니오 | medium | 2026-10-12 | — | — |
| f36 | [사실] | Open-RMF 작업 요청 스키마(task_request.json)의 fleet_name 은 플릿 이름 하나(문자열) 또는 이름 배열을 받을 수 있고, 지정하면 그 플릿(들)만 입찰한다. | ref-125 | 아니오 | medium | 2026-10-12 | — | — |
| f37 | [의견] | 상위 업무 시스템은 주문 전망과 시간 범위를 계획에 쓰고, ROP 는 실제로 들어온 요청을 플릿·능력·가장 이른 시작 시각 조건과 함께 받아 배정하는 것으로 책임을 나누며, 예측 요청을 확정 요청으로 자동 바꾸는 규칙은 별도 승인을 거치게 하는 것이 맞다고 본다. | ref-125, ref-1063, ref-1062 | 아니오 | medium | 2026-10-12 | — | — |
| f38 | [사실] | 강민교·김인철(한국로봇학회 논문지 18(2), 2023)의 제조 물류 작업 안전성·효율성 학습 실험은 NVIDIA Isaac 시뮬레이터 안 가상 제조 물류 환경에서 이동 로봇 2대로 수행됐고, 실제 하드웨어 로봇 적용·검증은 향후 연구로 남겼다. | ref-1643 | 아니오 | medium | 2026-10-12 | 제조 공장 / 수행 자원 | — |
| f39 | [사실] | 이 논문은 두 로봇의 정책 파라미터 등급이 같아 안전성·효율성 등급이 모두 같게 예측되는 드문 상태에서는 어느 로봇에 작업을 배정할지 판정하기 어렵다고 적고, 더 많은 정책 파라미터와 규칙이 필요하다고 본다. | ref-1643 | 아니오 | medium | 2026-10-12 | 제조 공장 / 예외·성과 | — |
| f40 | [추정] | 현대글로비스는 알티올과 공동 개발한 창고제어시스템(WCS) 플랫폼 오르카(ORCA)가 작업 계획을 실제 작업으로 바꾸고 각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정하며, 어댑터 인터페이스로 다른 제조사 설비를 같은 방식으로 연결한다고 설명한다. 학습 모델이나 고전 방법 대비 성과는 밝히지 않았다. | ref-1644 | 아니오 | low | 2026-10-12 | 물류창고 / 수행 자원 | 벤더 주장 |
| f41 | [의견] | 오르카 같은 국내 통합 제어 발표는 학습 기반 배정·경로의 운영 효과 근거가 아니라 20. 로봇·제조사 관제 연동과 61. 물류창고 쪽 통합 운영 사례로 보고, 이 영역에서는 학습 요소가 확인되지 않은 경계 사례로만 다루는 것이 맞다고 본다. | ref-1644 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [사실] | Smart "Predict, then Optimize"(Elmachtoub·Grigas)는 Management Science 68권 1호 9–26쪽(2022-01)에 게재됐다. | ref-1061 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [추정] | 학습 기반 배정·경로 정책을 실제 운영 현장에서 탐색·규칙 기반 방법과 같은 조건으로 제3자가 측정한 자료는 이번에도 찾지 못했고, 확인한 근거는 시뮬레이션(SILLM·RL-RH-PP·Garces 외), 혼합 현실(SJRL 실물 8대+가상 248대), 회사 자체 주장(DeepFleet 10%)으로 나뉜다. | ref-199, ref-1639, ref-1062, ref-1641, ref-916 | 아니오 | low | 2026-10-12 | — | — |
| f44 | [의견] | 학습과 고전 방법의 우열은 지도·밀도·계획 예산·실패 처리(복귀 정책)를 같게 맞춘 조건에서만 판단하고, 한 논문의 평균 개선율을 다른 논문의 수치와 섞어 순위를 만들지 않는 것이 맞다고 본다. | ref-199, ref-1639, ref-1640, ref-604 | 아니오 | medium | 2026-10-12 | — | — |

### 근거 발췌

- **f1**: arXiv v3 §4.2·부록: "Out-of-Distribution metric was calculated on Cities-tiles dataset", 평가용 지도는 "different structure of obstacles"를 갖도록 Cities-tiles 를 쓴다. 기존 위키(2026-09-30-area46-s6·s7·s8)는 LaCAM·RHCR 우위만 적고 일반화 지표의 지도 분할은 적지 않음. 격자 MAPF 벤치마크 정의이며 실물 현장 검증 아님
- **f2**: arXiv v3 §5(한계): "communication between agents is not currently disentangled". 플랫폼 자체의 명시 한계이며 통신 장애에서 안전하다는 보장이 아님
- **f3**: evaluation.md: "12 instances across 7 maps spanning diverse domains: mazes, rooms, random grids, warehouses, and large-scale game maps"; Benchmark Configuration Ranges 표 Team size "50 – 10,000"; Evaluation Process 의 GPU Instance·CPU Instance 사양. 저장소 고정 커밋 9d5e337 기준, 커밋 날짜 미확인. 시뮬레이션 평가 규칙이며 실제 창고 성과 아님
- **f4**: updates.md: "Results Announcement for Main Round 2026! `2 Sep 2026`" 수상 표 First Place/Combined Track "Team No Man's Sky"; "Delayed Announcement `10 August 2026`"; "Finish Line! `23 July 2026`" 의 "on **7 August 2026**"; "2026 AAMAS Prize Announcement `26 May 2026`" Team **SmartPath**. 참가 69팀·제출 3,361건. rules.md 3항: 제출 코드는 결과 발표 뒤 공개
- **f5**: f3·f4 에 근거한 판단. 수상 표에 알고리즘 분류가 없고 평가 자원이 GPU·CPU 두 구성으로 나뉜다(evaluation.md). LoRR 2026 의 주 위치는 27·54·25 영역이며 46 에는 요약·연결만 둔다
- **f6**: arXiv v2 Table III 오른쪽(Large maps with 10,000 agents) SILLM 행 "43.98 42.24 31.00 30.52 53.74 44.37 … 0.349", WPPL 행 "44.28 42.83 23.74 20.35 54.38 37.30 … 4.143". 비교 WPPL 은 회전 동작 제거·LNS 반복 40,000회 제한 조건(부록 F.1, 기존 2026-10-10-area27-s8.md 42행에 있음)
- **f7**: 초록 "throughput improvements of 137.7% and 16.0%, respectively". Table III 값으로 (43.98/44.28+42.24/42.83+31.00/23.74+30.52/20.35+53.74/54.38+44.37/37.30)/6−1 ≈ 0.1605. 논문이 계산 방식을 명시하지 않아 해석은 추정(독립 검증 2026-10-12 재계산)
- **f8**: arXiv v2 부록 E. Computation Resources: "trained on servers with 72 vCPU AMD EPYC 9754 128-Core Processor, 4 RTX 4090D (24GB), and 240 GB memory. Training on each map takes less than 12 hours." 프로젝트 부록 PDF 같은 문장
- **f9**: README(static_guidance·master 브랜치) "Static Guidance Version": "we maintain Backward Dijkstra, Static Guidance and Dynamic Guidance versions in separate branches (`static_guidance`,`dynamic_guidance`)", "set the `map_weights_path` to `""`". 메모가 쓴 wuwen-T 저장소는 미러라 공식 저장소로 출처를 바꿈. 코드 실행·재현은 하지 않음
- **f10**: YAML framework 절 "max_dagger_iterations: 100 # NOTE: how many iterations of imitation learning to run"; README 는 이 파일을 RTX4090D 1장·16 vCPU 예시로 소개. 논문 §IV "We iterate the imitation 12 times". 같은 연구팀 자료라 교차 확인 아님
- **f11**: f6~f10 에 근거한 판단. 기존 2026-10-10-area27-s8.md 42행도 10,000 을 계산 벤치마크 규모로 읽는다
- **f12**: arXiv 2603.23838v1 §5.1.3: "Each solver is allocated a total time budget of 1s CPU time per planning step", "we apply the same repair mechanism … to any infeasible solution returned upon solver timeout", "averaged over 16 held-out evaluation environments with different random seeds", "T = 800". JAIR 메타데이터 citation_date 2026/03/24, DOI 10.1613/jair.1.20611. MIT·Symbotic 공동 저자
- **f13**: Table 3 Symbotic 블록: "RH-PBS 20.83 ± 1.32 … 14.04 ± 5.39 … 1.76 ± 1.10", "RL-RH-PP (ours) 18.38 ± 0.50 … 15.38 ± 1.85 … 11.31 ± 2.21", "WPPL 16.29 … 13.73 … 10.05" (열 N=80·100·120, TPA). 동료 심사 학술지 게재지만 단일 연구의 자체 비교. 메모는 [추정]으로 냈으나 표 값 보고는 원문 확인이 되어 [사실], 해석은 밀도별로 한정
- **f14**: §5.1.2: "For each agent density setting, we train a separate RL policy from scratch." "The longest training duration, corresponding to N = 120, is approximately four days." "a single NVIDIA RTX 6000 Ada GPU". 온라인 추론 시간과 구별
- **f15**: arXiv 2602.15721v1 §4.1 Metrics: "(1) throughput and (2) the ratio of fail policy calls" (계획기 호출 대비). 600초×10회 실험 조건과 실패 정책 개념은 기존 2026-10-10-area27-s8.md 43행에 있음 — 새로운 것은 이 지표
- **f16**: §4.4 Experiment Result: 대체 정책으로 "(1) PIBT … and (2) LRGW"를 비교하고 지도별로 "LRGW and PIBT"가 최고 처리량을 나눠 가짐. 차동구동 AGV 시뮬레이션이며 분포 이동 탐지 실험은 아님
- **f17**: arXiv 2608.06702v1 §V-A.4 Evaluation Criteria: "We run each experiment for 1,000 timesteps with a 1-second per-timestep planning budget … averaged over 5 randomized trials"; §V "AMD Threadripper 3990X 64-core processor with 192 GB of RAM". 학습을 쓰지 않는 탐색 기반 알고리즘
- **f18**: §V-A.4: "unplanned agents fall back on their paths from the previous timestep", "it receives K seconds of planning time per rolling horizon … If it times out, we default to PIBT for K steps before returning back to RHCR." 알고리즘마다 실패 처리가 같지 않음
- **f19**: f17·f18 에 근거한 판단. 독립 검증(2026-10-12): PUSH 는 학습과 무관해 46 에서는 대조군·경계 설명으로만
- **f20**: arXiv 2608.05588v1 §5: "For each map, we train a policy with 256 agents and evaluate it with 32–320 agents in increments of 32. Each evaluation runs for 512 timesteps"; "generalization across initial states, goal locations, and numbers of agents rather than across maps". SILLM 과 공동 저자(Jiang·Li 등)라 독립 재현 아님
- **f21**: 초록·부록 C.3: "a challenging mixed-reality warehouse environment with 8 physical robots and 248 virtual robots". 256대 실물 운영이나 독립 창고 실측이 아님
- **f22**: §5.2: "such an adaptation would require non-trivial modifications … We therefore leave the adaptation of IL methods to the LMAPF-R2 model for future work." 성능 차이를 모두 강화학습 자체의 이득으로 돌릴 수 없음
- **f23**: 벤더 주장: arXiv 2508.08574v3 §4 "our test dataset, which consisted of 7 days across 7 warehouse floors that were held out during training", "roll out robot trajectories 60 seconds into the future". arXiv 메타데이터 journal-ref "Unpublished technical report, Amazon Robotics, Aug. 2025" — 동료 심사 없는 회사 자체 보고서라 [추정]. 개입 대조 실험 아님
- **f24**: 벤더 주장: Table 2 "Robot-Centric (RC) 97M 8.68 0.11 14.91 3.40", RF "9.60", IF "186.56", GF "14.22" (열 CDE (%)). 회사 자체 보고서 수치
- **f25**: 벤더 주장: aboutamazon.com 요약 "will improve robot fleet travel efficiency by 10%", 본문 "improving the travel time of our robotic fleet by 10%", "By reducing robot travel time by 10%"(article:published_time 2025-07-01). amazon.science "increasing the efficiency of our robot deployments by 10%"(datePublished 2025-08-11). 두 자료 모두 Amazon 이라 독립 확인 아님
- **f26**: f23~f25 에 근거한 판단
- **f27**: arXiv 2608.21554v1 §5.1: "four inpatient floors from the west wing of BIDMC", "The historical data span June 24, 2024 through June 29, 2025", "42 test days per floor and 168 floor-day evaluations per policy", "simulated over a 12 hour window starting at 6am". 실물 로봇 병원 배치 아님
- **f28**: §4.6: observed requests and scheduled requests "always receive unit weight", "predicted requests are weighted according" to 최근 예측 오차. 롤아웃의 미래 비용 평가에만 쓰이며 확정 요청을 바꾸지 않음
- **f29**: §5.5.3 Table 3 High demand: "Greedy Assignment Policy 36,948 0", "Proposed Adaptive Rollout 36,948 0", Token Passing 두 변형 "36,920 28"; 본문 "aggregate rejection counts alone do not fully distinguish the stronger policies"
- **f30**: §5.5.4: "The median improvement is approximately 5% for the mean wait-time metric and approximately 10% for the 95-th percentile metric", "reduces the 75-th percentile and maximum values of both wait-time metrics by more than 15%"; "Across all demand regimes, the largest and most consistent gains appear in the 95-th percentile wait-time metric." 기존 s8 '구체 수치는 초록에 없다'를 본문 수치로 정정
- **f31**: f16·f28 에 근거한 판단. 가중치 조정(Garces 외)과 대체 정책 호출(LSMART)은 다른 장치이며 공통 분포 이동 감지 임계값을 정한 근거는 확인하지 못함
- **f32**: Europe PMC 전문(PMC8747287) §5.5: "Table 5 shows the statistical measure result for 100 test samples collected from the real-time case study … on request-based sample mode", "88.9%, 93.5%, 91.8%, 92.1%, and 88.7%", "real-time tests is slightly less (91%)". 기존 91%·92.2% 는 위키에 있음 — 새로운 것은 표본 수·수집 방식
- **f33**: ISO 공식 목록·공개 메타데이터: "publicationDate":"2025-09-02", "edition":3, "ownerCommittee":"ISO/TC 108/SC 5", "pages":{"en":23}, currentStage 6060. 규범 본문은 유료라 열지 않음. ref-1060 서지(발행 '2025', 'ISO/TC 108') 보정
- **f34**: README API 목록: SimpleMotionPowerSink "can estimate the change in state-of-charge of the battery from the energy consumed to accelerate/decelerate a robot as it moves along a trajectory"; SimpleDevicePowerSink "from the PowerSystem's energy consumption over a duration". 고장 예지·잔여 수명 예측 성능 주장 아님
- **f35**: f32~f34 에 근거한 판단. 공통 고장 데이터 계약과 모델 소유권 합의는 확인하지 못함(oq-221 부분 근거)
- **f36**: task_request.json properties.fleet_name: "The name of the fleet, or an array of fleet names, allowed to perform this task. If specified, only the named fleet(s) will bid for this task.", oneOf string/array. 독립 검증: rmf_api_msgs 0.7.0 CHANGELOG(2026-09-18) "Allow fleet_name to be either string or string array". fleet_name 필드 자체는 기존 2026-09-29-area09-s7.md 40행에 있음 — 새로운 것은 배열 허용
- **f37**: f28·f36 에 근거한 판단. CJ대한통운 iFlex 주문 유형별 물량 예측(기존 5절·9절, ref-1063)은 상위 쪽 예시이고, Garces 외는 즉시 확정을 이미 들어온 요청에만 한다. 공통 표준으로 확인된 경계는 아님(oq-223 부분 근거)
- **f38**: §4.1(p.229): Isaac 시뮬레이터로 만든 실험 환경에 "이동 로봇 2대"·화물·이동 장애물 배치, Intel Xeon Silver 4210R·RTX A5000 3개; §5 결론: "하드웨어 로봇들을 포함한 실제 제조 작업 환경에 적용하여 성능을 검증"하는 것이 향후 연구. 심층 관계형 강화학습 기반 정책 규칙 학습
- **f39**: §4.2(p.231): 네 번째 상태는 "robot1과 robot2에 관해 추론된 정책 파라미터들의 등급이 모두 같아서" … "어느 로봇에게 작업을 할당해야 될지 판정하기 어려워진다"
- **f40**: 벤더 주장: 현대자동차그룹 Story(2026-04-16) "각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정합니다", "어댑터 인터페이스 구조를 통해 서로 다른 제조사의 설비도 동일한 방식으로 연결". 학습되는 변수·비교 정책·현장 효과 분모 미공개
- **f41**: f40 에 근거한 판단. 독립 검증(2026-10-12): 학습 요소 없음 → 영역 20·61 맥락
- **f42**: Crossref 서지: DOI 10.1287/mnsc.2020.3922, container-title "Management Science", volume 68, issue 1, page "9-26", published-print 2022-01. 기존 s8 '학술지 게재 연도 미확인' 정정
- **f43**: f6·f12·f27·f21·f25 를 묶은 판단. oq-220 부분 근거이며 해결 아님
- **f44**: f6·f13·f17·f18·f16 에 근거한 판단: SILLM 은 지도 6개 중 3개에서 WPPL 보다 낮고, RL-RH-PP 는 80대에서 RH-PBS 보다 낮으며, PUSH·LSMART 는 알고리즘마다 시간 초과 처리가 다르다

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1056 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 2025-04 | 논문 | high | 2026-10-12 | https://arxiv.org/abs/2407.14931 | 아니오 |
| ref-1637 | League of Robot Runners 조직위원회 (MAPF-Competition/web_resource, GitHub) | League of Robot Runners 2026 — Evaluation Process(evaluation.md)·Updates(updates.md)·Competition Rules(rules.md) | 미확인 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/MAPF-Competition/web_resource/tree/9d5e3378979561a55645cb737ca5e71bc91f020b | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10-28 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-1638 | He Jiang (DiligentPanda, GitHub) — SILLM 저자 공식 저장소 | Deploying Ten Thousand Robots: Scalable Imitaion Learning for Lifelong Multi-Agent Path Finding — README·예시 설정(Scalable-Imitation-Learning-for-LMAPF) | 미확인 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2602.15721 | 아니오 |
| ref-1639 | Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85) | Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation | 2026-03-24 | 논문 | medium | 2026-10-12 | https://doi.org/10.1613/jair.1.20611 | 아니오 |
| ref-1640 | Sanjay, V., & Li, J. (arXiv) | Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF | 2026-08-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.06702 | 아니오 |
| ref-1641 | Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv) | Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations | 2026-08-06 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.05588 | 아니오 |
| ref-1053 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 2025-08 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2508.08574 | 아니오 |
| ref-916 | Amazon | Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot | 2025-07-01 | 벤더 문서 | medium | 2026-10-12 | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model | 아니오 |
| ref-1054 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 2025-08-11 | 벤더 문서 | medium | 2026-10-12 | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination | 아니오 |
| ref-1062 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 2026-08-21 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.21554 | 아니오 |
| ref-1057 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 2021-12-21 | 논문 | high | 2026-10-12 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ | 아니오 |
| ref-1060 | ISO (ISO/TC 108/SC 5) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements | 2025-09-02 | 표준 | medium | 2026-10-12 | https://www.iso.org/standard/88029.html | 아니오 |
| ref-1642 | Open-RMF 유지관리자 (open-rmf, GitHub) | rmf_battery — README | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-1063 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명 | 2021-07-28 | 벤더 문서 | medium | 2026-10-12 | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 | 아니오 |
| ref-1643 | 강민교, 김인철 (한국로봇학회 논문지 18(2)) | 다중 로봇 제조 물류 작업을 위한 안전성과 효율성 학습 (Safety and Efficiency Learning for Multi-Robot Manufacturing Logistics Tasks) | 2023-06 | 논문 | medium | 2026-10-12 | https://doi.org/10.7746/jkros.2023.18.2.225 | 아니오 |
| ref-1644 | 현대자동차그룹 (현대글로비스) | 현대글로비스가 그리는 자동화를 넘어선 물류의 미래 | 2026-04-16 | 벤더 문서 | medium | 2026-10-12 | https://www.hyundaimotorgroup.com/ko/story/hyundai-glovis-physical-ai-logistics | 아니오 |
| ref-1061 | Elmachtoub, A. N., & Grigas, P. (arXiv; Management Science 68(1)) | Smart "Predict, then Optimize" | 2017-10 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/1710.08005 | 아니오 |

### 출처 요약

- **ref-1056**: 고전·학습·혼합 MAPF 방법 비교 벤치마크(arXiv v3, v1 2024-07-20). 이번에는 §4.2 분포 밖 평가용 Cities-tiles 지도와 §5 통신 미분리 한계를 확인했다.
- **ref-1637**: LoRR 2026 공식 웹 자료 저장소(고정 커밋 9d5e337, 커밋 날짜 미확인). 평가 구성(7개 지도 12개 인스턴스, 50~10,000 에이전트, GPU·CPU 인스턴스)과 2026-09-02 최종 결과·2026-08-10 지연·2026-05-26 AAMAS Prize 공지를 담는다.
- **ref-199**: SILLM 논문(arXiv v2 2025-05-18, v1 2024-10-28). Table III 지도별 처리량·계획 시간과 부록 E(훈련 자원·12시간 미만)·F.1(WPPL 비교 조건)을 확인했다.
- **ref-1638**: SILLM 프로젝트 페이지가 링크한 공식 코드 저장소. README 는 Backward Dijkstra·정적·동적 안내 버전을 별도 브랜치로 관리한다고 설명하고, 1-GPU 예시 YAML 은 max_dagger_iterations 100 을 둔다. 코드 실행은 하지 않았다.
- **ref-604**: LSMART 프리프린트. §4.1 대체 정책 호출 비율 지표와 §4.4 LRGW·PIBT 대체 정책 비교 결과를 확인했다.
- **ref-1639**: RL-RH-PP 를 제안한 JAIR 게재 논문(2026-03-24, arXiv 2603.23838 2026-03-25). 16개 보류 환경·800단계·단계당 CPU 1초 조건의 Amazon·Symbotic 모사 지도 비교(Table 3)와 밀도별 훈련 비용을 담는다.
- **ref-1640**: 학습 없는 지속형 MAPF 알고리즘 PUSH 를 제안한 프리프린트. 1,000단계·단계당 1초·5회 평균 조건과 알고리즘별 시간 초과 처리(RHCR 의 PIBT 대체)를 적는다.
- **ref-1641**: 회전을 포함한 지속형 MAPF 에 탐색 보조 공동 강화학습(SJRL)을 제안한 프리프린트. 지도별 학습·32~320대 평가와 실물 8대+가상 248대 혼합 현실 검증을 보고한다. SILLM 과 공동 저자.
- **ref-1053**: Amazon Robotics 의 다중 로봇 기반 모델 보고서(arXiv v3 2026-04-13). arXiv 메타데이터상 'Unpublished technical report, Amazon Robotics' 로 동료 심사 없는 회사 자체 보고서다. 7개 층·7일 보류 자료의 60초 궤적 예측 평가와 Table 2 CDE 를 확인했다.
- **ref-916**: Amazon 공식 발표(Scott Dresser, 페이지 메타 article:published_time 2025-07-01). DeepFleet 10% 를 요약은 '이동 효율을 높일 것', 본문은 '이동 시간 10% 개선/감소'로 적는다.
- **ref-1054**: Amazon Science 블로그. DeepFleet 이 작업 배정과 혼잡 회피 경로에 쓰여 '로봇 배치 효율을 10% 높이고 있다'고 적는다.
- **ref-1062**: 병원 이기종 로봇 배정의 예측 인지형 모델 기반 강화학습 프리프린트. 본문에서 BIDMC 4개 층 168 층-일 평가, 확정 요청 가중치 1, Table 3 거절 건수, 대기 시간 개선 수치를 확인했다.
- **ref-1057**: 청소 로봇 IMU 진동 5종 분류 기반 예지 정비 프레임워크(Sensors 22(1):13). Europe PMC 전문으로 실시간 시험 표본 100개(Table 5)와 요청 방식 수집을 확인했다.
- **ref-1060**: 기계 상태 감시·진단의 예지 일반 지침 제3판. 공식 목록·공개 메타데이터로 발행 2025-09-02·23쪽·SC 5 소관을 확인했고 규범 본문은 열지 않았다.
- **ref-1642**: Open-RMF 배터리 추정 라이브러리 README. 이동 궤적의 가감속 에너지(SimpleMotionPowerSink)와 장치 소비 전력(SimpleDevicePowerSink)으로 SoC 변화를 추정하는 API 를 설명한다(물리 모델, 학습 아님).
- **ref-125**: Open-RMF 작업 요청 JSON 스키마. fleet_name 이 문자열 또는 문자열 배열을 받고 지정한 플릿만 입찰한다(0.7.0, CHANGELOG 2026-09-18 — 독립 검증 기준).
- **ref-1063**: CJ대한통운 뉴스룸 게시물. 이플렉스가 주문 유형별 수요를 예측해 센터 인력 운영에 쓴다고 설명한다(기존 위키 5·9절에 이미 있음, 이번에는 책임 경계 의견의 참고로만 씀).
- **ref-1643**: 심층 관계형 강화학습으로 제조 물류 작업의 안전성·효율성 등급을 예측해 로봇에 배정하는 국내 연구(pp.225–232). Isaac 시뮬레이터 안 이동 로봇 2대로 실험했고 실물 검증은 향후 과제다.
- **ref-1644**: 현대자동차그룹 Story 기업 게시물. AW 2026 전시와 현대글로비스·알티올의 WCS 플랫폼 오르카(설비 상태·우선순위에 따른 동선·작업 순서 실시간 조정, 어댑터 인터페이스)를 소개한다. 학습 모델·성과 분모는 밝히지 않는다.
- **ref-1061**: 결정 손실(SPO)·SPO+ 로 예측을 학습하는 틀. Crossref 서지로 학술지 게재본(Management Science 68(1):9–26, 2022-01, DOI 10.1287/mnsc.2020.3922)을 확인했다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등, 정정 요청 없음): 섹션 4(분리 2026-09-30-area46-s4) — '예지와 예지 정비' 항목의 ISO 13381-1 서지를 2025-09-02 발행·제3판·ISO/TC 108/SC 5·23쪽으로 보강(f33, ref-1060 서지 보정). '충전 상태' 항목에 물리 모델 SoC 추정(rmf_battery, f34)과 학습 예측을 구분하는 경계 설명(f35)만 덧붙임(rmf_battery 는 28 맥락이며 학습 근거로 쓰지 않음) / 섹션 5 — 물류창고 사례: 74행 예외·성과 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 을 f25 로 정정(발표 2025-07-01 요약은 미래형 'will improve', 본문 '이동 시간 10%', 블로그 2025-08-11 '배치 효율 10%', 비교 기간·분모 미공개, [추정] 벤더 주장 유지). DeepFleet 오프라인 예측 평가 조건(7개 층·7일·60초, f23)과 CDE 3.40%(f24)는 Amazon 자체 기술보고서라 [추정] 벤더 주장으로; 의견 f26. 기존 ref-1053 근거 [사실] 문장(모델 구성 서술)은 보고서 자체 내용 서술이라 유지하되 성능 수치는 [추정]으로 다룬다(기준 엇갈림 표시). 병원 사례: 표·본문에 평가 조건(BIDMC 4개 층·168 층-일·12시간, f27), 확정 요청 가중치 1(f28, 제약 칸), 거절 0건 동률(f29), 대기 시간 수치(f30, 예외·성과 칸 '꼬리 지연 개선이 가장 컸다' 를 수치로 보강). 제조 공장: 국내 연구 강민교·김인철(f38·f39)을 시뮬레이션 연구로만 추가(실제 배치 사례 아님). 오르카(f40)는 학습 요소가 확인되지 않은 통합 제어 발표라 사례가 아니라 경계 설명 한 문장으로(f41). 기타: 91% 가 시험 표본 100개 기준임(f32) / 섹션 6(분리 2026-09-30-area46-s6) — '학습 기반 경로·교통 관리' 에 RL-RH-PP(f12~f14)와 SJRL(f20~f22, SILLM 공동 저자라 독립 재현 아님) 추가, 실패·복귀 처리 소절에 LSMART 대체 정책 호출 비율(f15)·LRGW/PIBT 지도별 최고(f16), 고전 대조군 PUSH 의 예산·폴백 조건(f17·f18)은 대조 설명으로만(f19); 의견 f31·f44. 첫 문장 '같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고' 는 f6·f13 처럼 지도·밀도별로 우열이 갈린다는 점으로 보강 / 섹션 7(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 평가 Cities-tiles(f1)·통신 미분리 한계(f2). League of Robot Runners 행: 기존 SILLM 2023 비교에 LoRR 2026 평가 구성(f3)과 최종 결과(f4)를 요약·연결만 추가(주 위치는 27·54·25 영역, 다음 실행 후보); 의견 f5. '기존 위키는 SILLM 비교만 소개' 류 서술은 쓰지 않음(기존 자료: ref-603 testing-formal-verification-and-benchmarking.md 115행, ref-191, ref-1306, standards/index.md 140·182행). SILLM 공식 구현 행 추가(f9·f10, 출처는 공식 DiligentPanda 저장소 ref-1638 — 메모의 wuwen-T 미러는 쓰지 않음). ISO 13381-1 행 서지 보정(f33) / 섹션 8(분리 2026-09-30-area46-s8) — SILLM 항목(대상 문장 '…최고 탐색 기반 기준선보다 16.0% 높았고…')은 삭제하지 않고 지도별 예외를 덧붙임: 대형 지도 6종 중 3종(Sortation·Warehouse·Random-1)에서 WPPL 이 높음과 단계당 0.349초 대 4.143초(f6), 16.0% 는 지도별 비율 평균으로 읽힌다는 해석은 [추정](f7), 지도별 훈련 12시간 미만·자원(f8); 의견 f11. Garces 외 항목의 '구체 수치는 초록에 없다' 를 본문 수치로 정정(f27~f30). SPO 항목 '학술지 게재 연도 미확인' → Management Science 68(1):9–26, 2022-01(f42). RL-RH-PP(f12~f14)·SJRL(f20~f22) 새 항목, PUSH(f17·f18)는 고전 대조 자료로 표시. Pookkuttath 항목 91% 표본 수(f32) / 섹션 9 — 상위 업무 시스템 행에 확정 요청 인계 경계(f36 fleet_name 문자열·배열, f37 의견), 로봇 자체 지능·제어 행에 SoC 물리 모델 추정은 28·제조사 쪽(f34·f35), 오르카 같은 WCS 통합 제어는 20·61 쪽 경계(f41). 158행 '경계는 아직 정하지 않았으며' 는 f37 의견으로 부분 보강하되 열린 질문 유지 / 섹션 11(분리 2026-09-30-area46-s11) — 해결 제안 없음. 부분 근거: oq-220(f43: 제3자 실측 없음, 근거 종류 구분), oq-221(f32·f33·f34·f35: 출력 종류만 확인, 공통 데이터 계약·모델 소유권 미확인), oq-222(f15·f16·f18·f28·f31: 가중치 조정과 대체 정책 호출은 확인, 공통 분포 이동 임계값 없음), oq-223(f36·f37: 의견 수준 경계), oq-224(f38·f39 국내 시뮬레이션 연구, f40 은 학습 성과 아님). 관련 근거: oq-058(f6·f13·f21, 벤치마크→실처리량 전이는 여전히 미확인). 분리 페이지 s11 의 질문 5개에 oq-220~oq-224 id 를 붙여 표기. 새 질문 3건 / 기존 내용 확인(새 finding 으로 넣지 않음): SILLM WPPL 비교의 회전 제거·LNS 40,000회 제한(메모 F09, 2026-10-10-area27-s8.md 42행), SILLM 실물 10대·가상 100대(s8 기존), LSMART 600초×10회·실패 정책 개념(2026-10-10-area27-s8.md 43행), CJ대한통운 iFlex 주문 유형별 수요 예측(메모 V05, 본문 5절 78행·9절 149행, ref-1063), DeepFleet 네 구조(s6·s8, ref-1053), Poskart 외 조정 결정계수 0.9629·0.9694·±0.1% 이내 약 50%·MiR100(s6·s8, ref-1058, 독립 검증 재확인), 현대차 5일·90%(5절, ref-1059 파이낸셜뉴스 — 1차 자료 미확인이라 [추정] 벤더 주장 유지), fleet_name 필드 자체(2026-09-29-area09-s7.md 40행) / 후속 정리 필요(대상 페이지 밖, 이번에 고치지 않음): docs/categories/ai-and-learning/index.md 107행 '로봇 이동 효율을 10% 높였다고 주장한다' 를 f25 로, 같은 행 Garces 요약에 f30 수치; docs/categories/site-type-applications/warehouse.md 107행 'Amazon 은 2025년 7월 발표(페이지에 발행일 표기 없음, 검색 결과 기준)' → 페이지 메타 2025-07-01 확인(ref-916); 다음 실행 후보: 27. 다중 로봇 경로·교통 관리 — MAPF·54. 시험·형식 검증·벤치마크·25. 작업 배정 — MRTA(f3·f4 LoRR 2026, f12~f22), 63. 병원·의료(f27~f30), 28. 공용 자원·충전·에너지 최적화(f34) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 학습 기반 배정·경로 정책과 고전 탐색 방법을 같은 실행 모델·지도·계획 예산·실패 처리(대체 정책) 조건으로 다시 돌려 학습의 순이득을 재현한 공개 자료가 있는가? (관련 기존 질문: oq-220, oq-058) | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f44 | 종류: 일반
- 예측 요청의 가중치를 낮추는 것으로 충분한 경우와 실행 중인 계획을 중단·교체하거나 고전 정책으로 돌아가야 하는 경우를 누가 어떤 지표로 구분하는가? (관련 기존 질문: oq-222) | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f31 | 종류: 일반
- 배터리 SoC 변화 추정·현재 이상 클래스·고장 예지 출력을 플릿 일정에 넘길 때 값의 유효기간·불확실성·책임 주체를 어떻게 표현하는가? (관련 기존 질문: oq-221) | 관련 영역: 46. 예측·학습 기반 최적화, 28. 공용 자원·충전·에너지 최적화 | 근거: f35 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 20 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 8건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-06/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f7: SILLM 초록 16.0% 의 계산 방식은 논문에 명시되지 않아 Table III 지도별 비율 평균(재계산 16.05%)과 일치한다는 해석만 [추정]으로 둠
    - f3·f4: LoRR web_resource 고정 커밋(9d5e337)의 커밋 날짜와 최종 수상팀 제출 코드의 학습 사용 여부는 확인하지 못함(published null)
    - f9·f10: SILLM 공식 저장소 README·예시 YAML 만 읽었고 코드를 실행해 논문 결과를 재현하지 않음. dynamic_guidance 브랜치 내용은 보지 않음
    - f23·f24·f25: DeepFleet 은 Amazon 자체 기술보고서·회사 발표만 근거라 [추정] 벤더 주장. 10% 의 비교 기간·대상 층·분모·개입 대조와 제3자 확인은 없음
    - f36: fleet_name 배열 허용의 도입 버전(rmf_api_msgs 0.7.0, CHANGELOG 2026-09-18)은 독립 검증 결과를 따랐고 이번 변환에서 CHANGELOG 를 다시 열지 않음. 스키마 본문(main)은 확인
    - f42: SPO 학술지 서지는 Crossref 메타데이터로 확인했고 학술지 본문은 열지 않음
    - f33: ISO 13381-1:2025 규범 본문(유료)은 열지 않아 조항 내용과 위키 시사점의 직접 대응은 미확인
    - f40: 오르카에서 실제 학습되는 모델·정책과 그 성능 비교·운영 분모는 미공개. 현대차 예지정비 5일·90%(ref-1059)의 1차 자료도 확인하지 못함
    - oq-220~oq-224 는 모두 부분 근거만 얻어 해결 제안하지 않음. 국내 실물 창고·병원에서 학습 기반 배정·경로를 고전 방법과 대조 실측한 자료, 이종 플릿 고장 데이터 계약·모델 소유권 합의, 공통 분포 이동 복귀 임계값은 찾지 못함
- 범위 경계 위반 의심:
    - f3·f4·f5: LoRR 2026 대회 평가 구성·결과는 27. 다중 로봇 경로·교통 관리 — MAPF, 54. 시험·형식 검증·벤치마크, 25. 작업 배정 — MRTA 가 주 위치이므로 이 영역에는 요약·연결만 둠
    - f17·f18·f19(PUSH), f34(rmf_battery), f40·f41(오르카): 학습과 무관한 고전 알고리즘·물리 모델·통합 제어이므로 이 영역에서는 대조·경계 설명으로만 쓰고 학습 성과 근거로 쓰지 않음(각각 27, 28, 20·61 영역 맥락)
    - f36·f37: 작업 요청 스키마와 상위 수요예측 경계는 23. 업무 시스템 연동과 겹치며, 이 영역에는 예측 요청과 확정 요청의 인계 경계로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 8건/15(ref-1637~ref-1644, 예약 구간 ref-1637~ref-1666 안), 재사용 12건(ref-1056·ref-199·ref-604·ref-1053·ref-916·ref-1054·ref-1062·ref-1057·ref-1060·ref-125·ref-1063·ref-1061). 출처 매핑(독립 검증 결과 기준): 메모 n1→ref-1056, n2+n3→ref-1637(한 출처로 묶음, raw 경로), n4→ref-199, n5→ref-1638(메모의 wuwen-T 저장소는 미러라 공식 DiligentPanda/Scalable-Imitation-Learning-for-LMAPF 로 교체), n6→ref-604, n7→ref-1639(JAIR DOI 10.1613/jair.1.20611, 2026-03-24), n8→ref-1640, n9→ref-1641, n10→ref-1053, n11→ref-916(발행 2025-07-01), n12→ref-1062, n13→ref-1060(서지 보정), n14→ref-1057(Europe PMC 전문), n15→ref-1642, n16→ref-1063, n17→ref-1643, n18→ref-1644(벤더 문서), n19→ref-125. 추가 재사용: ref-1054(10% 표현 대조), ref-1061(SPO 게재 서지, Crossref). 검증 반영: F08 을 Warehouse 한 지도에서 6개 지도 중 3개(Sortation·Warehouse·Random-1) WPPL 우세로 확장하고 계획 시간 병기(f6), 16.0% 해석은 [추정](f7); F09(LNS 40,000회)는 2026-10-10-area27-s8 중복이라 제외; V01 은 JAIR 표 값이라 [사실]로 두고 N100·N120 의 RL-RH-PP 우세를 병기(f13); V02·V03 은 Amazon 자체 기술보고서라 [추정]·벤더 주장(f23·f24); V04 는 '높였다'가 아니라 미래형·지표 차이로 정정(f25); A11 Garces 를 본문 정량 결과로 정정(f27~f30); V05 는 기존 내용과 완전 중복이라 제외(ref-1063 은 의견 f37 참고로만); PUSH·rmf_battery·오르카는 학습과 무관해 대조·경계 설명으로만(f19·f35·f41); U16 SPO 게재 서지 확인(f42); U09 Poskart 수치는 재확인만 하고 새 finding 없음; U15 현대차 5일·90% 는 [추정] 유지. LoRR 2026(F03~F07)은 f3~f5 로 요약해 연결만. 교차 확인 0건: 모든 [사실] finding 이 단일 출처이거나 같은 연구팀·같은 회사 자료(SILLM 논문·저장소, SILLM·SJRL·LSMART 공동 저자, Amazon 발표·블로그·보고서)라 독립이 아님 — 신뢰도 medium 이하. 열린 질문: oq-220~oq-224 는 docs/open-questions.md 242~246행 문구와 분리 페이지 s11 질문이 같음을 확인. 해결 제안 없음, 부분 근거만. 메모의 새 질문 3건은 oq-220·oq-058, oq-222, oq-221 과 겹치는 부분이 있으나 같은 질문은 아니어서(재현 조건, 판단 주체, 유효기간·책임) 관련 기존 질문을 밝혀 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호와 고정 위키 커밋 행 번호는 쓰지 않고 원문 절·표와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음. finding 44건(사실 29, 추정 6, 의견 9).
