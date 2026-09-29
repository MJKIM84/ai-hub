# 1차 검증(브리프) 2026-09-29-08

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인. CSS 저장소 README(raw) 열람: Capability 'implementation-independent specification of a function in industrial production', Skill 실행 가능 구현, Service 상업적 측면, 'Every Skill needs to have a SkillInterface (e.g. an OPC UA server)', 확장 온톨로지 CaSk·CaSkMan·RoboCaSk 모두 일치. 발행일 미확인(README 에 날짜 없음). |
| f2 | 예 | 예 | 아니오 | 유지 | 확인. IDTA 공식 저장소 raw README 열람: 요구/제공 능력 비교 목적, 속성(최대 속도·공차·온도 범위)·제약(property constraints: preconditions/invariants/postconditions, transition constraints: sequence/parallel)·스킬의 세 요소, 'first version officially published by IDTA' 일치. README 에는 'IDTA 02020' 번호가 없고 번호는 IDTA 다운로드 페이지 검색 결과로 확인. 발행일 미확인. 브리프는 fetched:false·source_unopened:true 로 표시했으므로 각주 표기는 브리프 기준을 따른다. |
| f3 | 예 | 예 | 아니오 | 유지 | 두 출처 모두 확인. 그러나 CSS 온톨로지와 IDTA 02020 은 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립 출처로 보지 않는다(브리프도 같은 사유를 적음) — cross_checked 는 false. 주장 문장 자체('두 발행 주체가 각각 정의')는 사실이므로 유지, 신뢰도 medium. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2209.10900 초록: 'there is currently no consistent way of describing the functions that each robot provides', 제조업 능력 모델을 자율 로봇에 적용·확장. v2 2023-02-09 일치. 초록 페이지에 소속 표시 없음(HSU 는 저자 이력으로 알려진 것). |
| f5 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2306.07569 v3(2025-09-10) 초록: 구성요소·하위 능력 기반 능력 추론, 'which tasks it can be assigned to and which it cannot', 어포던스 관계 추론 일치. 소속 LAAS 표시 있음. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인. 탐페레대학교 연구 포털: Procedia CIRP 97, 435–440(2021), CC BY-NC-ND. 'automatizes the matchmaking between product requirements and resource capabilities', 대형 카탈로그에서 대안 자원 탐색, 외부 설계 도구 연동 사례 일치. 온톨로지·규칙 구현 세부는 초록에 없음(브리프 표시와 같음). 발행 2021 이므로 월간 재검증 대상. |
| f7 | 예 | 예 | 예 | 유지 | 확인. LAAS(ref-249)·탐페레(ref-890)·HSU(ref-038) 세 출처 모두 열어 발행 주체가 다르고 인용 관계가 아님을 확인. '근거와 함께 돌려주는 설명 기능'은 어느 초록에도 없다는 브리프 서술도 맞다. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인. Open-RMF 사용자 정의 작업 문서: action_categories: ["clean", "manual_control"], add_performable_action 의 consider, set_action_executor, 'read-only' 교통 참여자·교통 협상 불참 일치. 문·승강기는 'customizability … is limited so that users don't need to worry about … open doors, or use lifts' 로, '바꿀 수 없다'보다는 '사용자 정의 동작의 범위에 들어가지 않는다'가 원문에 가깝다(수정 지시). 발행일 미확인. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인. 입력 원문 텍스트(data/source_texts/ref-153.txt): task_capabilities(loop·delivery, 설명은 loop·delivery·clean), recharge_threshold, battery_system·mechanical_system, RobotAPI 의 battery_soc·is_command_completed 일치. 재사용 출처(2026-09-29-07 f12 와 같은 근거). |
| f10 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2306.17030(IROS 2023) 초록: pre-/hold-/post-conditions, 세계 상태·개체 추론용 지식 베이스, 확장 행동 트리, 작업·로봇 간 교체 가능성 사례 일치. 단 'OWL' 은 초록에 없으므로 페이지에서는 '지식 베이스(세계 모델)'로 쓴다(수정 지시). 실기 배치 결과 없음. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인. PMC 전문(Healthcare 2025-04-30): SPARQL 로 전제조건·작업 경로 검사, SHACL 로 안전·기관 정책(에스코트 요구, hasAuthorityToOverride) 검증, Fundació Ave Maria 물류·RB1-Base 3대 플릿 시나리오, 'has not been deployed in a clinical robotic system yet', 시나리오는 Horizon 2020 ENDORSE 프로젝트에서 파생한 시뮬레이션 일치. 배터리·문·승강기 상태 조건은 전문에 없음. |
| f12 | 예 | 예 | 예 | 유지 | 세 출처(룬드·그리스 연구진·IDTA) 모두 열어 발행 주체 독립 확인. 다만 IDTA 02020 은 전제조건·불변·사후조건을 '기술'하는 모델이고 '실행 전에 검사하는 구조'는 SkiROS2·HERON 에서만 확인되므로 문장을 나눠 쓰게 한다. 근거 발췌의 'HERON(운반 시나리오)' 을 배터리·문·승강기 상태 조건의 예로 든 부분은 전문에서 확인되지 않아 페이지에 넣지 않는다. 신뢰도 high → medium. |
| f13 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2307.00827 v2(2024-04-28) 초록: 'two incompatible approaches', 'bidirectional mapping … two unidirectional, declarative mappings' 일치. |
| f14 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2606.02167(2026-06-01, IEEE CASE 2026): 네 표준(VDI 3682, IEC 61360-1, IDTA 02011, IDTA 02016), 'transforms distributed Multi-AAS architectures into complete PDDL planning problems', 실험실 생산 시스템 레이아웃 변형 4개 비교 일치. 정량 결과는 초록에 없음. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2208.01273(2022-08-02, 5쪽 작업 중): 'standardized digital data sheet', 시스템 AAS 의 런타임 운영 데이터·'skill-level commanding', 'generated and filled as part of our model-driven development and composition workflow' 일치. 초록 페이지에 소속(Technische Hochschule Ulm) 표시 없음 — 각주 기관란은 저자만 적거나 소속을 미확인으로 둔다. |
| f16 | 예 | 예 | 아니오 | 유지 | 확인. Zenodo 5648095(2021-11-03, FAIM 2021 Athens): OPC UA 스킬을 유한 상태 기계로, I4.0 언어 메시지·상호작용 상태 기계를 능동 AAS 에 모델링, 두 컴포넌트의 동등 협력 스킬 실행 예시 일치. 상태 기계 세부는 초록 범위 밖. 발행 2021 이므로 월간 재검증 대상. |
| f17 | 예 | 예 | 예 | 유지 | 확인. Schlegel 연구진(ref-883)·Sidorenko 연구진(ref-887)·CaSkade(ref-882) 세 출처 모두 열어 발행 주체 독립 확인. '검토되지 않은 연결의 실행을 막는 관문은 명시되지 않음' 서술도 세 출처에 부합. |
| f18 | 예 | 예 | 아니오 | 유지 | 확인. ROS Index vda5050_connector 1.1.1, BSD-3, 유지관리자 Leandro Pineda, InOrbit ros_amr_interop, VDA 5050 2.0, MQTT bridge·controller(주문 검증·실행)·adapter, State/NavToNode/VDA Action 세 핸들러 플러그인 일치. 다만 근거 발췌의 'Users must create custom adapter packages …' 문장은 페이지 원문('To create your own adapter package, add this package as a dependency and define the different plugin handlers for your robot')과 다르므로 직접 인용으로 쓰지 않는다. 발행일 미확인. |
| f19 | 예 | 예 | 아니오 | 유지 | [추정] 종합 판단. 근거 네 출처(ref-037·877·886·153) 모두 확인했고 '자동 생성 사례 미확인'은 이번 검증에서도 반증 없음. 열린 질문 1건과 짝을 이룬다. |
| f20 | 예 | 예 | 예 | 유지 | 확인. Open Robotics 문서 2건(ref-880·ref-153)과 ROS Index/InOrbit 패키지(ref-886) 를 모두 열어 '설정 선언 + 로봇별 구현' 구조를 각각 확인. 발행 주체 독립. high 유지 가능. |
| f21 | 예 | 예 | 아니오 | 유지 | 확인. CGH-CHART 페이지: KONE DX Class 승강기·개방 API, Smart Urban Co-Innovation Lab·AWS·CapitaLand Investment, Galen 빌딩 시험장, RMF, 층간 이동, 청소·보안·배송·컨시어지 로봇 확대 계획 일치. 업체 수·정량 결과 없음. 발행일 미확인. 현장 유형 '기타'(오피스) 적절. |
| f22 | 예 | 예 | 아니오 | 유지 | 확인. Frontiers 전문(2022-08-23) 을 이번 검증에서 열어 서보 장치로 카드 인식·근접 센서를 작동시킨 문 통과, FreeFleet 클라이언트, 타르투대학교병원 혈액 검체 운반을 확인. 브리프는 source_unopened:true(재인용)로 표시했으므로 각주 표기는 브리프 기준. 2026-09-29-07 f13 과 같은 근거·같은 id 재사용. |
| f23 | 예 | 예 | 아니오 | 유지 | 확인하되 주의. 브리프 URL(sereArticleSearch 형식)은 첫 열람에서 다른 논문(종교문화연구 1999 논평)을 반환했고, KCI landing URL(arti_id=ART001533055)과 검색 결과에서 황선명, 대전대학교, 보안공학연구논문지 8(1) 111–126, 2011, 컴포넌트 온톨로지·환경 온톨로지·사전 정의 TASK 컴포넌트 구성이 일치함을 확인. 각주 URL 을 landing 형식으로 바꾸게 한다. '유일한 국내 연구'는 이번 조사 범위 한정 표현으로 둔다. |
| f24 | 예 | 예 | 아니오 | 유지 | 확인. arXiv 2406.07962 v2(2024-10-18) 초록을 이번 검증에서 열어 few-shot 프롬프트 생성, 구문·모순·환각·누락 검사 루프, 최종 사람 검토 확인. 브리프는 source_unopened:true(재인용)로 표시. 2026-09-29-07 f20 과 같은 근거·id. |
| f25 | 예 | 예 | 아니오 | 유지 | [추정] 종합 판단. 근거 출처 모두 확인. 설명 기능·승인 관문 미확인 서술은 f7·f17 검증과 일치. 9절 직접 범위 서술로 적절. |
| f26 | 예 | 예 | 아니오 | 유지 | [추정] '연계 대상:' 표시 있음. 스킬 내부 구현·승강기 API 를 분류 원문 19장의 로봇 자체 지능·제어와 시설·설비 제어로 둔 판단은 원문 표와 맞다. |
| f27 | 예 | 예 | 아니오 | 유지 | [추정] 연결 영역 번호·이름 모두 부록 A 와 일치. f24 를 45·47 영역에 함께 연결한 것은 교차 규칙에 맞다. |
| f28 | 예 | 예 | 아니오 | 유지 | [추정] oq-150 부분 진전. Open-RMF 문서(문·승강기는 사용자 정의 동작 밖)와 IDTA README(로봇 현장 사례 없음) 확인. oq-150 은 해결로 바꾸지 않는다. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 예 | f9(ref-153 Open-RMF 플릿 어댑터 설정) 는 2026-09-29-07 의 f12 와 같은 근거 — 같은 id 재사용됨, 4. 이기종 로봇 등록 페이지로 링크하고 이 영역에서는 능력 선언·배터리 상태 관점만 서술한다, f22(ref-869 타르투대학교병원 문 서보 장치) 는 2026-09-29-07 의 f13 과 같은 근거 — 같은 id 재사용됨, f24(ref-465 자연어 능력 온톨로지 생성) 는 2026-09-29-07 의 f20 과 같은 근거 — 같은 id 재사용됨, 참고문헌 id 충돌: 이 브리프의 ref-038·ref-037·ref-880·ref-881·ref-883 은 같은 날 실행 2026-09-29-07 이 다른 URL(IDTA 02006, RoMi-H 등재, aas-specs-api, OPC UA Robotics, OntoKGen)에 부여한 번호와 겹친다 — 퍼블리셔가 URL 기준으로 합치며 번호를 재부여해야 한다 |
| 용어 일관성 | 예 | — |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f12: 신뢰도 high → medium 으로 내리고, 본문에서 'IDTA 02020 은 전제조건·불변·사후조건을 제약으로 기술한다'와 '실행 전에 조건을 검사하는 구조는 SkiROS2(전제·유지·사후 조건)와 HERON(SPARQL 전제조건·SHACL 정책)에서 확인된다'로 문장을 나눈다 — IDTA README 는 검사 구조를 말하지 않는다.
- f12·f11: 배터리·문·승강기 같은 구체 상태를 실행 조건으로 쓴 예로 HERON 을 들지 않는다 — HERON 전문에 배터리·문·승강기 조건이 없다. 확인된 예는 Open-RMF 의 recharge_threshold·battery_soc(f9)뿐이라고 쓴다.
- f3: 본문에 '두 모델 모두 Plattform Industrie 4.0 CSS 참조 모델에서 파생되어 독립 확인이 아니다'를 병기하고 [사실] 단일 계보 근거로 서술한다 — cross_checked 는 false 로 판정했다.
- f10: 'OWL 세계 모델' 을 '세계 상태와 개체를 추론하는 지식 베이스(세계 모델)' 로 바꾼다 — 초록에 OWL 표기가 없다.
- f8: '문·승강기 사용은 사용자 정의 로직에서 바꿀 수 없다' 를 '문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다' 로 고친다 — 원문은 customizability 가 그렇게 제한된다고 적는다.
- f18: 근거 발췌의 'Users must create custom adapter packages …' 문장을 직접 인용하지 않고 '로봇 플랫폼마다 세 핸들러 플러그인을 정의한 어댑터 패키지를 만들어야 한다' 로 재서술한다 — ROS Index 원문 문장과 다르다.
- ref-888(f23): 각주 URL 을 https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055 로 바꾼다 — 브리프의 sereArticleSearch URL 은 한 번의 열람에서 다른 논문을 반환했다. reference_updates 도 같은 URL 로 낸다.
- ref-883(f15): 각주 기관란에서 'Technische Hochschule Ulm' 을 빼고 저자만 적는다 — arXiv 초록 페이지에 소속 표시가 없다.
- ref-882·ref-229·ref-880·ref-886·ref-889: 발행일 자리에 '미확인' 을 쓰고 본문 기준일은 확인일 2026-09-29 로 둔다. ref-229·ref-869·ref-465 는 브리프가 source_unopened:true 로 표시했으므로 각주 접근일 뒤 ' (원문 미열람)' 과 reference_updates[].source_unopened: true 를 유지한다.
- reference_updates: ref-038~ref-890 은 같은 날 실행 2026-09-29-07 의 다른 URL 과 번호가 겹치므로 모든 항목에 URL 을 빠짐없이 적어 퍼블리셔가 URL 기준으로 합치게 하고, changelog_entry 에 '참고문헌 번호 충돌 확인 필요' 를 남긴다.
- 5. 적용 사례: 병원 사례는 f11(HERON, Fundació Ave Maria 시나리오는 Horizon 2020 ENDORSE 프로젝트에서 파생한 시뮬레이션이며 임상 배치 아님)과 f22(타르투대학교병원 현장 시험)로 나누어 각각 현장 유형 '병원' 을 명시하고, f21 은 현장 유형 '기타'(싱가포르 Galen 오피스 빌딩) 로 쓴다. 제조 공장·물류창고 현장 사례는 확인되지 않았다고 서술하고 물류창고를 기본값으로 쓰지 않는다.
- 용어: PDDL 첫 등장 시 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)' 로 풀어 쓰고 용어집 docs/glossary/pddl.md 에 링크한다. Open-RMF 첫 등장은 용어집 '오픈 RMF (Open-RMF)' 에 링크한다. 새 용어 후보 3건(스킬 인터페이스, 전제·유지·사후 조건, 수행 가능 동작)은 용어집에 없으므로 신규 등록한다.
- 11. 열린 질문: oq-150 은 해결로 바꾸지 않고 f28 의 부분 진전만 적는다. open_questions_new 4건은 브리프 형식 그대로 등록한다.

## 검증 노트

판정: 조건부 승인. 확인 28건, 미확인 0건, 교차 확인 4건(f7·f12·f17·f20; f3 은 두 출처가 같은 CSS 참조 모델 계보라 교차 확인으로 인정하지 않음). 강등: 없음(f12 신뢰도 high → medium). 원문 미열람 출처: 브리프 기준 ref-229·ref-869·ref-465(검증 에이전트는 세 출처를 이번에 직접 열어 내용을 확인했으나 브리프 표시를 올리지 않는다). 주의: 출처 18건 모두 열어 기관·제목이 일치함을 확인했고, ref-888 은 브리프의 KCI 검색형 URL 이 한 번 다른 논문을 반환해 landing URL 로 실재를 확인했다. IDTA 02020 번호는 README 가 아니라 IDTA 다운로드 페이지 검색 결과로 확인했다. HERON(f11)은 임상 배치 없는 시뮬레이션 시나리오이며 배터리·문·승강기 조건을 다루지 않는다. 능력 모델에서 어댑터 설정·핸들러 초안을 자동 생성한 사례와 근거를 함께 돌려주는 후보 질의는 확인되지 않았다(f19·f25 추정). 현장 사례는 병원(시뮬레이션 1, 현장 시험 1)과 기타(오피스 빌딩 시험 환경)뿐이며 제조 공장·물류창고 사례는 없다. 국내 자료는 2011년 KCI 논문 1건. 참고문헌 id ref-038~ref-890 이 같은 날 실행 2026-09-29-07 의 다른 URL 과 충돌하므로 퍼블리셔가 URL 기준으로 합쳐야 한다. 발행 2년 경과 출처(ref-890 2021, ref-887 2021, ref-883 2022, ref-869 2022, ref-888 2011)는 월간 재검증 대상. oq-150 미해결(f28 부분 진전). 정정 요청 없음. 검증 예산: 검색 2회(리서치 17회 포함 19/30), 열람 18회.
