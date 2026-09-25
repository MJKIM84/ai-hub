# 스토리텔러 산출 2026-09-25-10

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md | draft | 3~11절 신규 작성(소요대수 산정 모델, 작업대·충전기·승강기 병목, 가상 시나리오, ROP 경계, 열린 질문 4건). 2차 수정: 8절 각주 보강, 10절 순위 문장 삭제·MRTA 범위 한정, 9절 사실·의견 분리, 11절 문구, sources 에서 ref-107 제외 |
| create | docs/topics/2026/2026-09-25-area03-s8.md | draft | 자동 분리: 3. 처리능력·거점·설비 계획 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 요약 문장 각주에 ref-097·ref-103 추가 |
| create | docs/topics/2026/2026-09-25-area03-s6.md | draft | 자동 분리: 3. 처리능력·거점·설비 계획 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 드리프트 문장 삭제, 태그 없는 주장 3문장에 태그·각주 |
| create | docs/topics/2026/2026-09-25-area03-s7.md | draft | 자동 분리: 3. 처리능력·거점·설비 계획 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 없음, ref-107 인용 페이지) |
| create | docs/topics/2026/2026-09-25-area03-s11.md | draft | 자동 분리: 3. 처리능력·거점·설비 계획 의 "11. 열린 질문" 절을 옮겼다(2차 수정 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 3. 처리능력·거점·설비 계획 | 영역 심화로 3~11절 초안을 썼다(1차 조건부 승인 수정 13건, 2차 수정 지시 8건 이행) | run 2026-09-25-10
- 홈 최근 업데이트: 2026-09-25 — 3. 처리능력·거점·설비 계획: 3~11절 초안(로봇 소요대수 산정 모델, 작업대·충전기·승강기 병목, ROP 경계, 열린 질문 4건)
- 대분류 최근 업데이트: 2026-09-25 — 3. 처리능력·거점·설비 계획: 영역 심화 초안(대기행렬 모델과 시뮬레이션, 충전 설비, 승강기는 병원·호텔 사례로 한정)
- 세부영역 최근 업데이트: 2026-09-25 — 3. 처리능력·거점·설비 계획: 3~11절 신규 작성, 신뢰도 medium

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 차량 소요대수 산정 | Fleet Sizing | 예상 물동량과 서비스 수준(대기 시간·처리량) 목표를 만족하는 데 필요한 로봇·운반 차량의 최소 대수를 정하는 계획 문제이다. | 3, 13, 16 | ref-100, ref-099 |
| new | 로봇 이동형 풀필먼트 시스템 | Robotic Mobile Fulfillment System (RMFS) | 로봇이 상품을 담은 이동식 선반(pod)을 작업대까지 옮기고 작업자가 그 앞에서 피킹·보충하는 부품-작업자(parts-to-picker) 방식의 자동화 창고 시스템이다. | 3, 13, 16 | ref-096, ref-097 |
| new | 반개방형 대기행렬 네트워크 | Semi-Open Queueing Network (SOQN) | 외부에서 주문이 들어오되 로봇 같은 한정된 자원 수가 고정된 채 순환하는 시스템의 처리량·대기 시간을 해석적으로 추정하는 대기행렬 모델이다. | 3, 16 | ref-097, ref-098 |
| new | 이산 사건 시뮬레이션 | Discrete Event Simulation (DES) | 주문 도착·작업 완료 같은 사건이 일어나는 시점마다 시스템 상태를 갱신해 처리량·대기·가동률을 실험하는 시뮬레이션 방식이다. | 3, 22 | ref-101 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 논문 | medium | https://repub.eur.nl/pub/107376/ |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 논문 | medium | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 |
| ref-099 | Le-Anh, T., & de Koster, M. B. M. | A review of design and control of automated guided vehicle systems | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840 |
| ref-100 | Vis, I. F. A. | Survey of research in the design and control of automated guided vehicle systems | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 오픈소스 문서 | high | https://github.com/merschformann/RAWSim-O |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://doi.org/10.1177/20552076261437181 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 정부·연구기관 | medium | https://cslc.koti.re.kr/ |
| ref-107 | 법제처 국가법령정보센터 | 물류시설의 개발 및 운영에 관한 법률 | 정부·연구기관 | medium | https://www.law.go.kr/LSW/lsInfoP.do?lsId=000091 |
| ref-108 | 이문수, 채준재(로지스틱스연구) | AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 - | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? | 3, 4 | 열림 | — |
| new | — | 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? | 3, 18 | 열림 | — |
| new | — | 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? | 3, 10 | 열림 | — |
| new | — | 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? | 3, 4 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 보충 | 작업 대상 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 피킹 | 작업 대상 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 보충 | 수행 자원 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 피킹 | 수행 자원 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 피킹 | 제약 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 포장 | 제약 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |
| 적치 | 예외·성과 | docs/categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 3. 처리능력·거점·설비 계획 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| RAWSim-O | 오픈소스 | Merschformann, M. (RAWSim-O GitHub) | 3, 22 | ref-101 | https://github.com/merschformann/RAWSim-O |
| 스마트물류센터 인증제 | 평가 프로그램 | 한국교통연구원(인증스마트물류센터) | 3, 4 | ref-106 | https://cslc.koti.re.kr/ |

## 추가 조사 요청

- 1. 한 줄 정의의 '교대 운영' 근거 조사: 교대조별 작업자·로봇·작업대 수를 함께 정하는 처리능력 모델이나 사례. 3·6절에 필요하다(이번 브리프에서 1차 자료 없음).
- 1. 한 줄 정의의 '여러 거점의 자원 배치' 근거 조사: 거점 간 로봇 재배치·공유·임대 결정을 다룬 학술·공공 자료. 6·8절에 필요하다.
- 5. 현장 시나리오의 '완료·인계' 칸과 포장 단계 제약 조사: 물류센터 포장대를 병목으로 직접 분석한 1차 자료가 필요하다. 지금 포장 행은 추정뿐이고 완료·인계 칸은 해당 없음으로 비어 있다.
- 물류센터(병원·호텔이 아닌 곳)의 승강기·층간 반송 설비 병목 정량 자료 조사. 3절과 10. 설비·건물 시스템 연동 연결에 필요하다.
- 스마트물류센터 인증 세부 평가 지표 원문 확인(ref-106·ref-107 원문 미열람). 2026-09-25-09 f23 출처와 각주를 통합하는 일도 퍼블리셔에게 요청한다.
- Open-RMF 작업 배정기가 배터리 소모를 입찰에 반영하는 방식을 원문으로 확인해 달라. 10절의 13. 작업 배정 — MRTA 연결을 추정에서 사실로 올리는 데 필요하다.
- ref-096 URL을 검색 결과로 확인된 ScienceDirect 또는 pure.eur.nl 주소로 바꿀지 검토해 달라. 제1저자 표기(Lamballais Tessensohn)도 확인이 필요하다.
- 참고문헌 id ref-096~ref-067이 2026-09-25-09 등 이전 실행과 충돌하는지 게시 전에 퍼블리셔가 확인해야 한다.
- 퍼블리셔 요청: 자동 분리 주제 페이지 4건의 9. 검증 노트를 게시 시 정본 형식(1차 판정 / 2차 판정, 건수, 신뢰도)으로 치환해 달라(2차 검증 노트 지적).

## 이행한 수정 지시

- 원문 미열람 표기 — 13절에서 ref-096·054·055·056·057·059·060·061·064·065·066·067 각주의 접근일 뒤에 ' (원문 미열람)'을 붙였고, reference_updates 해당 항목에 source_unopened: true를 넣었다. ref-004·058·062·063에는 붙이지 않았다.
- f6 — 8절에서 결정 변수 세 가지와 SOQN은 [사실]로 쓰고, '처리량이 크게 좋아진다'는 결과는 원문 미확인을 밝힌 별도 [추정] 문장으로 분리했다. 4절·5절에는 결정 변수만 썼다.
- f11 — [추정]으로 강등하고 호텔 수치 실험(고객 노드 60개) 조건과 '물류센터 값이 아니다'를 문장에 밝혔다. 3절·5절에는 쓰지 않고 8절에만 두었다.
- f5 — 5절 제약 칸과 8절에서 '최대 처리량(처리 능력)'으로 썼다.
- f14 — 괄호 속 예시를 빼고 4절·7절에서 'RMFS 운영의 여러 결정 문제'로만 썼다.
- f8 — 3절·5절·6절에서 '대형'을 빼고 '유통사'로 썼다. ref-102 각주 기관 칸은 '저자 미확인'을 그대로 두었다.
- f10·f11·f12 — 3절·8절에 호텔·호텔·병원 사례임을 밝혔다. 5절 끝과 11절 셋째 질문을 이어 물류센터 근거가 없음을 적었다. 승강기 제어는 9절 표와 10절에서 10. 설비·건물 시스템 연동의 연계 대상으로만 두었다.
- 5절 포장(제약) — f13을 [추정]으로 두고 '물류센터 포장대를 병목으로 직접 분석한 1차 자료는 확인하지 못함'을 함께 적었다. 신뢰도를 높이는 표현은 쓰지 않았다.
- 9절 — f19는 '연계 대상:' 문구로 시작하게 유지했고, f18은 [추정]으로 두면서 '공개 사례는 확인하지 못했다'를 병기했다.
- f2 — 3절에 두 서베이의 저자가 다르다는 사실만 적고 '교차 확인됨' 표현은 쓰지 않았다.
- ref-096 — 기관 칸은 브리프 값을 그대로 썼다. 서지 'EJOR 256(3), 976–990, 2017'은 각주 제목 괄호와 8절 본문에 같게 적었다.
- 11절 — open_questions_new 4건을 옮기면서 관련 영역을 번호와 원문 명칭(예: 18. 사람–로봇 협업·운영 인터페이스)으로 적었다. '교대 운영'·'여러 거점의 자원 배치'는 근거 자료가 없다는 사실만 적었다.
- 10절 — 22. 시뮬레이션·예측용 디지털 트윈은 가정한 미래(증차·증설 대안)를 실험하는 용도로만 연결했고, 8. 실시간 세계 상태·데이터 일관성과는 구분한다고 적었다.
- 분량 초과 자동 분리: 3. 처리능력·거점·설비 계획 본문 7,075자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,977자
- 2차: 8절 요약 각주 — 세부영역 8절 요약 문장과 주제 페이지 s8 의 1절 첫 줄·3절 첫 문단의 [사실] 뒤에 [^ref-097][^ref-103]을 더했다.
- 2차: 10절 순위 표현 — '가장 가까운 연결은 충전 방식과 충전소 위치 연구다. [사실][^ref-098]'를 삭제하고 첫 문단을 '이 영역은 아래 다섯 영역과 이어진다.'라는 안내 문장으로 바꿨다.
- 2차: 10절 13. 작업 배정 — MRTA 항목 — 첫 문장을 'Open-RMF 플릿 어댑터 템플릿 설정에서는 충전 임계값보다 배터리가 낮은 로봇이 작업하지 않는다. [사실][^ref-105]'으로 범위를 좁히고, 배정 영향 문장은 [추정][^ref-105]으로 분리했다.
- 2차: 9절 마지막 문단 — '호텔 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다. [사실][^ref-103]'을 별도 문장으로 뗐고, 범위 문장은 '분류 원문 9장 시설·설비 제어 경계에 따른 이 위키의 판단이다. [의견]'으로 근거를 밝히며 ref-103 각주를 뗐다.
- 2차: 주제 페이지 s6 드리프트 — '소요대수는 다른 설계 과제와 얽혀 있어 따로 떼어 정하기 어렵다.'(와 그 앞 '한계도 있다.')를 삭제하고 Le-Anh·de Koster 문장만 남겼다.
- 2차: 주제 페이지 s6 태그 누락 — '대기행렬 모델은 … 추정한다.'에 [사실][^ref-096], '시뮬레이션은 … 쓰인다.'에 [추정][^ref-102], '충전 설비는 … 영향을 준다.'에 [사실][^ref-098]를 붙였다.
- 2차: 11절 문구 — 세부영역 11절의 '아래 질문으로 남긴다'를 '주제 페이지의 질문으로 남긴다'로 고쳤다.
- 2차: sources·cited_by 정합 — 세부영역 프런트매터 sources 에서 ref-107 를 뺐고, reference_updates 의 cited_by 를 실제 인용 페이지로 맞췄다(ref-107 는 s7 만, 분리 주제 페이지가 인용하는 출처에는 해당 주제 페이지 경로를 더함).
