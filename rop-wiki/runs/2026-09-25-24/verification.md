# 1차 검증(브리프) 2026-09-25-24

**판정: 조건부 승인** · 신뢰도: low

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문(data/source_texts/ref-031, VDA 5050 Version 3.0.0) 6.6 State 에 'published when relevant events occur or at least every 30 seconds'. 단일 발행 주체. 3.0.0 발행일은 oq-005 출처 충돌로 미확인이므로 기준일은 확인일과 판(3.0.0)으로 적는다. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: ref-031 4.1(connection 만 QoS 1, order·instantActions·state·factsheet·zoneSet·responses·visualization 은 QoS 0), 6.5(last will connectionState CONNECTION_BROKEN, retained), 6.2.3 startHibernation(HIBERNATING 연결 상태). 단일 출처. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: 6.5 에 'the timestamp and headerId fields will always be outdated' 원문 있음. 2장 Scope 가 교통 관리 로직 등을 범위 밖으로 둔다. 오래된 상태 대응 규정의 '부재'는 입력 원문이 110,737자까지만 발췌돼 전문 대조 불가 — [추정] 유지, '이번 열람 범위에서' 한정 표현 필수. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: raw state.schema 열람. timestamp date-time, lastNodeId, mobileRobotPosition(mapId·localized·localizationScore 0.0~1.0·deviationRange), loads, safetyState 모두 있음. localized 설명 원문 일치. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: raw robot_state.json 열람. unix_millis_time 정수, status 7종, issues(category·detail), battery 'State of charge of the battery' 0~1. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: raw integration_doors.md(/door_states 발행, state supervisor 문구, 직접 요청 negate 후 이전 상태 복귀)와 DoorState.msg(door_time·door_name·current_mode). 두 출처 모두 Open Robotics 계열이라 독립 교차 아님. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: raw LiftState.msg(lift_time, current/destination_floor, door_state, motion_state MOTION_UNKNOWN 포함, current_mode HUMAN·AGV·FIRE·OFFLINE·EMERGENCY — 화재·오프라인·비상은 읽기 전용, session_id)와 integration_lifts.md('keeping track of the internal and desired state of the lift'). 같은 발행 주체. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: 두 문서 재열람에서도 발행 주기·오래됨 기준 언급 없음. 구현 코드 미확인이므로 부재 확정이 아닌 [추정] 유지. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: raw ros2_documentation jazzy About-Quality-of-Service-Settings.rst 열람. Deadline·Lifespan('stale or expired')·Liveliness·Lease Duration 정의와 deadline missed·liveliness lost/changed 이벤트 일치. Jazzy 판 기준임을 명시. |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: raw Sparkplug 5장 열람. NDEATH·서버 연결 상실 시 STALE, seq 0~255, Reorder Timeout(SHOULD) 만료 시 'Node Control/Rebirth' NCMD(MUST) 원문 일치. |
| f11 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검증 검색 결과(OPC 10000-4 7.11 및 v105 참조)에서 sourceTimestamp=값·statusCode 마지막 변경 시각(UTC, 원천 가까이 같은 물리 시계), serverTimestamp=서버가 값을 받았거나 정확하다고 안 시각, StatusCode=품질·상태 확인. 판(1.05 등) 미확인. |
| f12 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과로 IEEE JSAC 39(5), 1183-1210, 2021-05, DOI 10.1109/JSAC.2021.3065072 확인, 초록 내용 일치. as_of 는 '2021' 이 아니라 '2021-05'로 적는다. |
| f13 | 예 | 예 | 아니오 | 유지 | 여러 출처를 SCM 질문에 대응시킨 추론. 허용 경과 시간 값을 정한 출처 없음. [추정] 유지, 권고 문장이 아니라 추론임을 드러낼 것. |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: raw EPCIS.ttl(버전 2.0, 수정 2021-09-30) eventTime·recordTime·eventTimeZoneOffset 주석 일치. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: EPCIS.ttl errorDeclaration·declarationTime·correctiveEventIDs·reason, CBV.ttl did_not_occur('There are no corrective events')·incorrect_data 정의 일치. 같은 GS1 저장소라 독립 교차 아님. |
| f16 | 예 | 예 | 아니오 | 유지 | f15 구조를 로봇 상태 이력에 옮긴 추론. [추정] 유지. |
| f17 | 예 | 예 | 아니오 | 유지 | 검증 에이전트가 raw sosa.ttl(w3c/sdw gh-pages 작업반 편집본)을 열어 phenomenonTime('Not necessarily the same as the resultTime')·resultTime 정의 확인. 다만 ref-030 의 URL 은 /TR 권고안이고 편집본은 official_artifact 라 권고안 원문은 미열람. 브리프는 ref-030 에 fetched:false 이면서 fetch_url 을 적고 summary 에 '확인했다'고 써 표시가 어긋남. |
| f18 | 예 | 예 | 아니오 | 유지 | f11·f14·f17 대응 추론. 세 표준 정의가 서로 다르다는 한계 문구 유지. [추정]. |
| f19 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 ref-004(rmf-core.md) 'a living database ... delays, cancellations, or route changes', conflict notice 와 협상, 제3자 판정자 일치. |
| f20 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과로 Management Science 54(4) 627-641, 약 37만 건·37개 매장·65% 부정확, 실사가 줄이고 매장 환경 복잡성·유통 구조가 늘린다는 초록 확인. 여러 사이트가 같은 초록이라 독립 교차 아님. 소매 매장 조건임을 본문에 명시. |
| f21 | 예 | 예 | 아니오 | 유지 | f20·f4 대응 추론. [추정] 유지. 근거 출처 ref-388 이 원문 미열람인데 브리프 source_unopened:false 로 적힘(표시 누락). |
| f22 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과로 Massawe·Kinyua·Vermaak, Sensors 12(4) 4187-4212, 2012, WSTD 제안 확인. '약 30%' 수치는 검증 검색 요약에 재현되지 않아 리서치 스니펫 범위이며 저자 보고값·조건 미확인 표기 필수. |
| f23 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과(arXiv 1805.06358, 2018-05-16) 초록의 두 성질 일치. |
| f24 | 예 | 예 | 아니오 | 유지 | f23·f6·f7 대조 추론. [추정] 유지. ref-391 원문 미열람인데 source_unopened:false 로 적힘. |
| f25 | 예 | 예 | 아니오 | 유지 | 원문 미열람(표준·NIST 해설 모두). 검색 결과로 정의 문구('fit for purpose digital representation ... with synchronization')와 참조 구조 존재는 확인. '데이터 수집·장치 제어 도메인과 핵심 도메인' 구분과 관측 요소 8종 목록은 검증 검색에서 재확인 못함 — 본문에서 도메인 이름은 빼거나 미확인 표시. |
| f26 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과로 IFAC-PapersOnLine 2018, DM·DS·DT 구분, DS='automated one-way data flow', DT 문헌 'scarce' 확인. 용어 후보 '디지털 섀도' 정의도 이 검색 결과로 뒷받침됨. |
| f27 | 예 | 예 | 아니오 | 유지 | f25·f26 과 분류 원문 7장 주석 대응 추론. [추정] 유지. 제조 대상 출처임을 명시. |
| f28 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과(KCI·DBpia)로 서지(한국CDE학회 논문집 26(4) 313-323, 2021, 저자 6인) 확인. 내용(설계 가상 검증·운영 실시간 모니터링)은 리서치 스니펫 범위. |
| f29 | 예 | 예 | 아니오 | 유지 | 원문 미열람. KCI 실재 확인. 게재지는 검색 요약이 '지능정보논문지'로, KoreaScience 는 한국인터넷방송통신학회논문지로 적고 DOI 는 10.7236/JIIBC.2023.23.4.189 — 충돌은 한쪽을 고르지 않고 열린 질문 유지. 제조 대상. |
| f30 | 예 | 예 | 아니오 | 유지 | f28 대응 추론. [추정] 유지. 논문 본문의 기능 구분 방식은 미확인. |
| f31 | 예 | 예 | 아니오 | 유지 | '연계 대상:' 표시된 경계 추론. 기존 oq-028(위치추정 신뢰도의 공통 수용 기준, 6·8 영역)과 직접 겹침. |
| f32 | 예 | 예 | 아니오 | 유지 | 분류 원문 9장과 대응한 경계 추론. [추정] 유지. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | f31 과 기존 열린 질문 oq-028(제조사마다 다른 위치추정 신뢰도의 공통 수용 기준, 관련 영역 6·8) — 11절에서 새 질문을 만들지 말고 oq-028 에 연결, 브리프 gaps 가 oq-024 를 이 영역 질문으로 들었으나 open_questions_new·page_proposals 에 연결 방법이 없음 — 11절에 oq-024 연결, f4(localizationScore·mapId)는 6. 지도·공간·위치 모델 페이지가 이미 ref-051 로 다룬 내용 — 기존 각주 ref-051 재사용, 이전 실행 2026-09-25-18 브리프가 같은 출처에 ref-182~ref-196 을 제안했으나 참고문헌 목록에 없음 — 이번 ref-378~ref-392 가 유일한 번호가 되도록 퍼블리셔가 이중 등록을 확인 |
| 용어 일관성 | 예 | — |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- 각주 정의: 원문을 열지 않은 출처 ref-030(W3C /TR 권고안), ref-384, ref-385, ref-386, ref-387, ref-388, ref-389, ref-390, ref-391, ref-392 의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — 이 출처들은 fetched:false 다. github_raw 로 연 ref-004·031·044·045·051·148·378~383 에는 붙이지 않는다.
- f17·ref-030: 본문에서 SOSA 시각 정의는 'W3C/OGC 작업반 저장소 편집본 기준(권고안 문구와 다를 수 있음)'으로 밝히고 각주는 ref-030 에 (원문 미열람)을 붙인다 — 권고안 URL 자체는 열지 않았다.
- f1·f2·f3·f4: VDA 5050 문장마다 '3.0.0 판(공식 저장소 main) 기준, 확인일 2026-09-25'를 남긴다 — 3.0.0 발행일은 oq-005 출처 충돌로 미확인이다.
- f3·f8: '규정이 없다'고 단정하지 말고 '이번에 연 문서 범위에서 찾지 못했다'로 쓰고 [추정]을 유지한다 — 전문 대조나 구현 코드 확인이 아니다.
- f12: 기준일을 2021 이 아니라 2021-05(IEEE JSAC 39(5))로 적는다.
- f20: 65% 수치에 '한 소매업체 37개 매장 조건이며 물류센터 값이 아니다'를 같은 문장에 붙인다 — 5절 보충 시나리오에서도 소매 자료의 유추임을 밝힌다.
- f22: '약 30%'는 '저자 보고값(실험 조건 미확인)'으로 표기한다 — 검증 검색에서 수치를 재현하지 못했다.
- f25: ISO 23247 참조 구조의 도메인 이름(데이터 수집·장치 제어 도메인, 핵심 도메인)과 관측 요소 8종 나열은 빼거나 '미확인'으로 표시하고, 정의 문장(동기화된 목적 적합 디지털 표현)과 참조 구조 존재만 [사실]로 쓴다 — 검증 검색은 정의와 참조 구조 존재만 확인했다.
- f28·f30: 8절·10절에서 이동건 외(2021)의 '설계 단계 가상 검증' 부분은 22. 시뮬레이션·예측용 디지털 트윈 쪽 기능으로 10절 연결에만 두고, 8. 실시간 세계 상태·데이터 일관성 본문에는 '운영 중 실시간 모니터링' 부분만 둔다 — 분류 원문 7장의 현재 상태 표현/가정한 미래 실험 구분.
- f29: 게재지 이름을 본문·각주에 단정해 적지 말고 '게재지 미확인(열린 질문)'으로 두고, 출처 충돌 열린 질문에는 KCI·KoreaScience 표기 차이를 한쪽 선택 없이 그대로 둔다.
- 11절: f31 의 위치 신뢰도 판단 문제는 새 질문으로 만들지 말고 기존 oq-028 에 연결하며, oq-024(선언 능력 대 관측 운용 능력)도 이 영역 관련 질문으로 연결한다 — 두 질문 모두 관련 영역에 8. 실시간 세계 상태·데이터 일관성이 이미 있다.
- 직접 인용: ref-031(f1 의 'published when relevant events occur or at least every 30 seconds'와 f3 의 'will always be outdated')과 ref-045(f14·f15)는 페이지에서 출처당 한 번만 원문 구절로 인용하고 나머지는 재서술한다 — 5.3 출처당 1회 규칙.
- 4절 용어: 새 용어 '디지털 섀도'는 기존 용어집 '디지털 트윈'과 구분되는 별도 항목으로 두고 정의 끝에 Kritzinger 외(2018) 분류 기준임을 밝힌다; '오류 선언'은 기존 EPCIS 용어 페이지와 연결한다.
- f2·f10(연결 끊김·STALE)은 19. 모니터링·이상 탐지·원인 분석과 10절에서 연결만 하고, f6·f7 의 문·승강기 제어 자체는 10. 설비·건물 시스템 연동의 연계 대상으로만 짧게 쓴다 — 분류 원문 9장 '시설·설비 제어' 경계.

## 검증 노트

판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다: 일반 웹 페이지는 열지 못했고 GitHub 공식 저장소 원문과 입력 원문 텍스트만 열었다. 확인 32건, 미확인 0건, 교차 확인 0건. 강등: 없음(단, f25 는 ISO 23247 도메인 이름을 빼고 정의만 [사실]로 쓰도록 축소 지시). 원문 미열람 출처: ref-030(W3C 권고안; 작업반 편집본 sosa.ttl 로 정의만 확인), ref-384, ref-385, ref-386, ref-387, ref-388, ref-389, ref-390, ref-391, ref-392. 원문 확인 출처: ref-004·ref-031(입력 원문), ref-044·ref-045·ref-051·ref-148·ref-378·ref-379·ref-380·ref-381·ref-382·ref-383(github_raw 재열람). 브리프 표시 문제: ref-030 이 fetched:false 이면서 fetch_url 과 '확인했다' 요약을 가짐, f21·f24 가 원문 미열람 출처(ref-388·ref-391)에 기대면서 source_unopened:false. 주의: 핵심 주장(3·6·9절)의 절반 이상이 표준 조각을 대응시킨 [추정]이다. 특히 분류 원문 질문(30초 전 문 상태)에 대한 답인 f13 은 허용 경과 시간 값을 정한 출처가 없는 추론이다. 모든 사실 주장은 발행 주체 한 곳의 자료다. 재고 부정확 65%는 소매 매장 값이고, 디지털 트윈 분류 자료는 제조 대상이다. 김지형(2023)의 게재지는 출처 충돌로 미확인이다. 검증 검색 9회 사용(리서치 16회와 합쳐 25/30). 정정 요청 없음.
