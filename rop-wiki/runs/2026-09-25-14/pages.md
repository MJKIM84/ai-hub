# 스토리텔러 산출 2026-09-25-14

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md | draft | 영역 심화: 3~11절 신규 작성(성과 지표 표준, 흐름 법칙·병목 탐지·프로세스 마이닝, 가상 시나리오, ROP 경계, 연결 7개 영역, 열린 질문 4건+기존 2건), task_state.json 은 기존 ref-111 재사용 |
| create | docs/topics/2026/2026-09-25-area04-s8.md | draft | 자동 분리: 4. 성과·경제성·프로세스 개선 의 "8. 대표 연구와 자료" 절(1,579자)을 옮겼다. 2차 수정: 각주 id 를 브리프 id 로 원복 |
| create | docs/topics/2026/2026-09-25-area04-s4.md | draft | 자동 분리: 4. 성과·경제성·프로세스 개선 의 "4. 핵심 개념과 용어" 절(1,517자)을 옮겼다. 2차 수정: 각주 id 를 브리프 id 로 원복 |
| create | docs/topics/2026/2026-09-25-area04-s6.md | draft | 자동 분리: 4. 성과·경제성·프로세스 개선 의 "6. 대표 접근법과 기술" 절(1,238자)을 옮겼다. 2차 수정: 각주 id 를 브리프 id 로 원복 |
| create | docs/topics/2026/2026-09-25-area04-s7.md | draft | 자동 분리: 4. 성과·경제성·프로세스 개선 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,187자)을 옮겼다. 2차 수정: task_state 행은 기존 ref-111 재사용, 나머지 각주 id 를 브리프 id 로 원복 |
| create | docs/topics/2026/2026-09-25-area04-s11.md | draft | 자동 분리: 4. 성과·경제성·프로세스 개선 의 "11. 열린 질문" 절(970자)을 옮겼다(2차 수정 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 4. 성과·경제성·프로세스 개선 | 3~11절 신규 작성(ISO 22400·SCOR·WERC 지표, 리틀의 법칙·병목 탐지·프로세스 마이닝, ROP 계산 지표와 주문·재무 지표의 경계, 열린 질문 4건), task_state.json 은 기존 ref-111 재사용 | run 2026-09-25-14
- 홈 최근 업데이트: 2026-09-25 — 4. 성과·경제성·프로세스 개선: 3~11절 신규 작성(성과 지표 표준, 병목 분석, 로봇 가동률과 주문·비용 지표의 경계, 열린 질문 4건)
- 대분류 최근 업데이트: 2026-09-25 — 4. 성과·경제성·프로세스 개선: 3~11절 신규 작성(ISO 22400·SCOR·WERC 지표, 리틀의 법칙·병목 탐지·프로세스 마이닝, ROP 경계, 열린 질문 4건)
- 세부영역 최근 업데이트: 2026-09-25 — 4. 성과·경제성·프로세스 개선: 영역 심화로 3~11절 신규 작성, 신뢰도 medium (실행 2026-09-25-14)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 종합설비효율 | Overall Equipment Effectiveness (OEE) | 설비의 가용성·효과성(성능)·품질률을 곱해 구하는 지표로, ISO 22400-2(2014판)가 제조 운영 관리 KPI의 하나로 정의한다. | 4, 16 | ref-139, ref-142 |
| new | 완전 주문 이행률 | Perfect Order Fulfillment | 완전 주문 수를 전체 주문 수로 나눈 비율로, 주문의 모든 품목 줄이 완전해야 완전 주문으로 보는 SCOR의 신뢰성 대표 지표(RL.1.1)이다. | 4, 1 | ref-140 |
| new | 리틀의 법칙 | Little's Law | 재공품(WIP)이 처리량(TH)과 사이클 타임(CT)의 곱과 같다는 관계로, 처리량·재공품·리드타임을 함께 해석하는 기준이 된다. | 4, 3 | ref-143 |
| new | 프로세스 마이닝 | Process Mining | 시스템에 남은 이벤트 로그로 실제 업무 흐름을 발견하고 대기·병목을 분석하는 기법이다. | 4, 2, 19 | ref-149, ref-147 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-001 | ASCM | SCOR Digital Standard | 표준 | medium | https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/ |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 논문 | medium | https://repub.eur.nl/pub/107376/ |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 논문 | medium | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 정부·연구기관 | medium | https://cslc.koti.re.kr/ |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-115 | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 표준 | medium | https://www.iso.org/standard/54497.html |
| ref-140 | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 표준 | medium | https://scor.ascm.org/performance/reliability/RL.1.1 |
| ref-141 | WERC(Warehousing Education and Research Council) | WERC DC Measures Survey - 2025 | 업계 보고서 | medium | https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf |
| ref-142 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Overall Equipment Effectiveness: consistency of ISO standard with literature | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527 |
| ref-143 | Project Production Institute | Little’s Law – A Practical Approach to Understanding Production System Performance | 업계 보고서 | medium | https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/ |
| ref-144 | Azadeh, K., de Koster, R., & Roy, D. | Robotized and Automated Warehouse Systems: Review and Recent Developments | 논문 | medium | https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873 |
| ref-145 | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S0307904X20305801 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 |
| ref-147 | Process Intelligence Solutions (PM4Py GitHub) | pm4py — Official public repository for PM4Py (Process Mining for Python) (README) | 오픈소스 문서 | high | https://github.com/process-intelligence-solutions/pm4py |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json |
| ref-149 | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9 |
| ref-150 | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 기사 | low | https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html |
| ref-151 | 박정수, 안영효(유통경영학회지) | 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? | 4, 1 | 열림 | — |
| new | — | 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? | 4, 16 | 열림 | — |
| new | — | 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? | 4, 3 | 열림 | — |
| new | — | 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? | 4, 19 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 피킹 | 작업 대상 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 피킹 | 수행 자원 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 피킹 | 제약 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 피킹 | 예외·성과 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 포장 | 제약 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 출하 | 완료·인계 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |
| 출하 | 예외·성과 | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 4. 성과·경제성·프로세스 개선 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 22400-2:2014 제조 운영 관리 KPI 정의 | 표준 | ISO | 4 | ref-139 | https://www.iso.org/standard/54497.html |
| WERC DC Measures | 평가 프로그램 | WERC(Warehousing Education and Research Council) | 4 | ref-141 | https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf |
| PM4Py | 오픈소스 | Process Intelligence Solutions | 4, 2, 19 | ref-147 | https://github.com/process-intelligence-solutions/pm4py |

## 추가 조사 요청

- 4·7절: ISO 22400-2:2014의 KPI 개수와 ISO/DIS 22400-2 개정 진행 여부를 ISO 원문 또는 독립 출처로 확인해야 한다 — 이번에는 제3자 요약뿐이라 개수는 미확인, 개정 부분은 삭제했다.
- 4·7절: WERC DC Measures 2025의 지표 정의와 벤치마크 수치를 원문으로 확인해야 한다 — f6이 [추정]으로 강등되었다.
- 3·11절: 로봇 가동률과 주문 단위 지표(완전 주문 이행률, 주문 이행 사이클 타임)·비용을 같은 기간으로 연결해 실증한 공개 사례가 필요하다 — 2절 질문에 대한 3절 결론이 [추정]뿐이다.
- 9·11절: 국내 물류 로봇 도입 투자 효과를 측정한 공공·학술 자료가 필요하다 — 현재는 벤더 발표 기사(ref-150)뿐이다.
- 11절: oq-008(거점 간 로봇 재배치·성수기 임대)과 oq-011(스마트물류센터 인증 세부 지표에 로봇 대수·가동률 포함 여부)의 학술·공공 근거가 여전히 없다.
- 다음 실행 후보: ASTM F45 이동로봇 성능 시험 방법(23. 시험·형식 검증·벤치마크)과 인간–로봇 협업 피킹 현장 실험(18. 사람–로봇 협업·운영 인터페이스)은 출처 상한으로 브리프에 들어오지 않았다.
- pipeline·퍼블리셔 담당: 1차 검증의 참고문헌 id 재부여 지시를 2차 검증이 원복시켰다(브리프 id ref-139~ref-151·ref-115 사용, task_state.json 은 기존 ref-111). agent_runner.py 의 next_ref_id 계산과 참고문헌 목록 입력의 최신성, ref-115 가 data 쪽에서 미사용인지 확인해야 한다.

## 이행한 수정 지시

- 참고문헌 id 재부여 — 1차 지시로 ref-125~ref-138로 바꿨던 신규 출처 id를 2차 지시에 따라 브리프 id(ref-139, ref-140, ref-141, ref-142, ref-143, ref-115, ref-144, ref-145, ref-146, ref-147, ref-148, ref-149, ref-150, ref-151)로 원복했고, 이 id들이 기존 참고문헌과 겹치지 않음을 2차 검증이 확인했다.
- task_state.json 재사용 — 1차 지시의 ref-140 대신 2차 지시대로 입력 참고문헌 목록의 같은 문서인 기존 ref-111을 5·9·10절과 분리 주제 페이지 s7에 달고, 새 id로 등록하지 않았다.
- f6 강등 — 4절 용어 목록과 7절 표의 WERC 문장을 [추정]으로 쓰고 '2026년 보고서는 주문 피킹 정확도를 품질 지표로 명시' 절을 삭제했다.
- f1 — 4·7절에서 '30여 개' 표현을 빼고 '(지표 개수는 미확인)'을 적었으며 'ISO 22400-2:2014판', '2014판'으로 기준일을 명시했다.
- f2 — 'ISO/DIS 22400-2 개정안 진행 중' 부분을 삭제하고, 4절 OEE 정의 문장 바로 뒤에 f3을 논문 저자들의 [의견]으로 붙였다.
- f3·f23 — 4·8절에서 'Computers & Industrial Engineering(2020) 게재 논문 저자들은', '박정수·안영효(2010)는'으로 [의견]의 주체를 문장 안에 밝혔다.
- f12 — 5절 표 예외·성과 칸의 3.41%·26.07% 수치 뒤에 '(저자 보고값이며 모델·시뮬레이션 조건의 결과이고 현장 실측이 아님)'을 병기했고, 6·8절에는 수치 없이 절충 결과만 적었다.
- f21 — 오토스토어 경제성 수치를 9절 연계 대상(재무) 맥락에만 두고 '[추정] 벤더 주장' 병기와 '연구 수행 주체와 방법론은 미확인이며 ROP의 직접 성과가 아니다'를 적었다.
- 원문 미열람 표기 — ref-111·ref-147·ref-148을 뺀 모든 각주 정의(ref-001·096·097·098·102·106·115·139~146·149~151)의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true를 넣었다.
- oq-011·oq-008 — 11절에서 oq-011은 열림 상태로 두고 f22로 성과관리 체계 평가와 등급 기준만 부분 보강했으며 개별 지표는 미확인이라고 적었고, oq-008도 미해결로 두었다. open_question_updates 에 해결 변경을 내지 않았다.
- 10절 연결 — f16 로봇 상태 기록은 8. 실시간 세계 상태·데이터 일관성(현재 상태 표현)에, f12·f13의 정책·충전 대안 비교는 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)에 나눠 연결하고 두 역할을 구분하는 문장을 넣었다.
- 분량 초과 자동 분리: 4. 성과·경제성·프로세스 개선 본문 9,623자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,845자
- 2차: task_state.json id 정정 — 세부영역 페이지 5절 완료·인계 칸, 5절 표 아래 문단, 9절 첫 문장·표, 10절 1. 주문·업무 시스템 연계 항목과 주제 페이지 s7 표의 task_state 행에서 [^ref-140]을 [^ref-111]로 바꾸고, 지시된 ref-111 각주 정의 줄을 두었으며, 두 페이지 프런트매터 sources에 ref-111을 넣고, reference_updates에서 task_state용 ref-140 항목을 빼고 ref-111 항목에 cited_by만 넣었다.
- 2차: 신규 출처 id 원복 — 세부영역 페이지와 분리 주제 페이지 5개의 본문 각주·각주 정의·프런트매터 sources, reference_updates·glossary_updates[].sources·standards_updates[].ref_id·additional_research_requests에서 ref-125→ref-139, ref-126→ref-140, ref-127→ref-141, ref-128→ref-142, ref-129→ref-143, ref-130→ref-115, ref-131→ref-144, ref-132→ref-145, ref-133→ref-146, ref-134→ref-147, ref-135→ref-148, ref-136→ref-149, ref-137→ref-150, ref-138→ref-151로 바꿨다.
- 2차: 문구 정정 — changelog_entry와 세부영역 페이지 diff_summary에서 '참고문헌 id ref-125~ref-138 재부여'를 빼고 'task_state.json 은 기존 ref-111 재사용'으로 바꿨으며, fixes_applied의 id 관련 첫 두 항목을 이번 수정 내용으로 고쳐 적었다.
- 2차: 10절 22. 시뮬레이션·예측용 디지털 트윈 항목의 '우선순위 정책과 충전 대안을 운영 전에 비교하는 일은 가정한 미래를 실험하는 쪽이다.' 문장 태그를 [사실]에서 [추정]으로 바꿨다([추정][^ref-146][^ref-102]).
