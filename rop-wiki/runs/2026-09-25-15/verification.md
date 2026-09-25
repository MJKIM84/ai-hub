# 1차 검증(브리프) 2026-09-25-15

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: factsheet.schema 원문(raw.githubusercontent.com)을 검증자가 직접 열었다. 필수 블록 11개(headerId·timestamp·version·manufacturer·serialNumber·typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification)와 두 설명 문구가 일치한다. 규격 원문 단일 출처이며 발행일은 미확인(확인일 기준). |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: loadSets 의 loadType('EPAL, XLT1200' 예시), maximumWeight, 최소·최대 적재 처리 높이, pickTime·dropTime(대략 소요 시간, 초)이 원문과 일치한다. 페이지에서는 pickTime·dropTime 을 '대략의 소요 시간'으로 적는 것이 원문에 더 가깝다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: actionType·actionDescription(자유 문장)·actionScopes(INSTANT·NODE·EDGE·ZONE)·actionParameters(key·valueDataType·isOptional, 선택 필드 description)·pauseAllowed·cancelAllowed 가 원문과 일치한다. valueDataType 6개 값도 일치한다. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: 원문에서 actionParameters 에 값 범위·전제조건 필드가 없음을 검증자도 확인했다. '흩어져 기술될 것'은 추론이므로 [추정]을 유지한다. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: AMR_Interop_Standard.json 원문에 maxSpeed·maxRunTime·chargerType·cargoType('Discription of cargo')·cargoMaxVolume·cargoMaxWeight·productDocumentation, operationalState 9개 값, loadPercentageStillAvailable(0~100)이 있다. 발행일 미확인. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: 두 원문에서 loadType 은 예시만, cargoType 은 설명 한 줄만 있고 어휘를 지정하지 않는다. 공통 어휘가 별도로 있는지는 확인하지 않은 추론이므로 [추정]을 유지한다. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: config.yaml 원문의 task_capabilities 주석, loop·delivery 활성화, actions(자리표시 예시), finishing_request(park·charge·nothing)가 일치한다. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: 입력 data/source_texts/ref-040.txt 원문에 actions: ["clean"], category·description 호출, is_command_completed() 확인 뒤 execution.finished() 호출이 있다. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: IDTA 02020 README 를 검증자가 raw 경로로 열어 구현 독립 기능 명세, 속성 예(최대 속도·허용 오차·온도 범위), 속성 제약(전제·불변·사후조건), 전이 제약(순서·병렬), 스킬, 'reliable comparison between required and provided capabilities', 1.0 첫 공식판을 확인했다. 브리프는 ref-229 을 fetched false 로 적었지만 근거 발췌는 'README 원문'이라 서로 맞지 않는다. 검증자는 신뢰도를 올리지 않으므로 medium 을 유지한다. |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: IDTA README(구현 독립 명세, 스킬은 능력의 구현)와 CaSkMan README(스킬 = OPC UA 등 호출 인터페이스를 가진 캡슐화된 구현, CSS 참조 모델 기반)는 핵심 구분을 뒷받침한다. 다만 IDTA README 에서 CSS 계열이라는 문구는 확인하지 못했고, ref-035 는 원문 미열람이다. 두 저장소 모두 헬무트 슈미트 대학(HSU) 연구진이 관여해 독립성이 약하므로 cross_checked 는 false 로 둔다. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: CaSkMan README 원문에 VDI 3682(공정 입출력), VDI 2860(취급 작업), DIN 8580(제조 공정), ISA 88(상태 기계), IEC 61360(속성 형식 기술), WADL·OPC UA 가 있다. |
| f12 | 예 | 예 | 아니오 | 유지 | 확인: IDTA 02047 README 를 검증자가 열어 목적 문구, 1.0 첫 공식판, AAS 메타모델 3.0 호환을 확인했다. 세부 필드는 README 에 없다(브리프 기록과 같음). 브리프는 fetched false 로 적었으므로 medium 을 유지한다. |
| f13 | 예 | 예 | 아니오 | 유지 | 확인: ssn-system.ttl 원문에 SystemCapability·OperatingRange·SurvivalRange·Condition·hasSystemCapability·inCondition 이 정의돼 있다. 발췌 인용은 원문('If, however, the SurvivalRange is violated, the System is "damaged" and SystemCapability specifications may no longer hold.')에서 'however'와 따옴표가 빠져 글자 단위로 다르다. 작업반 편집본이며 /TR 권고안(ref-030, 2017-10-19)과의 일치는 미확인. |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: SOMA README 원문에 활동 온톨로지, DUL 기반 OWL 구현, 의도·계획·움직임·접촉이 있다. ref-028 논문은 원문 미열람이며 서지만 재인용했다. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인하되 문구 수정 필요: README 는 기능(function)·기능 실행·상호작용·환경을 기술하고 '두 상위 온톨로지 DUL 과 SUMO 가 쓰인다'고 하지만, SUMO 는 OWL 표현이 없어 이 구현과 매핑에서 제외했다고 밝힌다. 따라서 'DUL·SUMO 로 확장하는 구현'은 부정확하다. 대상 표준도 IEEE 1872 가 아니라 IEEE 1872.2 다. IEEE 공식 산출물이라는 표시는 없다(제3자 구현). |
| f16 | 예 | 예 | 아니오 | 유지 | 확인(제목 수준): ref-025 는 참고문헌 목록에 있는 기존 출처이고 용어집 CORA 항목과 같은 근거다. 원문 미열람, 이번에는 다시 검색하지 않았다. 발행 2015 로 2년이 넘었으므로 월간 재검증 대상이다. |
| f17 | 예 | 예 | 아니오 | 유지 | 확인(서지 수준): ref-027 은 기존 참고문헌이며 제목과 주장이 일치한다. 원문 미열람(재인용). |
| f18 | 예 | 예 | 아니오 | 유지 | 확인(서지 수준): ref-029 는 기존 참고문헌이며 용어집 PDDL 정의와 같다. 원문 미열람(재인용). |
| f19 | 예 | 예 | 아니오 | 유지 | 확인: 검색 결과(Nature·PMC)에서 Scientific Reports 15권 34326, 저자 Naqvi·Sarkar·Ameri·Elmhadhbi·Louge·Karray, RCO 가 제조사가 명시한 광고 능력(advertised)과 실제 성능을 반영한 운용 능력(operational)을 정의한다는 점을 확인했다. 원문 미열람. |
| f20 | 예 | 예 | 아니오 | 유지 | 확인(제목 수준): ref-042 는 기존 참고문헌이다. 원문 미열람(재인용), 이번에는 다시 검색하지 않았다. |
| f21 | 예 | 예 | 아니오 | 유지 | 확인(제목 수준): ref-038 은 기존 참고문헌(arXiv 2209.10900)이다. 원문 미열람(재인용). |
| f22 | 예 | 예 | 아니오 | 유지 | 확인(서지 수준): ref-043 은 기존 참고문헌(KCI)이며 게재 사실만 뒷받침한다. 능력 기술 포함 여부는 미확인이라고 페이지에 적어야 한다. 원문 미열람. |
| f23 | 예 | 예 | 아니오 | 유지 | 확인: 검색 결과에서 Electronics 15(16) 3562(2026-08-11), 로봇·작업·장소 의미 모델, 선언적 추론과 절차적 평가의 혼합, 다축 능력 조건과 적재 상태 장소 도달 가능성, 공통 입력 ReasonerOutput, 할당기 4종 실험을 확인했다. 저자 미확인, 원문 미열람. |
| f24 | 예 | 예 | 아니오 | 유지 | 확인: 검색 결과에서 CAPILANO(Protégé OWL), SPARQL 질의, 가용성을 고려한 연속 작업 배정(Python), 라인리스 이동 조립 시스템(LMAS) 적용, 2022년 MHI Colloquium·WGMHI 연보 게재를 확인했다. 브리프의 ref-237 published null 은 2022 로 고칠 수 있다. 제조 조립 대상이며 물류 사례가 아니다. 원문 미열람. |
| f25 | 예 | 예 | 아니오 | 유지 | 확인: arXiv 2404.17524 검색 결과에서 저자 Vieira da Silva·Köcher·Gehlhoff·Fay, ETFA 2024, RDF 구문 검사·OWL 추론·SHACL 기반 반자동 품질 검사, 'almost free of errors'를 확인했다. 저자 보고 결과이며 원문 미열람. |
| f26 | 예 | 예 | 아니오 | 유지 | 확인: arXiv 2606.17073 검색 결과에서 Dussard·Sarthou(LAAS-CNRS), URDF 에서 LLM 으로 온톨로지 채우기, 여러 질의의 다수결과 구문·스키마 수준 검증, ICSR 2026(2026-07, 런던) 채택을 확인했다. 원문 미열람. |
| f27 | 예 | 예 | 아니오 | 유지 | 확인: ISO 소개 요약에서 모듈 공통 정보 모델(CIM)의 구조와 속성·하위 클래스의 쓰임과 의미, 상호운용성·재사용성·조립 가능성을 확인했다. 발행 2024-02(1판), 원문 미열람. Part 202:2025 는 소프트웨어 모듈 정보 모델이다. |
| f28 | 예 | 예 | 아니오 | 유지 | 확인: KSSN 검색 결과의 표제가 일치한다. 제정일과 ISO 22166-202 부합 여부는 미확인이다. 국내가 ISO 에 먼저 제안했다는 기사가 있으나 브리프 밖 내용이라 페이지에 쓰지 않는다. 원문 미열람. |
| f29 | 예 | 예 | 아니오 | 유지 | 확인: f2·f3·f5·f23 의 확인된 내용에서 도출한 추론이므로 [추정]을 유지한다. 분류 원문 SCM 관점 질문에 대응한다. |
| f30 | 예 | 예 | 아니오 | 유지 | 확인: f3·f8(이름 기반 선언·호출)과 f9·f11(능력–스킬–상태 기계)에서 도출한 추론이므로 [추정]을 유지한다. |
| f31 | 예 | 예 | 아니오 | 유지 | 확인: f25·f26 두 연구 모두 생성 뒤 형식 검증을 둔다는 점은 검색 결과로 확인했다. 물류 매뉴얼 사례는 없으므로 [추정]을 유지한다. |
| f32 | 예 | 예 | 아니오 | 유지 | 확인: '연계 대상:'으로 표시돼 있고 분류 원문 9장의 로봇 자체 지능·제어 경계와 맞는다. 추론이므로 [추정]을 유지한다. |
| f33 | 예 | 예 | 아니오 | 유지 | 확인하되 문구 수정 필요: arXiv 2501.08726 검색 결과에서 저자, 에너지 소비와 필요 로봇 수 최소화, AI 기반 방법을 포함한 최적화 알고리즘 검토를 확인했다. 그러나 '의료·물류 등에서 쓰이는'은 검색 결과와 브리프 발췌 어디에도 없다. 원문 미열람. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 예 | 용어집 VDA 5050 항목(현행판 3.0.0)과 f1~f3 의 3.0.0 판 기술이 일치한다. 새 각주 ref-228(factsheet.schema)는 기존 ref-031(명세)·ref-051(state.schema)·ref-052(README)와 URL 이 달라 중복이 아니다., 용어집 CSS·CORA·PDDL·플릿 어댑터 항목이 f10·f16·f18·f7 과 같은 내용이다. 용어는 새로 등록하지 않고 기존 용어 페이지로 연결한다., 이전 트랙 실행 2026-09-25-06 이 제안한 ref-044~ref-056(팩트시트·IDTA 02020 등)은 게시된 참고문헌의 같은 id 와 출처가 다르다. 이번의 새 id ref-228~ref-152 와 URL 이 겹치는지는 퍼블리셔가 확인한다. |
| 용어 일관성 | 아니오 | 용어집 '능력·스킬·서비스 모델(CSS)' 항목은 이 위키의 온톨로지 초안이 CSS 의 capability 를 '기능(Capability)'으로 부른다고 적는다. 영역 페이지와 용어 후보 '스킬'은 '능력'을 쓰므로 첫 등장 때 둘의 대응을 밝혀야 한다., 용어 후보 '스킬' 정의의 '상태 기계를 가진다'는 CaSkMan(f11)의 설계이지 IDTA 02020(f9)의 일반 정의가 아니다. |
| 인용 길이·저작권 | 아니오 | f13 발췌 인용이 원문 rdfs:comment('If, however, the SurvivalRange is violated, the System is "damaged" and SystemCapability specifications may no longer hold.')와 글자 단위로 다르다('however'와 따옴표 누락). |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f15: 문장을 'IEEE 1872.2 AuR 온톨로지(표준은 상위 온톨로지 DUL·SUMO 를 씀)의 OWL 구현으로, SUMO 는 OWL 표현이 없어 제외하고 DUL 만 포함한 제3자 구현'으로 고친다 — ref-232 README 는 SUMO 를 이 구현과 매핑에서 제외했다고 밝히고, 대상 표준은 IEEE 1872 가 아니라 1872.2 다.
- f10: 'IDTA 02020 이 CSS 계열'이라는 부분은 [사실] 문장에서 빼고, CSS 참조 모델 기반은 CaSkMan(ref-231)에 대해서만 [사실]로 쓴다. IDTA 02020 과 CSS 의 관계를 쓰려면 ref-035 를 근거로 [추정]을 붙인다 — IDTA README 에서 CSS 언급을 확인하지 못했다.
- f33: '의료·물류 등에서 쓰이는'을 지우고 '이동로봇 플릿의 작업 배정 문제'로 쓴다 — 검색 결과와 브리프 발췌 어디에도 적용 분야 서술이 없다.
- f13: 페이지에서 원문을 직접 인용하려면 ref-235 원문 문구를 글자 그대로 쓰고(출처당 1회), 아니면 재서술한다 — 브리프 발췌는 'however'와 따옴표가 빠져 원문과 다르다.
- ref-237: 참고문헌 등록(reference_updates)과 각주의 발행일을 '미확인'이 아니라 2022 로 쓴다 — 검색 결과에서 2022년 MHI Colloquium·WGMHI 연보 게재를 확인했다.
- ref-240: 발행일을 2024-02 로 쓴다 — ISO 소개 정보에서 2024-02 발행 1판을 확인했다.
- ref-238: 기관(저자) 표기를 'Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.'로 쓴다 — 검색 결과의 저자 목록.
- 각주·참고문헌 원문 미열람 표기: 브리프에서 fetched false 인 모든 출처(ref-229, ref-234, ref-236~ref-152, ref-025~ref-029, ref-035, ref-038, ref-041~ref-043)의 각주 정의에는 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 에는 source_unopened: true 를 넣는다. fetched true 인 출처(ref-228, ref-230~ref-233, ref-235, ref-040, ref-105)에는 붙이지 않는다.
- f16~f22·f28 은 제목·서지 수준의 재인용이다. 본문에서 이 출처들이 무엇을 '보였다'거나 '제안한다'고 세부를 풀어 쓰지 말고, 브리프 주장 범위(존재·제목·게재 사실)로만 쓴다. f22 는 '능력 기술 포함 여부 미확인'을 함께 적는다.
- f24: 5절 현장 시나리오에 넣지 말고 6·8절에서 '제조 조립(라인리스 이동 조립 시스템) 대상 연구'임을 밝혀 방법 참고로만 쓴다 — 물류 사례가 아니다.
- f25·f26·f31(문서·URDF 에서 LLM 으로 능력 온톨로지 생성): 교차 규칙에 따라 10절에 27. AI·학습·적응과 모델 운영, 21. 온보딩·설정·현장 시운전과 양쪽으로 연결한다. f25 의 '오류가 거의 없었다'는 저자 보고임을 밝힌다.
- f5·f19(상태 보고·운용 능력)를 8. 실시간 세계 상태·데이터 일관성에 연결할 때는 현재 상태 표현으로만 쓰고 22. 시뮬레이션·예측용 디지털 트윈과 섞지 않는다.
- 용어: 4절에서 '능력(capability)'이 첫 등장할 때 용어집 CSS 항목의 표기(온톨로지 초안의 '기능(Capability)')와 같은 뜻임을 밝힌다. 용어 후보 '스킬' 정의의 '상태 기계를 가진다'는 '상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계)'로 고친다.
- oq-004 는 해결로 바꾸지 않는다 — f27·f28 은 국내 모듈 정보 모델 KS 가 있다는 부분 근거일 뿐이고, IEEE 1872 계열이나 AAS 능력 서브모델을 KS 로 부합화한 사실은 확인되지 않았다. 11절에서 oq-004 에 연결하고 f27·f28 을 부분 근거로 적는다.
- 트랙 반영 제안 3건(2026-09-25-02; 4·7·8절)은 이번 브리프의 finding(f9·f10·f13·f15~f22)으로 반영하되, 7절의 IDTA 02020 은 제3자 논문 경유 [추정]이 아니라 f9(IDTA 저장소 README, 원문 미열람 표기)를 근거로 쓴다.

## 검증 노트

판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only, raw.githubusercontent.com 만 열람 가능)에서 검증됐다. 확인 33건, 미확인 0건, 교차 확인 0건. 강등: 없음(f15·f33 은 문구 수정, f10 은 CSS 계열 부분 한정). 원문 미열람 출처: ref-025, ref-026, ref-027, ref-028, ref-029, ref-035, ref-038, ref-041, ref-042, ref-043, ref-229, ref-234, ref-236, ref-237, ref-238, ref-239, ref-240, ref-138, ref-152. 검증자는 ref-229·ref-234 README 를 raw 경로로 열어 내용이 일치함을 확인했지만, 브리프의 fetched false 기록에 따라 신뢰도를 올리지 않았다. 주의: VDA 5050 팩트시트·MassRobotics·Open-RMF·IDTA·CaSkMan·SSN 은 규격 원문마다 한 발행 주체의 근거이고, 여러 규격을 함께 대조해야 화물 취급 가능 여부가 정해진다는 판단(f29)과 능력–실행 연결 두 방식(f30)은 추론이다. f16~f22·f28 은 제목 수준 재인용이며, 물류 로봇 매뉴얼에서 능력 모델을 LLM 으로 만든 공개 사례는 확인하지 못했다. oq-004 는 해결 불인정(국내 모듈 정보 모델 KS 존재만 부분 근거). 정정 요청 없음. 검색은 리서치 19회와 검증 9회를 합쳐 28회/30이다.
