# 스토리텔러 산출 2026-09-29-11

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/site-type-applications/warehouse.md | draft | 섹션 3~11 신규 작성(seed → draft), 프런트매터 related_areas·tags·confidence·sources·last_run 채움, 13절 각주 20건 추가; 2차 수정: 10절 1번 연결 벤더 주장 병기, AGV·AMR·WMS·WCS 첫 등장 풀이와 QPS·DPS·ITS 회사 표기 명시, 5절 마지막 단락 분할, [의견] 귀속 명시 |
| create | docs/topics/2026/2026-09-29-area61-s8.md | draft | 자동 분리: 61. 물류창고 의 "8. 대표 연구와 자료" 절(1,603자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area61-s6.md | draft | 자동 분리: 61. 물류창고 의 "6. 대표 접근법과 기술" 절(1,262자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area61-s4.md | draft | 자동 분리: 61. 물류창고 의 "4. 핵심 개념과 용어" 절(1,156자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area61-s11.md | draft | 자동 분리: 61. 물류창고 의 "11. 열린 질문" 절(1,068자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area61-s7.md | draft | 자동 분리: 61. 물류창고 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,062자)을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area61-s10.md | draft | 자동 분리: 61. 물류창고 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(868자)을 옮겼다; 2차 수정: 1. 기술·시장·업체 동향 연결 문장(3절 첫 항목·1. 세 줄 요약 첫 항목)에 벤더 주장 병기 |
| create | docs/topics/2026/2026-09-29-area61-s3.md | draft | 자동 분리: 61. 물류창고 의 "3. 왜 중요한가" 절(855자)을 옮겼다(2차 재실행에서 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 61. 물류창고 | 3~11절 신규 작성(seed → draft): 흐름 단계별 로봇 작업, 쿠팡 대구·DHL·CJ대한통운 사례, 스마트물류센터 인증 심사기준, ROP 직접 범위; 같은 날 실행 2026-09-29-10 의 ref-910~ref-913 과 id 충돌, URL 기준 병합 필요 | run 2026-09-29-11
- 홈 최근 업데이트: 2026-09-29 — 61. 물류창고: 3~11절 신규 작성(입고~반품 흐름 단계별 로봇 작업, 국내 쿠팡 대구·CJ대한통운과 해외 DHL·Amazon 사례, 스마트물류센터 인증 심사기준, ROP 직접 범위와 연계 대상)
- 대분류 최근 업데이트: 2026-09-29 — 61. 물류창고: 3~11절 신규 작성(흐름 단계별 로봇 작업 지도, 물류창고 사례 3건과 여섯 항목, 인증 심사기준의 6개 프로세스와 WMS·WCS/MCS 계층, 새 열린 질문 4건)
- 세부영역 최근 업데이트: 2026-09-29 — 61. 물류창고: 3~11절 신규 작성. 학술 서베이 3편, MAPD·지속형 MAPF, RAWSim-O, 국내 논문 2편, 인증 심사기준, 쿠팡 대구·DHL·CJ대한통운 사례를 정리하고 새 열린 질문 4건을 올렸다

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 상품-대-사람 | Goods-to-Person (GTP) | 로봇이나 설비가 선반·토트를 작업자 스테이션으로 가져와 작업자는 제자리에서 피킹하는 방식으로, 작업자가 선반까지 걸어가는 사람-대-상품(Person-to-Goods, PTG) 방식과 대비되며 로봇 이동형 풀필먼트 시스템이 대표 구현이다. | 61, 31, 25 | ref-919, ref-382 |
| new | 셔틀 기반 저장·회수 시스템 | Shuttle-Based Storage and Retrieval System (SBS/RS) | 층마다 움직이는 셔틀 차량과 리프트로 토트·상자를 랙에 넣고 꺼내는 자동 창고 시스템으로, 로봇화 창고 서베이가 로봇 이동형 풀필먼트 시스템·셔틀 기반 압축 저장 시스템과 함께 새 범주로 검토한다. | 61, 35 | ref-910 |
| new | AMR 협업 피킹 | AMR-assisted Order Picking | 자율이동로봇이 피킹 경로를 따라 작업자와 함께 움직이며 상품을 싣고 나르고 작업자는 집는 일만 맡는 방식으로, 기존 피커-대-상품 창고에 큰 개조 없이 도입할 수 있어 전자상거래 창고 서베이가 자동화 선택지의 하나로 든다. | 61, 31 | ref-382, ref-917 |
| new | 스마트물류센터 인증 | Smart Logistics Center Certification | 물류시설의 개발 및 운영에 관한 법률 제21조의4에 따라 국토교통부가 첨단·자동화 설비를 갖춘 물류창고를 1~5등급으로 인증하는 제도로, 하차·입고부터 상차·출고까지 6개 프로세스의 기능영역과 구조·성과·정보시스템의 기반영역을 심사한다. | 61, 23, 59 | ref-124, ref-921 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-910 | Azadeh, K., de Koster, R., & Roy, D. (Transportation Science 53(4)) | Robotized and Automated Warehouse Systems: Review and Recent Developments | 논문 | medium | https://pubsonline.informs.org/doi/10.1287/trsc.2018.0873 |
| ref-911 | Fragapane, G., de Koster, R., Sgarbossa, F., & Strandhagen, J. O. (European Journal of Operational Research 294(2)) | Planning and control of autonomous mobile robots for intralogistics: Literature review and research agenda | 논문 | medium | https://doi.org/10.1016/j.ejor.2021.01.019 |
| ref-382 | Boysen, N., Weidinger, F., & de Koster, R. (European Journal of Operational Research 277(2)) | Warehousing in the e-commerce era: A survey | 논문 | medium | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ |
| ref-913 | Schrotenboer, A. H., Wruck, S., Vis, I. F. A., & Roodbergen, K. J. | Integration of returns and decomposition of customer orders in e-commerce warehouses | 논문 | medium | https://arxiv.org/abs/1909.01794 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub 공식 저장소) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 오픈소스 문서 | high | https://github.com/merschformann/RAWSim-O |
| ref-915 | 곽경민, 박범, 고은지, 윤철주, 김경훈 (CJ대한통운, 로봇학회 논문지 17(4)) | 급속 확산되는 물류현장의 로봇적용 사례 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002899267 |
| ref-916 | 김태현, 송상화 (인천대학교, 한국디지털산업학회지 26(1)) | 온라인 주문 풀필먼트를 위한 물류센터 피킹 설비 최적화에 대한 연구 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002687327 |
| ref-917 | 로봇신문 (장길수) | CJ대한통운이 뽑은 물류자동화 혁신 기술 '톱3' | 기사 | low | https://www.irobotnews.com/news/articleView.html?idxno=28424 |
| ref-918 | Amazon | Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot | 벤더 문서 | medium | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model |
| ref-919 | 로봇신문 (장길수) | 쿠팡 대구 풀필먼트 센터에는 어떤 로봇들이... | 기사 | medium | https://www.irobotnews.com/news/articleView.html?idxno=30736 |
| ref-920 | 물류신문 (석한글) | ‘물류 투자만 6조’, 쿠팡 물류 인프라의 정점 ‘대구 FC’ 가보니 | 기사 | medium | https://www.klnews.co.kr/news/articleView.html?idxno=306994 |
| ref-921 | 스마트물류시설인증센터 (한국교통연구원) | 인증스마트물류센터 : 인증심사 > 심사기준 > 일반 | 정부·연구기관 | high | https://cslc.koti.re.kr/new_sub2/new_sub2_2_1 |
| ref-124 | 국토교통부 (국가물류통합정보센터) | 스마트물류센터 인증제 안내 | 정부·연구기관 | high | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW |
| ref-923 | CJ대한통운 | CJ대한통운 안성 MP허브, 국토부 ‘스마트물류센터 1등급’ 인증 | 벤더 문서 | medium | https://cjlogistics.com/ko/newsroom/news/NR_00001109 |
| ref-924 | Robotics 24/7 (Eugene Demaitre) | DHL Makes First Commercial Deployment of Boston Dynamics Stretch Robot to Unload Trailers and Containers | 기사 | medium | https://www.robotics247.com/article/dhl_makes_first_commercial_deployment_boston_dynamics_stretch_robot_unload_trailers_containers |
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 표준 | medium | https://ref.gs1.org/epcis/ |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. (AAAI 2021) | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 논문 | medium | https://arxiv.org/abs/2005.07371 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. (AAMAS 2017) | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 논문 | medium | https://arxiv.org/abs/1705.10868 |
| ref-257 | Interact Analysis (Rueben Scriven) | AMR Multi-Fleet Orchestration Software Explained | 업계 보고서 | medium | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)? | 61, 20 | 열림 | — |
| new | — | 스마트물류센터 인증 심사기준의 정보시스템 항목(WMS 150점, WCS/MCS 50점)에서 이기종 로봇 오케스트레이션 계층은 어느 항목으로 평가되며 인증 심사가 로봇 플릿 관제 기능을 따로 보는가? | 61, 23 | 열림 | — |
| new | — | 반품 재적치를 피킹 경로에 통합하는 최적화 연구를 로봇 이동형 풀필먼트 시스템이나 AMR 협업 피킹에 적용한 연구·사례가 있는가? | 61, 25 | 열림 | — |
| new | — | 트레일러 하역 로봇의 떨어진 상자 복구 같은 예외 처리가 로봇 자체 복구와 오케스트레이션 계층의 재계획 사이에서 어떻게 분담되는지 공개된 인터페이스나 사례가 있는가? | 61, 32 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 시작 조건 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |
| 물류창고 | 작업 대상 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |
| 물류창고 | 수행 자원 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |
| 물류창고 | 제약 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |
| 물류창고 | 완료·인계 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |
| 물류창고 | 예외·성과 | docs/categories/site-type-applications/warehouse.md#5-적용-사례-현장-유형-명시 | 61. 물류창고 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 7절 스마트물류센터 인증제 행: 1~5등급·최대 2%p 이자 지원·시설자금 한도·용적률·높이 완화·시행령 개정일의 직접 근거인 스마트물류시설인증센터 인증혜택 페이지(https://cslc.koti.re.kr/new_sub1/new_sub1_4)와 법적근거 페이지(https://cslc.koti.re.kr/new_sub1/new_sub1_2)를 참고문헌으로 등록해야 한다 — 1차 검증이 확인했으나 브리프 출처에 없어 본문은 ref-921·ref-124 로만 각주를 달았다.
- 5절 포장 단계: 물류창고 포장 단계의 로봇 도입 사례(출처 있는 것)가 필요하다 — 이번 브리프에 없어 '이번 실행에서 로봇 사례 미확인'으로 두었다(직전 실행 2026-09-29-10 의 CJ대한통운 양팔 로봇 사례를 재인용하려면 그 출처를 이 영역 브리프에 넣어야 한다).
- 5절 DHL 사례: DHL 원 보도자료(dhl.com 2023-02, group.dhl.com 2025-05·2025-07)를 열어 전문지 기사(ref-924)와 대조하고, 하역 사례의 제약·완료 확인 방식(현재 '미확인')을 채울 사실이 필요하다.
- 5·7절 인증: CJ대한통운 안성 MP허브터미널의 1등급 인증 사실을 스마트물류시설인증센터의 인증 목록으로 대조하고, 등급 구분 점수 기준(심사기준 페이지에 없음)을 확인해야 한다.
- 11절: oq-134·oq-138·oq-142·oq-146(국내 물류창고의 운영 기록 시뮬레이션 재현, 대화형 시나리오 구성·업무 지시, 소음 조건 음성 지시 인식률)은 이번 실행에서 별도 검색 예산이 배분되지 않아 미해결로 남았다 — 다음 실행에서 국내 자료를 겨냥한 검색이 필요하다.
- 13절 각주: 재사용 참고문헌 ref-003·ref-004·ref-005·ref-006·ref-257 의 각주 줄은 참고문헌 목록 입력이 0건이라 docs/references/ref-NNN.md 의 '각주 형식' 줄과 대조하지 못하고 브리프 sources 값으로 적었다 — 퍼블리셔가 등록된 기관·제목·URL 과 맞춰야 한다.
- 6절 계획·제어: 국내 물류창고의 이기종 플릿 통합 관제나 로봇 밀도·처리능력 설계 수치를 보고한 독립 출처(학술·기관)가 있으면 성과 항목의 벤더 주장(65%, 48%, 35%, 10%)을 대체하거나 대조할 수 있다.
- 5절 CJ대한통운 문장: QPS·DPS·ITS 약어의 공식 풀이(회사 표기)를 브리프 출처에서 확인하지 못해 '회사 표기, 풀이 미확인'으로 두었다 — 다음 실행에서 로봇신문 기사 또는 CJ대한통운 자료로 확인하면 풀어 쓸 수 있다.

## 이행한 수정 지시

- f1 열거 삭제 — 3절 첫 단락에서 '레이아웃·저장 슬로팅·주문 배치·피커 경로·피커–주문 배정' 열거를 빼고 '창고 설계·계획·제어 논리 전반을 다시 세워야 한다'로 썼다.
- f5 시뮬레이션 창고 기준 명시 — 6절 '온라인 작업 배정과 대규모 경로 계획', 8절 Li 외 항목, 10절 27. 다중 로봇 경로·교통 관리 — MAPF 연결에서 1,000대(지도 빈 칸의 38.9%) 수치 옆에 '시뮬레이션 창고 기준'을 붙였다.
- f11 표현·출처 병기 — 5절 쿠팡 대구 사례의 표(완료·인계·예외·성과)와 서술에서 '2분 안에'를 '평균 2분'으로 고치고, AGV 대수·선반 1,000kg·평균 2분·3,200억 원 이상이 현장 공개에서 회사가 제공한 수치임을 문장에 병기했다.
- f12 정확한 옮김·독립성 표시 — 5절에서 물류신문의 AGV 는 '1,000여 대', 소팅봇은 '수백 대가 넘는'으로 옮기고, 두 보도가 같은 현장 공개 행사의 회사 제공 정보에 기반해 독립성이 제한된다는 문장을 사례 서술에 [의견] 으로 남겼다(교차 확인은 [사실][^ref-919][^ref-920] 로 유지, 페이지 신뢰도 medium).
- f19 신뢰도·문구·출처 범위 — [사실] 로 유지하되 페이지 confidence 는 verification.json 의 medium 을 썼고, 4·7절에서 '시행령은 2020-10-08 개정돼 2021-01-01 시행'으로 고쳤으며, 7절 인증제 행에 '스마트물류시설인증센터 인증혜택·법적근거 안내 기준'을 밝히고 두 페이지의 참고문헌 등록은 additional_research_requests 첫 항목으로 넘겼다.
- f20 표현·벤더 주장 병기 — 5절 CJ대한통운 안성 사례의 표와 서술에서 '120개 이상 도크'를 '간선차량 120여 대 동시 접안'으로 고치고, 모든 문장을 [추정] 벤더 주장[^ref-923] 으로 썼으며 인증 사실이 인증센터 목록으로 대조되지 않았음을 적었다.
- f10·f13·f15·f16·f17·f20 벤더 주장 병기 — 4절 AMR 협업 피킹(f10), 5절 쿠팡 65%(f13)·DHL 하역 속도와 복구 목표(f15)·Amazon 로봇 100만 대(f16)·CJ대한통운 QPS·ITS·AMR(f10)·안성(f20), 6절 DeepFleet 10%(f17), 10절 1·46번 연결(f16·f17)에서 [추정] 뒤에 '벤더 주장'을 병기했다.
- ref-003·ref-257 미열람 표기, ref-004 열람 표기 — 13절 각주 정의에서 ref-003·ref-257 의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 두 항목에 source_unopened: true 를 넣었으며, ref-004 는 미열람 표기를 붙이지 않고 source_unopened: false 로 두고 summary 의 '원문 미열람.' 머리말을 제거했다.
- ref-910~ref-913 URL·id 충돌 기록 — reference_updates 의 네 항목에 브리프 URL 을 그대로 적고 summary 에 충돌 사실을 덧붙였으며, changelog_entry 에 '같은 날 실행 2026-09-29-10 의 ref-910~ref-913 과 id 충돌, URL 기준 병합 필요'를 남겼다.
- 5절 현장 유형·여섯 항목·포장 단계 — 사례 셋(쿠팡 대구, DHL 하역, CJ대한통운 안성) 모두 '현장 유형: 물류창고'를 명시하고 여섯 항목 표를 f25 대로 채웠으며, 포장 단계는 '이번 실행에서 로봇 사례를 확인하지 못했다'로 적고 직전 실행의 CJ대한통운 양팔 로봇 사례는 넣지 않았다.
- f7 피커 기반 명시 — 5절 반품 단계 문장과 6절 '보충과 반품의 최적화', 8절 Schrotenboer 항목에서 이 연구가 피커 기반 창고의 최적화이며 로봇 피킹 적용이 아님을 명시했다.
- f16·f17 기준일 근거 — 13절 각주 발행일은 브리프대로 2025-07 로 두고, 5절 Amazon 문장에 '페이지에 발행일 표기 없음, 검색 결과 기준'을 남겼다.
- 11절 기존·신규 질문 — oq-134·oq-138·oq-142·oq-146 은 상태 '열림'을 바꾸지 않고 '이번 조사에서도 국내 물류창고 자료 미확인'으로 적었으며(open_question_updates 에 update 없음), open_questions_new 4건은 브리프 문구대로 관련 영역 번호·이름을 유지해 페이지 11절과 open_question_updates(new, areas 61·20 / 61·23 / 61·25 / 61·32)에 등록했다.
- 9절 연계 대상 — f27 의 WMS 재고·주문 판단, 소터·컨베이어·도크 설비 제어, 하역·피킹 로봇의 인식·파지를 표 오른쪽 열에 '연계 대상:' 접두어로 짧게만 적고, 아래 단락에서 분류 원문 19장의 외부 영역임을 밝혀 ROP 직접 범위처럼 쓰지 않았다.
- 2차: 10절 1. 기술·시장·업체 동향 연결 문장 벤더 주장 병기 — warehouse.md 10절의 남은 요약 문장과 분리 페이지 docs/topics/2026/2026-09-29-area61-s10.md 의 3절 첫 항목·1. 세 줄 요약 첫 항목을 '[추정] 벤더 주장[^ref-918][^ref-257]' 로 고쳤다(1차 항목 7 의 보고와 페이지가 달랐던 곳).
- 2차: warehouse.md 약어 첫 등장 풀이 — 5절 쿠팡 표 수행 자원의 AGV 를 '무인운반차(Automated Guided Vehicle, AGV)'로, 5절 CJ대한통운 문장의 AMR 을 '자율이동로봇(Autonomous Mobile Robot, AMR)'으로(같은 규약에 따라 함께 풀었다), 9절 표 첫 행의 WMS 를 용어집 링크 [창고 관리 시스템(Warehouse Management System, WMS)](../../glossary/wes-wcs-wms-mes-tms.md)로, 9절 단락의 WCS 를 용어집 링크 [창고 제어 시스템(Warehouse Control System, WCS)](../../glossary/wes-wcs-wms-mes-tms.md)로 풀고 MCS 는 '심사기준 표기 그대로'라고 밝혔으며, 5절 CJ대한통운 문장 끝에 'QPS·DPS·ITS 는 회사 표기로 출처에 풀이가 없다'를 덧붙이고 새 풀이는 지어내지 않았다(추가 조사 요청에도 적었다).
- 2차: 5절 마지막 단락 분할 — '나머지 단계는 다음과 같다' ~ '로봇 피킹 적용은 아니다. [사실][^ref-913]'(보충·포장·반품 단계, 4문장)와 'Amazon 은 2025년 7월 발표…' ~ '매트릭스에 반영한다'(Amazon 과 여섯 항목 종합, 3문장)의 두 단락으로 나누고 문장·태그·각주는 바꾸지 않았다.
- 2차: [의견] 귀속 명시 — 5절 쿠팡 사례 서술의 문장을 '…교차 확인의 독립성은 제한적이다(1차 검증 노트 기준). [의견][^ref-919][^ref-920]' 로, DHL 사례 서술의 문장을 '…전문지 기사로 대신했다(브리프 자체 점검 기준). [의견][^ref-924]' 로 고쳤다.
- 2차: reference_updates ref-382 충돌 문구 삭제 — ref-382 summary 끝의 '같은 날 실행 2026-09-29-10 의 ref-382 와 id 충돌(URL 기준 병합 필요)' 문구를 지웠고, ref-910·ref-911·ref-913 의 충돌 문구는 유지했다.
