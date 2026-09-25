# 1차 검증(브리프) 2026-09-25-29

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 data/source_texts/ref-031.txt(VDA 5050 3.0.0, main) 2절 Scope 의 'Other Communication Interfaces' 항목이 주변 설비·인프라·외부 IT 시스템 인터페이스를 제외한다. 단일 출처(표준 원문)로 [사실] 유지. 발행일 미확인, 3.0.0 판 기준. |
| f2 | 예 | 예 | 아니오 | 유지 | 추론 finding. ref-031 범위 제외는 원문으로 확인했다. ref-125(task_request.json)는 이번 실행에서 원문 미열람이며 1. 주문·업무 시스템 연계 게시 페이지 인용을 재사용했다. 번역 계층을 정한 표준은 없어 [추정] 유지. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: ref-031 원문 6.1.4.6(OTHER_ORDER_ACTIVE, 수준 WARNING)과 6.1.3(취소 불가 동작은 RUNNING을 거쳐 FINISHED/FAILED 보고). 단일 출처 [사실]. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: raw.githubusercontent.com 으로 B2MML-TransactionProfile.xsd 를 열어 TransactionVerb1Type(NOTIFY·GET·PROCESS·CHANGE·CANCEL·CONFIRM·SYNC ADD/CHANGE/DELETE)을, ISA95-JOBCONTROL documentation.csv 를 열어 ISA95JobOrderReceiverObjectType 메서드(Store~Clear 11개)를 확인했다. 두 주장은 출처가 각각 달라 교차 확인은 아니다. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: task_state.json 원문의 status enum 12개, unix_millis_start_time/finish_time, estimate_millis, cancellation·killed·interruptions. '상위 시스템에 되돌릴 결과의 원천이 된다'는 연결 해석이므로 본문에서는 스키마 내용을 [사실], 원천 역할은 연결 설명으로 쓴다. |
| f6 | 예 | 예 | 아니오 | 유지 | ref-133·ref-134 원문 미열람. 두 출처는 참고문헌 목록에 있고 1. 주문·업무 시스템 연계 게시 페이지에서 검증된 인용을 재사용했다. 이번 검증에서 재검색하지 않았다. 순서 결정과 대응시킨 추론이므로 [추정] 유지. |
| f7 | 예 | 예 | 아니오 | 유지 | ref-132 원문 미열람. 게시 페이지 1. 주문·업무 시스템 연계 5·10절 인용을 재사용했다. [추정] 유지. 기준일 2025. |
| f8 | 예 | 예 | 아니오 | 유지 | f3(ref-031 원문)과 f4(ref-129 원문)를 대응시킨 추론이다. 되돌림 규칙 표준은 확인되지 않았다(oq-021). [추정] 유지. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: CBV.ttl 원문에서 arriving(위치 도착)·receiving(수령자 재고 추가)·accepting(점유·소유 변경) 정의를, VDA 5050 원문 Table 5 에서 drop FINISHED 정의('Load has left the mobile robot and mobile robot reports new load state')를 확인했다. 서로 다른 두 사실을 각 출처가 뒷받침하므로 교차 확인은 아니다. |
| f10 | 예 | 예 | 아니오 | 유지 | ref-044·ref-031·ref-049 원문 기반 추론. 주장 문구의 '7번'은 번호만 쓴 호칭이므로 본문에서는 '7. 화물·재고·자산 식별과 추적'으로 쓴다(수정 지시). [추정] 유지. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: 입력 ref-023 원문(워크셀 장 4단계 'Requests a IngestorRequest till receives a IngestorResult')과 IngestorResult.msg 원문(time·request_guid·source_guid·status ACKNOWLEDGED=0/SUCCESS=1/FAILED=2)을 확인했다. 메시지에 time 필드도 있으므로 '만 담는다'는 '요청 id·워크셀 id·상태(와 시각)'로 정확히 쓴다(수정 지시). |
| f12 | 예 | 예 | 아니오 | 유지 | ref-121 원문 미열람. 게시 페이지 2. 공정·워크플로 모델링 6절 인용을 재사용했다. 물류 적용 사례 미확인으로 [추정] 유지. 기준일 2022. |
| f13 | 예 | 예 | 아니오 | 유지 | ref-102·ref-098 원문 미열람. 게시 페이지 3. 처리능력·거점·설비 계획 3·10절의 검증된 [사실] 문장을 재사용했다. 두 출처는 서로 다른 주장을 뒷받침하므로 문장별로 각주를 나눈다(수정 지시). 신뢰도 medium 상한. |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: fleet_adapter_template config.yaml 원문의 recharge_threshold 0.10('below which robots in this fleet will not operate'), recharge_soc 1.0, 로봇별 charger, finishing_request park/charge/nothing. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: rmf_demos README 원문의 호텔 환경(로비와 객실 2층, 승강기 2대, 여러 문, 3개 플릿·로봇 4대)과, 공간·건물 설비(승강기·문 등)를 공유하는 로봇 교통 관리에 관한 설명. Open-RMF 설명으로 서술하고 ROP 직접 범위처럼 쓰지 않는다. |
| f16 | 예 | 예 | 아니오 | 유지 | ref-060·ref-103 원문 미열람. 게시 페이지 3. 처리능력·거점·설비 계획 인용을 재사용했다. 병원·호텔 사례이고 물류센터 적용은 미확인(oq-010)이라는 한정을 본문에 유지한다. ref-103 발행일 미확인. |
| f17 | 예 | 예 | 아니오 | 유지 | 확인: RAWSim-O README 원문('a discrete event-based simulation for Robotic Mobile Fulfillment Systems … researching effects of multiple decision problems'). '증차·증설 같은 가정한 미래의 실험 도구'는 22. 시뮬레이션·예측용 디지털 트윈 연결에 관한 해석이므로 README 내용과 구분해 쓴다. |
| f18 | 예 | 예 | 아니오 | 유지 | 확인: robot_state.json 원문의 status enum 7개(uninitialized·offline·shutdown·idle·charging·working·error), battery 0.0~1.0, task_id, issues(운영자가 대응할 문제), location, unix_millis_time. '지표의 원천'은 연결 해석이다. |
| f19 | 예 | 예 | 아니오 | 유지 | ref-148 은 원문 확인. ref-115·ref-149 는 원문 미열람인데 브리프의 source_unopened 는 false 로 적혀 있다(브리프 표시 누락). 게시 페이지 4. 성과·경제성·프로세스 개선 10절의 연결 근거를 재사용했다. 적용 연구 미확인(oq-018), [추정] 유지. |
| f20 | 예 | 예 | 아니오 | 유지 | ref-146 원문 미열람. 3.41%·26.07%는 게시 페이지 4. 성과·경제성·프로세스 개선 5절에서 검증된 [사실] 문장(저자 보고값, 모델·시뮬레이션 조건)을 재사용했다. 단일 출처 수치이므로 '저자 보고값·현장 실측 아님' 한정을 반드시 유지한다. 이 페이지의 결론을 좌우하는 핵심 수치로 쓰지 않는다. |
| f21 | 예 | 예 | 아니오 | 유지 | ref-146·ref-102 원문 미열람. 게시 페이지 4. 성과·경제성·프로세스 개선 10절 연결 서술과 분류 원문 7장의 8·22 구분을 대응시킨 추론이다. [추정] 유지. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분을 지킨다. |
| f22 | 예 | 예 | 아니오 | 유지 | ref-129·ref-130·ref-031 은 원문 확인, ref-125 는 원문 미열람. 매핑 부재는 검색 범위 안의 관찰이지 부재를 확인한 것이 아니므로 '확인되지 않았다'로 쓰고 oq-020 을 연결한다. [추정] 유지. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 예 | — |
| 용어 일관성 | 예 | — |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- page_proposals 의 섹션 '5. 다른 대분류와의 연결' — patches 의 section 은 대분류 페이지 H2 그대로 '다른 대분류와의 연결'(번호 없음)로 쓴다. 대분류 H2 에는 번호가 없고 다른 절은 건드리지 않는다.
- f10 — 본문에서 '7번'을 '7. 화물·재고·자산 식별과 추적'으로 쓴다. 코드·번호만 쓰는 호칭을 금지하기 때문이다(공통 규칙 6절). 다른 대분류는 'B. 공통 정보·환경 모델'처럼 문자와 이름을 함께, 세부영역은 번호와 이름을 함께 쓴다.
- f11 — 'IngestorResult 는 요청 id·워크셀 id·상태만 담는다'를 '시각, 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다'로 고친다. IngestorResult.msg 원문에 time 필드가 있다.
- f13 — 충전기 부족·과잉 문장에는 [^ref-102]만, 충전·배터리 교환 전략 비교 문장에는 [^ref-098]만 단다. 두 출처는 서로 다른 주장을 뒷받침하므로 교차 확인처럼 한 문장에 묶지 않는다.
- f16 — 병원 사례에는 [^ref-060]을, 호텔 사례에는 [^ref-103]을 따로 달고 '물류센터 적용 여부는 미확인'을 유지한다. 승강기는 3. 처리능력·거점·설비 계획이 받는 제약 입력으로만 쓰고, 승강기 제어는 연계 대상으로 짧게 둔다. 분류 원문 9장의 시설·설비 제어 경계에 따른 것이다.
- f20 — 3.41%·26.07% 수치에는 '저자 보고값, 모델·시뮬레이션 조건, 현장 실측 아님'을 함께 쓴다. 단일 출처이고 원문을 열지 못했기 때문이다.
- f5·f17·f18 — 스키마·README 가 담은 내용만 [사실]로 쓴다. '상위 시스템에 되돌릴 결과의 원천', '가정한 미래의 실험 도구', '지표의 원천'이라는 연결 해석은 태그 없는 연결 설명으로 쓰거나 [추정]으로 분리한다.
- 모든 [추정] finding(f2·f6·f7·f8·f10·f12·f19·f21·f22)은 '~것으로 보인다' 문형과 [추정] 태그로 쓰고 [사실]로 올리지 않는다. f22 의 매핑 부재는 '이번 조사 범위에서 확인되지 않았다'로 쓰고 oq-020 을 연결한다.
- f21 — 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)과 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)의 구분 문장을 유지한다. f18 은 8. 실시간 세계 상태·데이터 일관성 쪽 연결로만 쓴다.
- 원문 미열람 출처 각주 — ref-125·ref-132·ref-133·ref-134·ref-121·ref-102·ref-098·ref-060·ref-103·ref-115·ref-149·ref-146 의 각주 정의는 접근일 뒤에 ' (원문 미열람)'을 붙인다. 참고문헌 목록에 있는 줄 형식 그대로 쓰고, reference_updates 에 이 출처들을 넣으면 source_unopened: true 로 둔다. 원문을 연 ref-031·ref-111·ref-129·ref-130·ref-044·ref-023·ref-049·ref-104·ref-105·ref-101·ref-148 에는 이 표시를 붙이지 않는다.
- 직접 인용 — evidence_excerpt 의 영문 구절(ref-031 은 f1·f3·f9 세 곳)을 본문에 그대로 옮기지 않는다. 요약·재서술하고, 직접 인용이 필요하면 출처당 한 번 짧은 구절만 쓴다.
- 연결 범위 — 브리프가 근거 없음으로 제외한 11. 분산 시스템·통신·컴퓨팅 구조, 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영 과의 연결은 쓰지 않는다. G. 안전·보안·지능·거버넌스 연결은 f22(28. 표준·상호운용성·다사업자 거버넌스)만 쓴다.
- 링크 — 다른 대분류와 세부영역 링크는 docs/categories/a-business-supply-chain-design/index.md 위치를 기준으로 한 상대 경로에 .md 를 붙여 쓴다(예: ../c-connectivity-and-execution-foundation/index.md, ../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md). 각주 정의는 페이지의 '참고 자료' 절에 추가하되 기존 ref-002 각주와 그 절의 문장은 바꾸지 않는다.

## 검증 노트

판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(fetch_mode mirror_only)에서 검증됐다. 확인 22건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-125, ref-132, ref-133, ref-134, ref-121, ref-102, ref-098, ref-060, ref-103, ref-115, ref-149, ref-146. 원문 확인: GitHub 공식 저장소 원문 10건(ref-031 drop 정의, ref-111, ref-129, ref-130, ref-044, ref-049, ref-104, ref-105, ref-101, ref-148)을 raw.githubusercontent.com 으로 다시 열었고, ref-031·ref-023 은 입력 원문 텍스트로 대조했다. 원문 미열람 출처는 이번 검증에서 재검색하지 않고, 게시된 1~4 세부영역 페이지의 검증 이력과 참고문헌 목록 등재로 실재를 인정했다. 검색 0회. 브리프 표시 누락: f19 가 원문 미열람 출처 ref-115·ref-149 에 기대는데 source_unopened 가 false 로 적혀 있다. self_check.limits 의 '10건'은 나열된 11건과 수가 맞지 않는다. 주의: 연결 상대 세부영역 대부분이 seed 여서, 연결 근거는 A. 업무·공급망 설계 쪽 게시 페이지의 주장에 기댄다. 연결 22건 가운데 9건은 추론([추정])이다. f20 의 수치는 단일 출처의 저자 보고값(모델·시뮬레이션 조건)이다. 11. 분산 시스템·통신·컴퓨팅 구조와 27. AI·학습·적응과 모델 운영 등과의 연결은 검증된 근거가 없어 이번에 싣지 않았다. 정정 요청 없음.
