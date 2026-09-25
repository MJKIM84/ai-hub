---
title: "단계 5. 검증 방법과 가설 판정"
type: track-stage
track: floorplan-recognition
stage: 5
related_areas: [23, 21, 22, 6, 27]
tags: [인식 정확도, 지도 품질, 모델링 시간, 가설 판정, 평가 지표]
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-718, ref-719, ref-067, ref-063, ref-065, ref-070, ref-720, ref-727, ref-729, ref-628, ref-728, ref-153, ref-721, ref-723, ref-724, ref-725, ref-726, ref-722, ref-031]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › 중점 연구 트랙 › [건축 도면 자동 인식](index.md) › 단계 5. 검증 방법과 가설 판정

# 단계 5. 검증 방법과 가설 판정

> 단계 상태: 진행 중 · 열린 질문: 9건 · 답한 질문: 1건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 인식·지도 품질과 현장 모델링 시간 단축 효과를 어떻게 측정하고, 가설 1~3을 어떻게 판정하는가.

위 문장은 트랙 정의의 "밝힐 것"이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 조사 결과는 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)과 [공간 그래프 스키마 초안](space-graph-schema-draft.md)으로 이어진다.

## 2. 질문 목록

이 단계의 질문은 구축자가 이 단계의 밝힐 것에서 정한 시작 질문 3개(q5-01~q5-03)와, 앞 단계와 이번 실행에서 생긴 후속 질문이다. [가정] 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커 또는 주제 페이지 링크를 적는다. 제기 근거 칸에는 finding id(실행 id 병기) 또는 "사용자"만 쓴다.

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q5-01 | 요소별 인식 정확도(검출·위치 오차)와 지도 품질(주행 성공률, 경로 차이)을 어떤 지표로 측정하는가? | 답함 | 사용자 | 2026-09-25-80 | [답](#q5-01) |
| q5-02 | 현장 모델링 시간 단축 효과를 어떤 기준(수작업 대비 소요 시간, 수정 횟수)으로 측정하는가? | 열림 | 사용자 | | |
| q5-03 | 가설 1~3은 단계 1~4의 결과로 어떻게 판정되는가? | 열림 | 사용자 | | |
| q5-04 | PAN-Robots 과제가 보고한 설치 기간 6개월→2개월의 비교 조건(대상 공장 규모, 기준 시스템, 단계별 소요 시간)을 과제 결과 보고서·산출물로 확인해, 도면 기반 자동 생성의 시간 단축 효과를 판정할 기준 자료로 쓸 수 있는가? (q1-04 에서 파생) | 열림 | f2, 실행 2026-09-25-22 | | |
| q5-05 | 요구–제공 능력 매칭으로 만든 로봇별 통행 가능 판정이 실제 주행에서 틀리는 경우(통과 가능 판정 후 실패, 불가 판정의 과잉 제한)를 시뮬레이션·실기체 시험으로 어떻게 측정하고 임계값을 보정하는가? (q3-03 에서 파생) | 열림 | f21, 실행 2026-09-25-65 | | |
| q5-06 | 도면 기반으로 만든 시뮬레이션 월드로 예측한 처리량·혼잡 지점을 실제 현장 측정과 비교해, 가설 3 의 '시뮬레이션 초기값으로 쓸 수 있다'를 판정하는 지표와 허용 오차는 무엇인가? (q3-04 에서 파생) | 열림 | f14, 실행 2026-09-25-70 | | |
| q5-07 | 도면–현장 차이 탐지 방법(재측량 대조, 다중 세션 변화 탐지)의 성능을 물류 현장에서 놓친 변화·잘못 탐지한 변화와 지도 갱신 지연으로 측정하려면 어떤 지표와 시험 절차가 필요한가? (q4-02 에서 파생) | 열림 | f8, 실행 2026-09-25-75 | | |
| q5-08 | 지도 판을 교체한 뒤 재검증 시험(목적지 대응점 잔차, 영향받은 차선 주행, 구역 규칙 확인)의 합격 기준과 판 교체에 드는 중단 시간·재검증 공수를 어떤 지표로 측정하는가? (q4-04 에서 파생) | 열림 | f19, 실행 2026-09-25-78 | | |
| q5-09 | 요소 검출 F1·위치 오차·목적지 잔차·도착 성공률 같은 지도 품질 지표의 합격 임계값을 이미지 픽셀 기준이 아니라 물류 로봇의 노드 허용 편차(VDA 5050 allowedDeviationXY)·문 폭 대비 차체 여유 같은 운영 허용치에서 어떻게 도출하는가? (q5-01 에서 파생) (관련: q4-12, q5-08) | 열림 | f20, 실행 2026-09-25-80 | | |
| q5-10 | 도면 기반 지도와 기준 지도(측량 또는 현장 SLAM 지도)에서 같은 출발–도착 쌍으로 경로 차이(길이 비율, 지나는 공간·문·승강기 순서)를 재는 시험 세트를 물류센터에서 어떻게 구성하는가(쌍 선택, 층간 이동 포함, 제조사별 반복)? (q5-01 에서 파생) | 열림 | f21, 실행 2026-09-25-80 | | |

## 3. 조사 결과

### q5-01 요소별 인식 정확도와 지도 품질을 재는 지표 {#q5-01}

확인한 자료를 이 위키가 묶으면, 요소별 인식 정확도와 지도 품질은 (1) 요소 인식, (2) 공간 구조·그래프, (3) 지도·정렬과 주행의 세 층으로 나누어 재는 구성이 근거가 가장 많은 것으로 보인다. 세 층을 한 번에 제시한 단일 출처는 찾지 못했으며, 이는 이 위키의 종합이다. [추정][^ref-718][^ref-719][^ref-067][^ref-063][^ref-070][^ref-720][^ref-721][^ref-725][^ref-726][^ref-628][^ref-153]

이번 실행은 일반 웹 페이지 열람이 막힌 환경에서 진행되어 지표 정의 대부분은 검색 요약 기준이며, 교차 확인된 것은 파놉틱 품질과 SPL 정의 두 가지다. 확인한 인식 지표는 주거 평면도와 이미지 픽셀 기준이고, 물류센터 도면에 적용한 평가는 찾지 못했다.

#### 요소 인식 지표

- Floor-SP(2019-08)는 3D 스캔에서 재구성한 평면도를 모서리·방·각도 세 수준의 정밀도(precision)·재현율(recall)·F1 점수로 평가한다. 모서리는 정답 모서리와 10픽셀 안에 있으면, 각도는 모서리가 맞고 정답 각도와 5° 미만 차이면, 방은 정답과의 교집합 대 합집합 비(Intersection over Union, IoU)가 임계값을 넘으면 맞은 것으로 본다. [사실][^ref-718] MonteFloor(2021-03)도 방·모서리·각도 지표로 대규모 평면도 재구성을 평가한다. [사실][^ref-719]
- FloorPlanCAD(2021-05) 계열의 파놉틱 심볼 스포팅은 파놉틱 품질(Panoptic Quality, PQ)을 분할 품질(SQ, 참 양성의 평균 IoU)과 인식 품질(RQ, TP/(TP+0.5FP+0.5FN))의 곱으로 정의하고, 의미 라벨이 같고 IoU 가 0.5 를 넘으면 예측 심볼을 정답과 매칭한다(벡터 CAD 선 요소 단위). [사실][^ref-067]
- CubiCasa5K 논문(2019-04)은 방·아이콘(문·창문 포함)의 클래스별 IoU 와 정확도를 보고하며, 분할 원시 결과보다 다각형화한 인스턴스 기반 점수가 낮은 이유로 벽·아이콘 접합점을 놓치거나 잘못 위치시키면 분할 품질과 상관없이 다각형을 만들 수 없다는 점을 든다. [사실][^ref-063]
- Raster-to-Vector(FloorplanTransformation) 공식 README(2017)는 저자들의 방법이 약 90% 의 정밀도와 재현율을 달성했다고 요소 유형별 구분 없이 적는다(저자 보고). [사실][^ref-065]

#### 공간 구조·그래프 지표

- Raster-to-Graph 공식 README(2024)는 구조 그래프 예측 성능을 정밀도·재현율로 계산한 엣지 F1 로 보고하며, 논문 값 96.1 과 저장소 값 96.2 의 차이는 정밀도·재현율을 반올림한 시점의 차이라고 적는다. [사실][^ref-070]
- SSIG 공식 저장소 README(ICCV Workshops 2023)는 평면도 구조 유사도를 IoU 와 방 연결 그래프의 그래프 편집 거리(Graph Edit Distance, GED)의 가중합으로 정의하고, 시험한 평면도 세 쌍 조합의 38% 넘게에서 IoU 와 GED 가 매긴 순위가 서로 반대였다고 보고한다. [사실][^ref-720]

#### 지도 품질 지표

- Filatov 외(2017-08)는 2D SLAM 지도 비교 지표로 점유 셀 비율, 모서리 수, 닫힌 영역 수를 제시해 겹침·번짐·어긋남 같은 지도 오류를 드러내게 했다. 다만 이 지표는 같은 데이터 시퀀스에서 나온 여러 SLAM 결과를 서로 비교할 때 쓰는 상대 지표이며, 기준 지도 없이 지도의 절대 품질을 판정하는 지표가 아니다. 세 지표 이름은 이 논문을 인용한 문헌의 요약 기준이다. [사실][^ref-727]
- SLABIM 공식 README 는 설계 BIM 과 SLAM 센서 데이터를 묶은 데이터셋으로 라이다–BIM 전역 정합, BIM 위 로봇 자세 추적, 의미 지도 작성(바닥·벽·문·기둥) 세 과제를 검증하며, 라이다 스캔·지도의 BIM 좌표 기준 정답 자세를 제공한다(README 기준 ICRA 2025 채택 2025-01-28, 대학 건물 대상). [사실][^ref-729]
- 연계 대상: Lee·Woo·Shin(IJPEM, 2026)은 2D 건축 CAD 도면으로 자동 생성한 점유 격자 지도의 품질을 그 지도 위 위치추정의 이동·회전 RMSE 와 궤적 일관성 오차로 SLAM 지도와 비교해 평가했다. [사실][^ref-628]
- 연계 대상: PRM-RL(Francis 외, 2019-02)은 건물 평면도로 만든 경로망과 같은 건물의 SLAM 지도로 만든 경로망에서 장거리 실내 주행을 평가해, SLAM 지도 경로망이 시뮬레이션과 실제 로봇 성능 차이를 좁힌다고 보고했다(저자 보고). [사실][^ref-728]
- Open-RMF 플릿 어댑터 튜토리얼은 로봇 지도와 RMF 좌표의 변환을 층마다 대응 경유점(최소 4쌍 권장)으로 추정하고 층별 평균제곱오차(MSE)를 기록해 정렬 정확도를 확인하게 한다(발행일 미확인, 2026-09-25 확인). [사실][^ref-153]

#### 주행 성능 시험 표준과 지표

아래 시험과 지표는 로봇이 실제로 주행하는 성능을 재는 것이며, 분류 원문 9장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이다. ROP 는 이 시험을 직접 하기보다 제조사·통합자의 시험 결과를 받아 쓰는 쪽이다(아래 경계 문장).

- 연계 대상: ISO 18646-2:2024(2판, 2019 판을 기술 개정, 2024-01)는 이동 서비스 로봇의 주행 성능을 자세 정확도·반복성, 장애물 감지·회피, 경로 이탈, 좁은 통로 통과, 지도 작성 정확도로 측정하며, 실내 환경을 다루고 안전 요구사항 검증에는 쓰지 않는다. 시험 절차 세부는 미확인이다. [사실][^ref-721]
- 연계 대상: ASTM F3244(2021 개정)은 무인 지상 차량(A-UGV)이 여유가 제한된 정의 영역을 지나는 능력을 시험하며, 시험 영역을 물리 경계·가상 경계·바닥 표시 세 방식으로 만들고 시험에 쓸 장애 유형으로 장애물과 통신 장애 두 가지를 둔다. [사실][^ref-723]
- 연계 대상: NIST 의 Bostelman·Hong·Cheok(IEEE TePRA 2015)은 AGV 가 정해진 경로를 얼마나 잘 따르는지를 다중 카메라 기준값(ground truth) 측정과 지령 데이터를 비교해 평가하는 시험 절차와 지표를 제시하고 ASTM F45 에 시험법으로 권고했다. [사실][^ref-724]
- Anderson 외(2018-07)의 작업반 권고는 내비게이션 평가의 주 지표로 경로 길이 가중 성공률(Success weighted by Path Length, SPL)을 두고, 이를 에피소드마다 성공 여부에 최단 경로 길이/max(실제 경로 길이, 최단 경로 길이)를 곱한 평균으로 정의한다. [사실][^ref-725]
- 연계 대상: Arena-Bench(2022-06)는 ROS 내비게이션 방식을 성공률(충돌 2회 미만이고 시간 초과 없음), 충돌 수, 도착 시간, 경로 길이, 장애물 이격 거리, 가속도 변화·거칠기 같은 지표로 안전·강건성·효율·매끄러움을 나눠 비교한다. [사실][^ref-726]
- 국내 정부 R&D 보고서 '이동/조작/HRI/통신성능 등 서비스로봇 성능평가 및 표준화 기술개발'은 정형·비정형 실내외 환경의 위치인식·지도작성·주행경로 성능평가 기술과 실내 정형 환경 기반 주행 성능 평가기법·성능 지표 개발을 핵심 내용으로 둔다. 발행일과 세부 지표는 미확인이다. [사실][^ref-722]
- 연계 대상: 장애물 회피·좁은 통로 통과·경로 추종 같은 주행 시험 자체는 로봇·제조사 쪽 성능이므로, ROP 쪽 지표는 도면 인식·공간 그래프·좌표 정렬 품질과 도착 인정 판정에 한정하고 주행 시험 결과는 제조사·통합자 시험(ISO 18646-2, ASTM F3244 식)을 받아 쓰는 경계가 될 것으로 보인다. [추정][^ref-721][^ref-723][^ref-724][^ref-031]

#### 운영 허용치와 임계값

- VDA 5050 3.0.0 은 로봇이 노드를 지난 것으로 보려면 제어점이 노드의 허용 편차(allowedDeviationXY, 타원) 안에, 방향이 allowedDeviationTheta 안에 있어야 한다고 규정한다(명세 3.0.0, 발행일 미확인 — [열린 질문](../../open-questions.md) oq-005). [사실][^ref-031]
- 확인한 인식 지표는 모서리 10픽셀·IoU 0.5 같은 이미지 기준 임계값을 쓰므로, 로봇 지도 품질 판정에 쓰려면 축척으로 미터 단위로 바꾸고 임계값은 VDA 5050 노드 허용 편차 같은 운영 허용치에 맞춰 정해야 할 것으로 보인다. 픽셀 임계값을 운영 허용치로 옮긴 출처는 찾지 못했다. [추정][^ref-718][^ref-067][^ref-031][^ref-153]

#### 경로 차이의 정의

- '경로 차이'는 같은 출발–도착 쌍에 대해 도면 기반 지도와 기준 지도(측량 또는 현장 SLAM 지도)에서 구한 경로를 비교해, 길이 비율(SPL 식)과 지나는 공간·문·승강기의 순서가 같은지(그래프 편집 거리 식)를 함께 재는 방식으로 정의할 수 있을 것으로 보인다. PRM-RL 은 두 경로망을 각각 평가했을 뿐 같은 쌍의 경로 차이 지표는 확인하지 못했다. [추정][^ref-725][^ref-720][^ref-728]

#### 세 층 지표 구성 (종합)

아래 표는 검증된 발견 사항으로 이 위키가 구성한 종합이며 출처의 표를 옮긴 것이 아니다. 3층의 주행 지표는 제조사·통합자의 시험 결과를 받아 쓰는 연계 대상으로 구분했다. [추정][^ref-718][^ref-067][^ref-070][^ref-720][^ref-721][^ref-725][^ref-726][^ref-628][^ref-153][^ref-031]

| 층 | 무엇을 재는가 | 지표 후보 | 측정 주체 |
|---|---|---|---|
| 1. 요소 인식 | 벽·문·엘리베이터·계단·충전 위치의 검출과 위치 | 클래스별 정밀도·재현율·F1(IoU 0.5 초과 또는 거리 임계값으로 매칭), 벡터 CAD 는 파놉틱 품질, 미터 단위 모서리·문 중심 거리와 각도 오차 | ROP 쪽(도면 인식 품질) |
| 2. 구조·그래프 | 방 분할과 공간 연결 | 방 IoU, 공간 그래프의 엣지 F1·그래프 편집 거리(문·승강기 연결 포함) | ROP 쪽 |
| 3. 지도·정렬 | 생성 지도와 기준·제조사 지도의 대응 | 기준 지도 대비 지도 정확도, 목적지 대응점 잔차, 경로 차이, 도착 인정 판정 | ROP 쪽 |
| 3. 주행 | 그 지도로 실제 주행한 결과 | 주행 성공률, SPL, 경로 이탈, 좁은 통로 통과, 그 지도 위 위치추정 오차 | 연계 대상(제조사·통합자 시험 결과 수용) |

```mermaid
flowchart LR
  plan["도면 인식 결과"] --> elem["요소 인식 지표"]
  plan --> graph["구조·그래프 지표"]
  elem --> maprop["지도·정렬 지표(ROP)"]
  graph --> maprop
  drive["주행 시험 결과(연계 대상: 제조사·통합자)"] --> accept["도착 인정 판정(ROP)"]
  maprop --> accept
```

#### 설명용 시나리오: ‘3층 출하 대기장’

다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았다.

**물류 흐름 단계:** 출하

**시나리오:** 도면에서 얻은 ‘3층 출하 대기장’ 목적지를 제조사가 다른 로봇들의 지도로 옮기고 도착 인정 기준을 확인

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 해당 없음 |
| 제약 | 인식 지표의 임계값은 이미지 픽셀 기준이라, 대기장 목적지 좌표의 합격 여부는 미터 단위로 바꾼 뒤 노드 허용 편차 같은 운영 허용치로 정해야 할 것으로 보인다. [추정][^ref-718][^ref-067][^ref-031][^ref-153] |
| 완료·인계 | VDA 5050 은 노드 통과를 제어점과 방향이 노드 허용 편차 안에 있는지로 본다. [사실][^ref-031] 이 가정 사례에서는 대기장 목적지 좌표를 제조사별 지도로 옮긴 뒤 목적지 대응점 잔차가 노드 허용 편차 안에 드는지와 각 제조사 로봇의 실제 도착 성공률을 함께 재야 지도 품질이 SCM 쪽 도착 인정 기준으로 이어질 것으로 보인다. [추정][^ref-031][^ref-153] |
| 예외·성과 | 해당 없음(잔차가 허용 편차를 넘을 때의 보정과 합격 기준은 후속 질문 q4-12 로 남아 있다) |

#### 근거 공백

- 이번 검색 범위(한국어 3회 포함 17회)에서는 물류센터 평면도 인식 결과와 그 지도로 한 로봇 주행 품질을 함께 평가한 벤치마크나 국내 사례를 찾지 못했다(부재 확인 아님). 확인한 BIM–SLAM 평가는 대학 건물, 평면도 주행 평가는 사무 건물 대상이다. [추정][^ref-722][^ref-729][^ref-728]

## 4. 결론과 남은 불확실성

**결론**

- 요소 인식은 정밀도·재현율·F1(IoU 또는 거리 임계값 매칭)과 벡터 CAD 의 파놉틱 품질로, 공간 구조는 엣지 F1 과 IoU·그래프 편집 거리로 재는 선례가 있다. [사실][^ref-718][^ref-067][^ref-070][^ref-720]
- 지표를 요소 인식·구조·그래프·지도·정렬과 주행의 세 층으로 두고, 주행 지표는 제조사·통합자 시험 결과를 받아 쓰는 연계 대상으로 나누는 구성이 확인한 근거와 가장 잘 맞는 것으로 보인다. [추정][^ref-718][^ref-720][^ref-721][^ref-725][^ref-031]
- 픽셀 기준 인식 임계값은 미터 단위로 바꾸고 노드 허용 편차 같은 운영 허용치에 맞춰야 할 것으로 보인다. [추정][^ref-718][^ref-067][^ref-031][^ref-153]

**남은 불확실성**

- 지표 정의마다 단일 출처이며, 교차 확인된 것은 파놉틱 품질과 SPL 정의뿐이다. Floor-SP 와 MonteFloor 지표 문구의 출처는 검색 요약에서 구분되지 않았다.
- ISO 18646-2:2024 의 지도 작성 정확도 시험 절차와 KS 부합화 여부는 미확인이다(원문 미열람).
- Filatov 외의 세 지표 이름은 인용 문헌 요약 기준이고, PRM-RL 의 성공률 수치는 요약마다 달라 싣지 않았다.
- 국내 R&D 보고서(ref-722)의 발행일과 세부 지표는 미확인이다.
- 세 층 구성·임계값 변환·경로 차이 정의·‘3층 출하 대기장’ 사례는 이 위키의 종합이며, 확인한 인식 지표는 주거 평면도·이미지 픽셀 기준이다.
- 현장 모델링 시간 단축 측정(q5-02)과 가설 판정(q5-03)은 아직 조사하지 않았다.
- 공간 그래프 스키마 초안은 바꾸지 않았다(v1.2 유지). 평가 지표는 스키마의 개념·관계가 아니라 검증 방법이어서 변경 제안이 없었다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q5-09 | 요소 검출 F1·위치 오차·목적지 잔차·도착 성공률 같은 지도 품질 지표의 합격 임계값을 이미지 픽셀 기준이 아니라 물류 로봇의 노드 허용 편차(VDA 5050 allowedDeviationXY)·문 폭 대비 차체 여유 같은 운영 허용치에서 어떻게 도출하는가? (q5-01 에서 파생) (관련: q4-12, q5-08) | 단계 5. 검증 방법과 가설 판정 | f20 (실행 2026-09-25-80) | 열림 |
| q5-10 | 도면 기반 지도와 기준 지도(측량 또는 현장 SLAM 지도)에서 같은 출발–도착 쌍으로 경로 차이(길이 비율, 지나는 공간·문·승강기 순서)를 재는 시험 세트를 물류센터에서 어떻게 구성하는가(쌍 선택, 층간 이동 포함, 제조사별 반복)? (q5-01 에서 파생) | 단계 5. 검증 방법과 가설 판정 | f21 (실행 2026-09-25-80) | 열림 |

## 6. 완료 조건 충족 현황

충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 평가 지표와 검증 절차가 [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)의 "6. 검증 방법" 절에 실림 | 미충족 | 평가 지표 소절만 실림(실행 2026-09-25-80, 추정 중심), 검증 절차(q5-02) 미조사 | 미충족 · 미승인 |
| 가설 판정표가 [트랙 개요](index.md)의 "3. 가설과 판정 상태"에 실림 | 미충족 | q5-03 미조사 | 미충족 · 미승인 |
| 사용자에게 제안하는 실험 계획이 [실험](experiments.md)에 실림 | 미충족 | 제안된 실험 계획 없음 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(막힌 질문 q5-02·q5-03·q5-04·q5-05·q5-06·q5-07·q5-08 과 이번 새 질문 q5-09·q5-10 이 열림)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 확인된 사실은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안"으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

- [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 인식 결과와 생성한 지도를 시뮬레이션·실기체 주행 시험으로 검증한다. 이번 실행의 주행 시험 표준(ISO 18646-2, ASTM F3244, NIST AGV 시험)과 내비게이션 지표(SPL 등), 세 층 지표를 "6. 대표 접근법과 기술"에 반영하도록 제안했다
- [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 분류 원문 10장의 함께 필요한 영역(시운전). '현장 모델링 시간을 줄이는' 적용처다
- [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 분류 원문 10장의 함께 필요한 영역(시뮬레이션). 생성한 지도를 '시뮬레이션 초기값으로 사용'한다
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 지도 품질 지표(SLABIM 정답 자세, CAD 지도 위치추정 오차, 상대 지표의 한계)와 목적지 잔차를 노드 허용 편차로 판정하는 방법(추정)을 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료"에 반영하도록 제안했다
- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 도면 해석 모델의 평가 지표(모서리·방 정밀도·재현율, 파놉틱 품질, 클래스별 IoU, SSIG)를 "6. 대표 접근법과 기술"에 반영하도록 제안했다(분류 원문 8장 교차 규칙: 도면 해석은 6. 지도·공간·위치 모델에 적용)

## 8. 출처

[^ref-718]: Chen, J., Liu, C., Wu, J., & Furukawa, Y., Floor-SP: Inverse CAD for Floorplans by Sequential Room-wise Shortest Path, 2019-08, https://arxiv.org/abs/1908.06702, 접근일 2026-09-25 (원문 미열람)
[^ref-719]: Stekovic, S., Rad, M., Fraundorfer, F., & Lepetit, V., MonteFloor: Extending MCTS for Reconstructing Accurate Large-Scale Floor Plans, 2021-03, https://arxiv.org/abs/2103.11161, 접근일 2026-09-25 (원문 미열람)
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P., FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-25 (원문 미열람)
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-25 (원문 미열람)
[^ref-065]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y., FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation), 2017, https://github.com/art-programmer/FloorplanTransformation, 접근일 2026-09-25
[^ref-070]: Hu, S. 외, Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer), 2024, https://github.com/SizheHu/Raster-to-Graph, 접근일 2026-09-25
[^ref-720]: van Engelenburg, C. 외 (caspervanengelenburg GitHub), ssig — README (SSIG: A Visually-Guided Graph Edit Distance for Floor Plan Similarity, ICCVW 2023), 2023, https://github.com/caspervanengelenburg/ssig, 접근일 2026-09-25
[^ref-727]: Filatov, A. 외, 2D SLAM Quality Evaluation Methods, 2017-08, https://arxiv.org/abs/1708.02354, 접근일 2026-09-25 (원문 미열람)
[^ref-729]: HKUST Aerial Robotics Group (HKUST-Aerial-Robotics GitHub), SLABIM — README (SLABIM: A SLAM-BIM Coupled Dataset in HKUST Main Building), 2025-01-28, https://github.com/HKUST-Aerial-Robotics/SLABIM, 접근일 2026-09-25
[^ref-628]: Lee, H.-C., Woo, H.-M., & Shin, S. (International Journal of Precision Engineering and Manufacturing), Digital Twin-based Sensor-Free Virtual Mapping for Autonomous Mobile Robot Localization, 2026, https://link.springer.com/article/10.1007/s12541-026-01598-2, 접근일 2026-09-25 (원문 미열람)
[^ref-728]: Francis, A. 외, Long-Range Indoor Navigation with PRM-RL, 2019-02, https://arxiv.org/abs/1902.09458, 접근일 2026-09-25 (원문 미열람)
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25 (원문 미열람)
[^ref-721]: ISO, ISO 18646-2:2024 - Robotics — Performance criteria and related test methods for service robots — Part 2: Navigation, 2024-01, https://www.iso.org/standard/82643.html, 접근일 2026-09-25 (원문 미열람)
[^ref-723]: ASTM International, F3244 Standard Test Method for Navigation: Defined Area, 2021, https://store.astm.org/f3244-21.html, 접근일 2026-09-25 (원문 미열람)
[^ref-724]: Bostelman, R. V., Hong, T. H., & Cheok, G. S. (NIST), Navigation Performance Evaluation for Automated Guided Vehicles, 2015, https://www.nist.gov/publications/navigation-performance-evaluation-automated-guided-vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-725]: Anderson, P. 외, On Evaluation of Embodied Navigation Agents, 2018-07, https://arxiv.org/abs/1807.06757, 접근일 2026-09-25 (원문 미열람)
[^ref-726]: Kästner, L. 외, Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-25 (원문 미열람)
[^ref-722]: KISTI ScienceON(정부 R&D 보고서), 이동/조작/HRI/통신성능 등 서비스로봇 성능평가 및 표준화 기술개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO201800040065, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

## 9. 이력

실행 id `build-2026-09-25`는 확장 아이디어 편입 때의 트랙 시드 생성을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 초안 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-80 | q5-01 | q5-09, q5-10 | 없음(v1.2 유지) | 2 |
| 2026-09-25 | build-2026-09-25(트랙 시드, 파이프라인 실행 아님) | 없음 | 시드 q5-01~q5-03(3건, [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [공간 그래프 스키마 초안](space-graph-schema-draft.md)에서 생성) | 1 |
