# 1차 검증(브리프) 2026-09-25-50

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문(data/source_texts/ref-031.txt) 6.1.3 절 — 가능한 한 빨리 정지, 예정 동작 FAILED, 정지 뒤 cancelOrder FINISHED, 유휴. 단일 출처(같은 발행 주체). evidence_excerpt 의 '취소 시 적재물 처리는 따로 정하지 않는다'는 원문에 언급이 없다는 해석이므로 본문에 쓰면 [추정]으로 둔다. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: 4.1 절 last will·'fulfills the order up to the last released node'(입력 원문). 단 github_raw 로 다시 연 6.5 절에는 connectionState 값이 HIBERNATING 까지 넷이다 — 세 값만 적은 것은 불완전하므로 수정 지시. 원문은 connection 토픽을 로봇 상태 점검용으로 쓰지 말라고 적는다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: state.schema(github_raw 열람) errorLevel = WARNING·URGENT·CRITICAL·FATAL, actionStatus 에 RETRIABLE. 명세 6.2.3.2 에서 RETRIABLE 상태의 로봇은 관제 또는 운영자 개입을 기다리고 retry·skipRetry 즉시 동작으로 처리된다. ref-051·ref-031 은 발행 주체가 같아 교차 확인이 아니다. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: state.schema loads 의 loadId(바코드·RFID 예시), loadType, loadPosition, loadDimensions, weight(kg). '관제가 알 수 있는 근거가 된다'는 로봇이 loads 를 보고하는 경우에 한한다(선택 필드). |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 표 4 의 startPause·stopPause 설명과 state.schema paused 설명이 일치. |
| f6 | 예 | 예 | 아니오 | 유지 | 부분 확인: 5.3 절 관제 기능 목록에 교착 탐지·해소와 통신 오류 탐지·해소가 있음(입력 원문). 그러나 '사용자 개입이 필요한지, 취소 뒤 새 주문을 보낼지 관제가 결정'하는 문장은 6.1.5 절 통로(corridor) 이탈 오류(OUTSIDE_OF_CORRIDOR) 맥락이고, 6.4.5 절 구역 오류 처리는 관제가 진행 방법을 정한다고만 적는다 — '구역 충돌' 표현 수정 지시. 2장 범위에서 교착 해소 전략·알고리즘 자체는 명세 밖이다. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: RobotUpdateHandle.hpp(github_raw 열람)에 interrupt, Interruption::resume, cancel_task, kill_task, replan(update_position 으로 준 마지막 위치에서 새 계획), set_commission(Commission: 배정·직접 작업 수락 여부), create_issue 가 있음. 헤더 문서 주석 기준이며 동작 검증은 아님. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 ref-004 — 'living database' 로 지연·취소·경로 변경 반영, 충돌 통지 뒤 플릿 관리자 협상과 제3자 판정, 긴급 참여자의 의도적 충돌 게시. 게시된 D. 계획·최적화 연결 주장(실행 2026-09-25-49 f15)과 같은 출처이므로 ref-004 각주 재사용. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: integration_fleets.md(github_raw) — Full Control 은 경로를 언제든 중단·교체, Traffic Light 는 pause/resume 만 허용. Read Only 는 ref-251 에 없고 ref-004 에만 있다(제어권 없음, 공유 공간당 하나). ref-004·ref-251 는 같은 발행 주체라 교차 확인 아님. 각주를 주장 부분별로 맞게 단다. |
| f10 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치: 이슈 224 의 재시작 뒤 작업 유실, SQLite 작업 백업 PR 161, rmf-web 영속 DB 조회 제안이 검색 요약에 나타남. 발행일 미확인. 반영 여부 미확인이므로 oq-048 은 해결 아님. |
| f11 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 같은 논문·같은 URL 이 기존 ref-188(실행 2026-09-25-49 f23, 게시된 D. 계획·최적화 연결)로 이미 있다 — ref-188 을 새로 등록하지 말고 ref-188 재사용. 용어는 기존 용어집 action-dependency-graph(행동 의존 그래프) 재사용. |
| f12 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치(arXiv 2403.18145, ICAPS 34 pp.201–209, 저자 Feng·Paul·Chen·Li): SES 가 지연된 로봇의 통과 순서를 재스케줄, 최선 변형이 중소 규모 1초 미만·대규모 기준선 대비 최대 4배 빠름. 수치는 저자 보고값이며 단일 출처. |
| f13 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치(MDPI Sensors 21(19) 6536, 저자 Kalempa·Piardi·Limeira·Oliveira): 우선순위 선점 스케줄링·작업 의존성·고장 허용, ARENA 소규모 창고 물류 실험. |
| f14 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과로 실재 확인(arXiv 2211.08201 v2 2023-06-03, IFAC 2023 게재). 저자는 Emanuelsson, Penacho Riveiros, Li, Johansson, Mårtensson(KTH) — 출처 기관 칸 수정 지시. 고장 예제 부분은 리서치 브리프의 검색 요약 기준이며 이번 검증 검색에서 다시 확인하지 못함. |
| f15 | 예 | 예 | 아니오 | 유지 | 원문 미열람(유료), 검색 결과로 ISO 소개 페이지·제목 일치 확인. ISO 22301:2019 는 2012 판을 대체한 2판이고, 개정 1:2024(기후 행동 변경, iso.org/standard/88412)이 있다 — 기준 판 명시 지시. |
| f16 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치: 행정안전부 페이지가 「재해경감을 위한 기업의 자율활동 지원에 관한 법률」, 기업재난관리표준(행정안전부 고시), 인증대행기관의 1차 문서평가·2차 현장평가를 설명. 발행일 미확인. |
| f17 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치(고용노동부 공지 bbs_seq=20220301591, 2022-03): 오미크론 확산기 중소규모 사업장 BCP 가이드와 7단계. 감염병 대응 목적의 권고 가이드임을 본문에 밝힌다. |
| f18 | 예 | 예 | 아니오 | 유지 | 확인: compensating-transaction.md(github_raw, ms.date 2026-04-16) — 원래 상태를 반드시 복원하지 않음, 보상 실패 가능, 단계를 멱등 명령으로, 진행 기록 후 실패 지점부터 재개, 영향이 크거나 자동화가 어려운 결정은 사람 포함. 소프트웨어 설계 패턴이므로 물리 작업 되돌림에 적용하는 부분은 [추정]으로 서술. |
| f19 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치: XHandler 가 고장 로봇을 넘겨받아 시스템 정지 없이 복구 시도, 자동 처리 불가·충돌 위험 때만 정지. [추정]·벤더 주장·vendor_claim 표시 적정. 통합업체 FAQ 로 AutoStore 와 독립 출처가 아니다. |
| f20 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치: SynQ 가 멈춘 로봇 아래 재고를 다른 보관함으로 재할당하고 정기 휴식·저수요 시간에 로봇을 꺼낼 때까지 주문 처리 지속. [추정]·벤더 주장 표시 적정. 검색에 나온 URL 은 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 브리프 URL 경로와 다르다 — 수정 지시. |
| f21 | 예 | 예 | 아니오 | 유지 | 원문 미열람, 검색 결과 일치: 저장소를 일지 방식으로 두어 수정·삭제 수단이 없고, 같은 eventID 의 거의 같은 이벤트가 ErrorDeclaration(선언 시각, 선택 사유, 선택 correctiveEventIDs)을 가리킨다. EPCIS 1.2(2016-09-29) 기준이며 현행 판은 아님 — 기준 판 명시. 기존 용어집 epcis-error-declaration 재사용. |
| f22 | 예 | 예 | 아니오 | 유지 | 종합 추정으로 [추정]·low 적정. 근거 출처 가운데 ref-573·ref-581 은 원문 미열람인데 finding 은 source_unopened: false 로 적혀 있다(브리프 표시 불일치, 페이지 서술에는 영향 없음). 이 흐름을 한 절차로 정한 출처는 없다고 밝힌다. |
| f23 | 예 | 예 | 아니오 | 유지 | 경계 추정으로 [추정] 적정. '연계 대상:' 표시가 있고 분류 원문 9장 '로봇 자체 지능·제어' 경계와 맞다. VDA 5050 2장이 운영 책임 배분을 범위 밖으로 둔다는 점과도 맞는다. |
| f24 | 예 | 예 | 아니오 | 유지 | 추정 적정. 근거 확인: 4.1 절 last released node 규칙, 6.1.2 절 결정 지점에서 정지, state.schema newBaseRequest '새 기반이 오지 않으면 속도를 줄인다'. oq-038 해결은 아님. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | ref-188(Hönig 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, https://ieeexplore.ieee.org/abstract/document/8620328/)은 기존 ref-188 과 같은 논문·같은 URL — 실행 2026-09-25-49 f23(D. 계획·최적화 대분류 연결)에서 이미 인용, f8·f9 는 실행 2026-09-25-49 f15(Open-RMF 제어 수준·교통 협상, ref-004)와 겹친다 — ref-004 각주 재사용, f3 는 실행 2026-09-25-48 f1(VDA 5050 errorLevel 네 값, ref-051)과 겹친다 — ref-051 각주 재사용, 19. 모니터링·이상 탐지·원인 분석과 연결, f2 는 실행 2026-09-25-48 f4(connection 토픽 last will, ref-506 connection.schema)와 겹친다 |
| 용어 일관성 | 아니오 | f11 의 행동 의존 그래프(ADG)는 용어집 action-dependency-graph 로 이미 있다 — 새 등록하지 않고 재사용, f21 의 오류 선언(errorDeclaration)은 용어집 epcis-error-declaration 로 이미 있다 — 재사용, 용어 후보 '업무연속성 관리 시스템'은 세부영역 원문 명칭 '20. 예외 복구·재계획·업무 연속성'의 띄어쓰기('업무 연속성')와 다르다 — '업무 연속성 관리 시스템'으로 통일 |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- ref-188: 새 참고문헌으로 등록하지 않고 기존 ref-188(같은 논문·같은 URL)로 바꾼다. f11 을 쓰는 본문 각주와 reference_updates 모두 ref-188 을 쓴다 — 중복 출처 방지.
- f11·f21: 행동 의존 그래프와 오류 선언은 기존 용어집 항목(action-dependency-graph, epcis-error-declaration)에 연결하고 glossary_updates 에 새로 넣지 않는다 — 용어집에 이미 있다.
- 용어 후보 '업무연속성 관리 시스템'을 '업무 연속성 관리 시스템'으로 고쳐 등록한다 — 세부영역 명칭의 띄어쓰기와 맞춘다.
- f2: connectionState 값을 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 네 값으로 적거나 '등'을 붙인다 — ref-031 6.5 절(github_raw 열람)에 HIBERNATING 이 있다.
- f6: '구역 충돌 같은 상황에서' 부분을 '통로(corridor) 이탈 오류 같은 상황에서'로 고친다 — 사용자 개입·취소 뒤 새 주문 결정 문장은 ref-031 6.1.5 절 문맥이다. 교착 해소 전략·알고리즘 자체는 명세 범위 밖(ref-031 2장)이라는 점도 함께 적는다.
- f1: evidence_excerpt 의 '취소 시 적재물 처리는 따로 정하지 않는다'를 본문에 쓰면 [추정]으로 두고 '6.1.3 절에 적재물 언급이 없음'으로 표현한다 — 명세 원문에 없는 해석이다.
- f9: Read Only 설명의 각주는 ref-004 만 단다 — ref-251(integration_fleets)는 Full Control·Traffic Light 만 다룬다.
- f12: 1초 미만·최대 4배 수치를 '저자 보고값(ICAPS 2024, 단일 출처)'으로 명시한다 — 독립 교차 확인이 없다.
- f15: 'ISO 22301:2019 기준(개정 1:2024 별도)'으로 판을 명시한다 — ISO 가 2024년 개정 1(기후 행동 변경)을 냈다.
- f21: 'EPCIS 1.2(2016-09-29) 기준'을 본문에 명시하고 현행 판에서의 유지 여부는 단정하지 않는다 — 현행 판 원문을 확인하지 않았다.
- f15·f16·f17: 기업 BCP·BCMS 체계는 ROP 직접 범위가 아니라 현장 제한 운영·수동 전환 계획의 참조 틀(연계 대상)로 짧게 서술하고, f17 은 감염병 대응 권고 가이드임을 밝힌다.
- f19·f20: 본문에서 [추정] 뒤에 '벤더 주장'을 병기하고, AutoStore 자체 제어기(XHandler)·통합업체 소프트웨어(SynQ)의 기능으로 서술하며 ROP 기능처럼 쓰지 않는다 — 두 출처는 서로 독립이 아니다.
- f18: 보상 트랜잭션 패턴을 물리 작업·재고 되돌림에 적용하는 문장은 [추정]으로 쓴다 — 출처는 소프트웨어 설계 패턴이다.
- ref-574: 기관 칸을 'Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH)'로 고친다 — 검색 결과로 저자를 확인했다.
- ref-580: URL 을 검색 결과로 확인한 https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp 로 고친다 — 브리프 URL 경로가 확인되지 않았다.
- 원문을 열지 못한 출처(ref-188, ref-572, ref-573, ref-574, ref-575, ref-576, ref-577, ref-579, ref-580, ref-581, ref-374)는 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. 발행일이 없는 ref-576·ref-579·ref-374 는 각주 발행일 자리에 '미확인'을 쓴다.
- 11절 열린 질문: oq-003·oq-021·oq-038·oq-048 은 해결로 바꾸지 않는다 — f10·f18·f21·f24 는 부분 근거일 뿐 답이 아니다.

## 검증 노트

판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. raw.githubusercontent.com 으로 연 출처(ref-031, ref-051, ref-004, ref-251, ref-537, ref-578)는 원문과 대조했고, 나머지는 검색 결과 일치로 확인했다. 확인 24건, 미확인 0건, 교차 확인 0건(VDA 5050 명세와 스키마, Open-RMF 문서들은 각각 발행 주체가 같아 독립 교차 확인이 아니다). 강등: 없음(f19·f20 은 이미 [추정]·벤더 주장). 원문 미열람 출처: ref-188(브리프의 ref-188, 기존 id 로 통합), ref-572, ref-573, ref-574, ref-575, ref-576, ref-577, ref-579, ref-580, ref-581, ref-374. 수정 사항: f2 connectionState 에 HIBERNATING 누락, f6 사용자 개입 결정은 통로 이탈 오류 문맥, ISO 22301 개정 1:2024 와 EPCIS 1.2 기준 판 명시, ref-574 저자·ref-580 URL 정정. 브리프 표시 불일치: f22 는 원문 미열람 출처(ref-573·ref-581)에 기대는데 source_unopened: false 로 적혀 있다. 해결 인정한 열린 질문 없음(oq-003·oq-021·oq-038·oq-048 은 부분 근거만 있음). 정정 요청 없음. 검증 검색 10회(리서치 20회와 합쳐 30/30, 상한 도달). 주의: 핵심 주장은 표준·오픈소스 문서 각각 한 곳에 기댄다. 연구 수치(f12)는 저자 보고값이다. 운반 중 고장 처리 흐름(f22)과 ROP 경계(f23)는 이를 한 절차로 정한 출처가 없는 종합 추정이다.
