# 1차 검증(브리프) 2026-09-25-06

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw.githubusercontent.com 의 main factsheet.schema 를 직접 열어 최상위 required 의 여섯 블록과 선택 블록 mobileRobotConfiguration 을 확인했다. 단일 발행 기관(VDA/VDMA). 스키마 발행일 미확인. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: loadSets 필드(setName~description, pickTime·dropTime 포함)가 스키마와 일치한다. 이 finding 은 백로그 q1-07 에도 답이 되지만 이번 실행 선택 질문이 아니다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: mobileRobotActions 의 필드와 actionScopes(INSTANT·NODE·EDGE·ZONE), blockingTypes(NONE·SOFT·SINGLE·HARD), actionParameters(key·valueDataType·description·isOptional)가 스키마와 일치한다. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: actionParameters 에 최소·최대 필드가 없는 것을 스키마에서 확인했다. '범위 정보는 흩어져 있다'는 해석이므로 [추정]을 유지한다. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: state.schema 의 actionStatus 일곱 값과 RETRIABLE·PAUSED·FAILED 설명이 일치한다. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: 필수 errorType·errorLevel, 선택 errorReferences·errorDescription(Translations)·errorHint(Translations), 등급 WARNING·URGENT·CRITICAL·FATAL 과 그 설명이 state.schema 와 일치한다. ref-022(2.0.0)는 원문 미열람이며 대비용이다. 같은 발행 기관이라 교차 확인이 아니다. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문과 main 명세를 다시 열어 pick 의 FINISHED(적재물이 로봇에 들어오고 새 적재 상태를 보고), FAILED(예: 스테이션이 예상과 달리 비어 있음), startCharging 의 FINISHED(powerSupply.charging true 보고)를 확인했다. pick 파라미터 목록도 표 4 와 일치한다. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: AMR_Interop_Standard.json 에서 identityReport·statusReport 필드와 operationalState 값을 확인했다. 스키마에 판 번호가 없어 판은 미확인이다. 백로그 q1-08 에도 답이 된다. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 IDTA 02020 README 를 raw 경로로 열어 능력 정의, 속성, 속성 제약(전제·불변·사후조건), 전이 제약, 스킬, 'reliable comparison', 1.0 첫 공식 판을 확인했다. 브리프는 이 출처를 fetched=false·source_unopened=true 로 기록했는데 self_check.limits 에는 '열었다'고 적었다. 표시가 서로 어긋난다(R-1). 발행일 미확인. |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: 템플릿 JSON 에서 CapabilitySet·CapabilityContainer·PropertySet·CapabilityRealizedBy·CapabilityComposedOf·CapabilityGeneralizedBy·SameProperty·ConstraintSet·PropertyConstraintContainer·TransitionConstraintContainer 와 semanticId 형식 https://admin-shell.io/idta/CapabilityDescription/<요소>/1/0 을 확인했다. 브리프의 fetched 표시는 f9 와 같은 방식으로 어긋난다. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: SOMA-ACT.owl 에서 ExecutionStateRegion, 여섯 ExecutionState 개체, 충족되지 않은 사후조건을 예로 드는 NonmanifestedSituation 설명을 확인했다. |
| f12 | 예 | 예 | 아니오 | 유지 | 확인: 노드셋 문서화 CSV 에 MotionDeviceSystemType·MotionDeviceType·ControllerType·TaskControlType·SafetyStateType·LoadType·OperationalModeEnumeration·ExecutionModeEnumeration 이 있다. 명세 본문은 아니다. |
| f13 | 예 | 예 | 아니오 | 유지 | f1~f11 을 종합한 추론이며 [추정]을 유지한다. IEEE 1872 계열·SSN·PDDL·KnowRob 행은 원문 미열람이라 q1-03 은 완결된 답이 아니다(required_fixes 참고). |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 6.2.3 에서 사전 정의 동작 규정과 추가 동작 문장을 확인했다. 두 출처가 모두 VDA 저장소라 독립 교차가 아니다. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 6.1.4.3 은 INVALID_ORDER_ACTION 을 level 'WARNING' 으로 보고하게 한다(예: 최대 리프트 높이 초과). 브리프가 '오류 등급 글자 단위 미확인'으로 남긴 값은 WARNING 으로 확인됐다. |
| f16 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문(튜토리얼 원본)에서 rmf_fleet actions: ["clean"], category·description, execute_action(category, description, execution), execution.finished() 를 확인했다. 선언에 파라미터 스키마·조건 항목이 없다. |
| f17 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과(arXiv 2209.09632, at 71(2))에서 OPC UA SkillType, 스킬 상태 기계(PackML 과 유사), ParameterSet 설명을 확인했다. 주장 범위가 스니펫 안에 있다. PreconditionCheck·ContextCheck 는 주장에 넣지 않았으므로 본문에도 쓰지 않는다. 기준일 2022. |
| f18 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과(reference.opcfoundation.org/specs/OPC-30050 6.3.5)에서 PackML 상태 기계가 모든 인스턴스에 AvailableStates·AvailableTransitions 를 요구함을 확인했다. '표준 명령 집합으로 옮긴다'는 부분은 스니펫에 직접 나오지 않지만 PackML 규격의 일반 목적 서술이다. 판·발행일 미확인. |
| f19 | 예 | 예 | 아니오 | 유지 | 확인: CaSkMan README 를 raw 로 열어 'alignment ontology' 문구, ISA 88 상태 기계와 REST·OPC UA 인터페이스 메서드를 확인했다. README 가 드는 정렬 대상에는 VDI 2206·WADL·OPC UA 도 있다. README 이므로 발행일 미확인. |
| f20 | 예 | 아니오 | 아니오 | 강등 | 원문 미열람. 검색 결과로 저자·학술지(at 71(2) 163–175, 2023), OPC UA 동반 규격 기반 정보 모델, 스킬로 운반 제어, AGV 는 VDA5050 에 따른 MQTT 로 둔다는 점, GetTransporter·ReleaseSpecificShuttle 을 확인했다. 그러나 '스킬을 운반 단위의 자기 기술 대안으로 논의'는 스니펫과 맞지 않는다(자기 기술은 PartnerRFIDTag 로 설명됨). 사실 → 추정. |
| f21 | 예 | 예 | 아니오 | 유지 | f3·f5·f14·f16 과 f9·f10·f17~f19 를 대응시킨 추론이다. 근거 finding 이 모두 확인돼 [추정] low 를 유지한다. |
| f22 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과(doi 10.3390/s17030569, Sensors 17(3) 569, 2017-03, 저자 Xin Li·Bilbao·Martín-Wanton·Bastos·Rodriguez)에서 정보 이질성 문제와 핵심 온톨로지가 임무·차량·통신·환경 도메인 온톨로지를 잇는 구조를 확인했다. 괄호 안 Position 예시는 스니펫에서 확인하지 못했다(required_fixes). |
| f23 | 예 | 예 | 아니오 | 유지 | 원문 미열람. IDTA 게시 URL(2024/06 IDTA-01001-3-0-1)이 실재하고, 모든 AAS 요소를 semanticId 로 주석한다는 점을 확인했다. ECLASS·IEC CDD 사전 참조는 관련 문서 스니펫(ZVEI 서브모델 템플릿, ECLASS·IDTA 안내)에서 확인했으며 메타모델 명세 본문의 구절은 미열람이다. 발행 2024. |
| f24 | 예 | 예 | 아니오 | 유지 | 확인: CaSkMan README 가 Cap:Capability 대신 하위 클래스(예: DIN8580:Fraesen)를 쓰라고 권한다. '기능 이름 대신 표준 분류 위치로 의미를 고정한다'는 해석 부분이다. |
| f25 | 예 | 예 | 아니오 | 유지 | 원문 미열람. arXiv 2306.07569 검색 결과(Dussard·Sarthou·Clodic, WOSRA 2023)에서 구성요소와 하위 능력으로 능력을 추론한다는 초록을 확인했다. v1 2023-06, v3 2025-09 개정. |
| f26 | 예 | 예 | 아니오 | 유지 | f10·f14·f22~f25 에서 도출한 추론이다. [추정] low 를 유지한다. 물류 AMR 의 '운반·도킹·리프트'를 직접 다룬 비교 자료는 없다. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | 참고문헌 id 충돌: 브리프의 ref-044·ref-045·ref-047·ref-048·ref-049·ref-050 이 참고문헌 목록에 이미 게시된 다른 출처(GS1 CBV.ttl·EPCIS.ttl, Open-RMF 메시지 3건, Oliot EPCIS)와 같은 id 다. ref-046·ref-051~ref-056 도 미게시 브리프 2026-09-25-04·05 가 쓴 id 와 겹친다, f1·f3 이 단계 1 페이지 q1-02 절의 기존 [추정]('agvGeometry' 등 팩트시트 블록, 판 미확인, ref-031)을 3.0.0 원문으로 대체한다. 이는 충돌이 아니라 판 차이다, f6 이 단계 1 페이지와 온톨로지 초안의 '3.0 새 오류 등급 CRITICAL·URGENT [추정][^ref-032]'과 오류 개념의 등급 속성(2.0.0 WARNING·FATAL)을 3.0.0 원문으로 보강한다. 2.0.0 서술은 ref-022 를 재사용한다, f17 이 실행 2026-09-25-02 의 f16(CSS 스킬 상태 기계, 출처 미확정)과 겹친다. 같은 ref-036 을 재사용한다, f9·f10 이 실행 2026-09-25-02 의 f17(IDTA 02020 구조, 제3자 논문 ref-037 경유)을 1차 자료로 대체한다. 기존 ConditionContainer 표기가 템플릿의 ConstraintSet·PropertyConstraintContainer 와 다르다, f8 이 백로그 q1-08 에, f1~f3 이 q1-07 에 답이 되지만 이번 실행의 선택 질문이 아니다 |
| 용어 일관성 | 아니오 | 용어집 'VDA 5050' 항목의 한 줄 정의가 규격이 아니라 팩트시트('차량이 자신의 기능 정보를 상위 관제에 미리 알리는 메시지')로 되어 있다. 이 정의가 새 용어 후보 '팩트시트'와 겹친다, 용어 후보 '자산관리셸(AAS)'과 기존 참고문헌 제목의 '자산관리쉘' 표기가 다르다(제목 인용은 원문 그대로 둔다) |
| 인용 길이·저작권 | 아니오 | ref-031 에서 직접 인용이 두 번 계획돼 있다(f14 의 추가 동작 문장, f15 의 'receives an order with actions it cannot perform'), ref-049 에서 직접 인용이 두 번 계획돼 있다(f19 'an alignment ontology that connects', f24 'use one of the many subclasses') |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- 참고문헌 id 충돌: 브리프의 새 출처 id 를 다음처럼 바꿔 각주·프런트매터 sources·reference_updates 에 일관되게 쓴다 — ref-044→ref-062, ref-045→ref-063, ref-046→ref-064, ref-047→ref-065, ref-048→ref-066, ref-049→ref-067, ref-050→ref-068, ref-051→ref-069, ref-052→ref-070, ref-053→ref-071, ref-054→ref-072, ref-055→ref-073, ref-056→ref-074. 기존 ref-044~ref-050 페이지(GS1·Open-RMF·Oliot)를 덮어쓰지 않는다. 이유: 게시된 참고문헌과 미게시 브리프 2026-09-25-04·05 의 id(최대 ref-061)와 겹친다. 재사용 출처 ref-022·ref-031·ref-036·ref-040 은 그대로 쓴다.
- q1-03: '답함'으로 바꾸지 않고 '부분 답'(남는 finding: f1~f13)으로 처리한다 — 백로그 '조사 중', 단계 페이지 2절 '열림', answer_link null. 이유: IEEE 1872 계열·SSN·PDDL·KnowRob 행의 다섯 정보 항목이 원문 미열람·미조사라고 브리프 자체가 적었다. 3절 q1-03 소제목에는 명시 id 를 붙이지 않고 '(부분 답)'을 유지한다.
- q1-04·q1-05 는 '답함'으로 처리하고 3절에 '### q1-04 … {#q1-04}', '### q1-05 … {#q1-05}' 소제목을 둔다. 결론 문장 f21·f26 은 [추정]으로 둔다.
- f20: [사실] → [추정]으로 강등하고 '스킬을 운반 단위의 자기 기술 대안으로 논의' 구절은 뺀다 — 검색 요약에서 자기 기술은 PartnerRFIDTag 로 설명되어 주장과 맞지 않는다. 저자·학술지 at 71(2) 163–175(2023), VDA 5050 MQTT 병행, GetTransporter·ReleaseSpecificShuttle 은 쓸 수 있다.
- f22: 괄호 안 예시(한 로봇의 Position 은 지역 좌표, 다른 로봇은 각도 좌표)를 본문에 쓰지 않는다 — 검증 검색 요약에서 확인되지 않았다. 저자는 'Li, X. 외'로 둔다.
- f15: 오류 등급을 쓸 때 'WARNING'으로 적는다(입력 원문 6.1.4.3 에서 확인). '미확인'으로 두지 않는다.
- 인용: ref-031(새 id 그대로)의 직접 인용은 f14·f15 가운데 하나만, ref-049(새 id ref-067)의 직접 인용은 f19·f24 가운데 하나만 쓰고 나머지는 재서술한다 — 5.3 출처당 1회 규칙.
- 단계 1 페이지 q1-02 절: 기존 '팩트시트는 … agvGeometry … 블록으로 구성되는 것으로 보인다(판 미확인) [추정][^ref-031]' 문장을 f1 의 3.0.0 서술([사실], 3.0.0 main 기준, 기준일 2026-09-25)로 바꾸고 2.0.0 의 agvGeometry 명칭은 '2.0.0 과 필드 대조 미실시'로 남긴다. 두 서술을 같은 판처럼 병치하지 않는다. 기존 '새 오류 등급 CRITICAL·URGENT [추정][^ref-032]'은 f6 을 근거로 [사실]과 state.schema 각주를 더해 서술하되 ref-032 문장의 태그는 올리지 않고 f6 문장을 별도로 둔다.
- 모델·표준 비교표: IDTA 02020 칸의 기존 'ConditionContainer'(ref-037 경유) 표기를 f10 의 ConstraintSet·PropertyConstraintContainer·TransitionConstraintContainer 로 바꾸고 칸 상태는 브리프 기록대로 '원문 미열람'을 유지한다. VDA 5050·MassRobotics·SOMA·OPC UA Robotics·Open-RMF 행 가운데 fetched=true 출처(ref-031·ref-040·ref-044→062·ref-045→063·ref-048→066·ref-050→068·ref-051→069)만 쓴 칸은 상태를 '확인'으로 할 수 있다. CaSkMan·OPC 30050 PackML 은 '후보 밖'으로 근거 finding id 와 함께 행을 추가한다.
- 각주 원문 미열람 표기: 브리프에서 source_unopened: true 인 출처(ref-022, ref-036, ref-046→064, ref-047→065, ref-052→070, ref-053→071, ref-054→072, ref-055→073, ref-056→074)는 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates[].source_unopened: true 로 둔다. 이전 실행에서 '(원문 미열람)'이던 ref-031·ref-040 은 이번 실행에서 원문을 열었으므로 이 페이지의 각주에서 그 표기를 뺀다.
- 온톨로지 초안: 승인한 변경 6건만 반영하고 버전을 '0.1' → '0.2'로 올린다(H1 '(v0.2)', 프런트매터 ontology_version, track_updates.ontology_draft_version). 개념 '오류' 등급 속성에 WARNING·URGENT·CRITICAL·FATAL(3.0.0)과 errorReferences·errorHint 추가(f6) — 2.0.0 WARNING·FATAL 도 병기한다. 새 개념 '실행 상태'(f5·f11, 보조 f18)를 '확정'으로 넣는다. 새 관계 '스킬 / 실행 상태를 드러낸다 / 실행 상태'(f19, 보조 f17·f18), '기능 / 일반화된다 / 기능'(f10·f24), '기능 / 구성된다 / 기능'(f10)을 넣는다. 개념 '기능' 속성에 '의미 참조'(f14·f23·f24)를 더한다. 4절 다이어그램도 함께 고친다.
- 온톨로지 초안: '제약' 개념 수정(속성 제약·전이 제약 종류 추가, f9)은 반영하지 않고 6절 미해결 모델링 질문으로 둔다 — 전제조건을 제약의 한 종류로 둘지 실행 조건으로 둘지 정하는 기존 6절 질문과 충돌한다. 6절의 '스킬 상태 기계 속성' 항목은 새 관계로 다뤘음을 적고 갱신한다.
- 새 질문 'VDA 5050 사전 정의 동작과 IDTA 02020 능력·VDI 2860 취급 분류 매핑 …'(단계 4, f21)은 q4-06 과 뜻이 겹치므로 backlog_updates 에 새로 넣지 않는다. 필요하면 q4-06 의 조사 메모로만 남긴다.
- 새 질문 'VDA 5050 3.0.0 팩트시트 동작 파라미터에 허용 범위 필드가 없을 때 제조사는 … 어디에 적는가'(f4)의 단계를 1 → 2 로 고친다 — 제조사가 실제 문서·팩트시트에 정보를 어떻게 싣는지 묻는 질문이라 단계 2. 로봇 문서 유형과 정보 구조 조사에 속한다.
- 용어집: 'VDA 5050' 항목(glossary_updates action: update)의 정의를 '독일자동차산업협회(VDA)와 VDMA가 정한 이동로봇과 상위 관제(fleet control) 사이의 통신 인터페이스 권고안이다'로 고친다(근거 ref-031 원문 1·2장). 새 용어 '팩트시트'는 브리프 정의로 등록하되 '차량' 대신 '이동로봇'을 쓴다. '자산관리셸'·'의미 식별자'는 새 용어로 등록한다.
- corr-001 미처리 — 이번 실행의 대상 페이지(7. 화물·재고·자산 식별과 추적)가 아니므로 다음 갱신 실행으로 넘긴다. corrections_applied 에 넣지 않는다.
- 단계 페이지 6절·상태 줄: 완료 조건은 두 항목 모두 '미충족', 전환 '아니오(비교표의 IEEE 1872 계열·SSN·PDDL·KnowRob 행 다섯 정보 항목 미조사, ROP용 능력 개념 요구 목록 초안 미반영, 막힌 질문 q1-03·q1-06·q1-07·q1-08)'로 적는다. 상태 줄 숫자는 답함 4건(q1-01·q1-02·q1-04·q1-05)과 열린 질문 수를 백로그와 맞춘다.

## 검증 노트

판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. GitHub 공식 저장소 원문은 검증자가 직접 열어 대조했다. 확인 25건, 미확인 1건(f20), 교차 확인 0건(모든 핵심 사실이 발행 기관 한 곳의 산출물). 강등: f20 사실 → 추정. 원문 미열람 출처: ref-022, ref-036, ref-052, ref-053, ref-054, ref-055, ref-056(새 id ref-070~ref-074), ref-046·ref-047(새 id ref-064·ref-065; 브리프는 미열람으로 기록했으나 self_check 에는 '열었다'고 적어 표시가 어긋난다. 검증자가 raw 경로로 내용을 확인했다). 주의: 새 출처 id 가 게시된 참고문헌 ref-044~ref-050 및 다른 미게시 브리프와 충돌해 ref-062~ref-074 로 재부여를 지시했다. pipeline 담당은 next_ref_id 산출을 점검해야 한다. q1-03 은 IEEE 1872 계열·SSN·PDDL·KnowRob 행이 미조사라 부분 답으로 처리한다. q1-04·q1-05 는 답함이며, 결론 부분(f21·f26)은 추정이다. 한국 자료는 찾지 못했다. corr-002 불인정: 분류 원문 정의는 정정 대상이 아니다. corr-001 은 대상 페이지 밖이라 미처리. 미사용 출처: 없음. 온톨로지 변경 승인: 오류 수정(f6), 실행 상태 추가(f5·f11·f18), 스킬 / 실행 상태를 드러낸다 / 실행 상태(f19·f17·f18), 기능 / 일반화된다 / 기능(f10·f24), 기능 / 구성된다 / 기능(f10), 기능 속성 '의미 참조' 추가(f14·f23·f24) → v0.2. 거부: 제약 종류 수정(f9) — 6절 전제조건 질문과 충돌해 미해결 모델링 질문으로 이동. 백로그 중복: f21 새 질문은 q4-06 과 중복. 단계 태그 수정: f4 새 질문 단계 1 → 2. 단계 완료 조건: 미충족(부족: 비교표 IEEE 1872 계열·SSN·PDDL·KnowRob 행의 다섯 정보 항목, ROP용 능력 개념 요구 목록 초안). 단계 전환: 미승인(막힌 질문 q1-03·q1-06·q1-07·q1-08).

## 트랙 추가 검증

| 항목 | 결과 |
|---|---|
| 표준 출처(발행 기관 자료) | 예 |
| 벤더 주장 표기 | 예 |
| 온톨로지 변경 근거 | 아니오 |
| 백로그 중복 질문 | VDA 5050 사전 정의 동작(pick, drop, startCharging 등)과 IDTA 02020 능력·VDI 2860 취급 분류를 대응시키는 매핑 규칙을 만들 수 있는가, 제조사 추가 동작은 어떻게 처리하는가? (q4-06 과 중복) |
| 단계 태그 문제 | VDA 5050 3.0.0 팩트시트의 동작 파라미터에 허용 범위 필드가 없을 때, 제조사는 리프트 높이 같은 동작 한계를 물리 파라미터·적재 명세의 최소·최대 필드와 자유 문장 설명 가운데 어디에 적는가? → 단계 2 |
| 완전성 표현 | 예 |
| 단계 완료 판정 | 미충족 |
| 단계 전환 승인 | 아니오 |
