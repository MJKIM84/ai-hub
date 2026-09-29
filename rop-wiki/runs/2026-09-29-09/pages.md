# 스토리텔러 산출 2026-09-29-09

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/robot-ontology/ontology-verification-and-change-management.md | draft | 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건·2차 수정 4건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 |
| create | docs/topics/2026/2026-09-29-area07-s6.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "6. 대표 접근법과 기술" 절(2,811자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area07-s8.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "8. 대표 연구와 자료" 절(1,834자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area07-s4.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "4. 핵심 개념과 용어" 절(1,478자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area07-s11.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "11. 열린 질문" 절(1,150자)을 옮겼다. 2차 수정: 신규 질문 4번째의 태그를 진술 문장으로 옮김 |
| create | docs/topics/2026/2026-09-29-area07-s7.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,053자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area07-s3.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "3. 왜 중요한가" 절(909자)을 옮겼다. 2차 수정: 두 번째 단락 첫머리의 번호 목록 오독 제거 |
| create | docs/topics/2026/2026-09-29-area07-s10.md | draft | 자동 분리: 7. 온톨로지 검증·변경 관리 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(743자)을 옮겼다. 2차 수정: 6·21·54·57 연결 항목의 [사실]을 [추정]으로 되돌림 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 7. 온톨로지 검증·변경 관리 | 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건·2차 수정 4건 이행), version 2; 참고문헌 ref-886~ref-890 이 같은 날 실행 2026-09-29-08 의 다른 URL 과 번호가 겹쳐 퍼블리셔가 URL 기준으로 번호를 재배정해야 함 | run 2026-09-29-09
- 홈 최근 업데이트: 2026-09-29 — 7. 온톨로지 검증·변경 관리: 역량 질문·SHACL·피트폴 스캐너 기반 검증과 OWL 2 버전 IRI·IDTA 템플릿 폐기 규칙 등 판 관리 관행을 정리하고, 로봇 능력 온톨로지의 개정 영향·재검증 절차는 미확인으로 남겼다(가정·병원 사례 2건, 신뢰도 medium)
- 대분류 최근 업데이트: 2026-09-29 — 7. 온톨로지 검증·변경 관리: 섹션 3~11 신규 작성(역량 질문·자동 평가·언어 모델 결합 검증·판 식별·변경 표현·원문 근거 검토 여섯 갈래), 열린 질문 4건 신규·oq-147 조사 중, 실행 2026-09-29-09
- 세부영역 최근 업데이트: 2026-09-29 — 7. 온톨로지 검증·변경 관리: 영역 심화로 3~11절을 처음 채웠다. 검증 수단과 판 표기 규칙은 여러 발행 주체에서 확인됐으나 로봇 능력 온톨로지의 개정 감지·재검증 절차와 매뉴얼 절·줄 근거 검토 구현은 미확인이다(실행 2026-09-29-09)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 역량 질문 | Competency Question (CQ) | 온톨로지가 답할 수 있어야 하는 질문으로 요구사항을 적은 것으로, SPARQL 같은 질의로 형식화해 온톨로지가 요구를 충족하는지 검증하는 데 쓴다. | 7, 5, 54 | ref-890, ref-891 |
| new | 온톨로지 피트폴 | Ontology Pitfall | 온톨로지 모델링에서 흔히 생기는 결함 유형으로, 피트폴 스캐너(OOPS!)가 구조·기능·사용성 차원의 카탈로그와 심각·중요·경미 중요도로 자동 탐지한다. | 7 | ref-889 |
| new | 버전 IRI | Version IRI (owl:versionIRI) | OWL 2 에서 같은 온톨로지 IRI 를 공유하는 온톨로지 시리즈 가운데 특정 판을 식별하는 IRI 로, 이전 판·호환·비호환 주석과 함께 온톨로지 버전 관리에 쓴다. | 7, 57 | ref-886 |
| new | 온톨로지 진화 | Ontology Evolution | 도메인 변화나 정보 시스템 요구 변화에 대응해 온톨로지를 최신 상태로 유지하는 활동으로, 변경 감지·표현·적용·영향 관리를 포함하는 다단계 과정으로 다뤄진다. | 7 | ref-888 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-886 | W3C (OWL Working Group) | OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition) | 표준 | high | https://www.w3.org/TR/owl2-syntax/ |
| ref-459 | W3C (RDF Data Shapes Working Group) | Shapes Constraint Language (SHACL) | 표준 | high | https://www.w3.org/TR/shacl/ |
| ref-888 | Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review) | Ontology evolution: a process-centric survey | 논문 | medium | https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article |
| ref-889 | Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)) | OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation | 논문 | medium | https://oa.upm.es/35873/ |
| ref-890 | Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M. | Competency Questions and SPARQL-OWL Queries Dataset and Analysis | 논문 | medium | https://arxiv.org/abs/1811.09529 |
| ref-891 | Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam) | An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics | 논문 | medium | https://arxiv.org/abs/2509.22434 |
| ref-892 | Hegde, H. 외 (Database, Oxford) | A Change Language for Ontologies and Knowledge Graphs | 논문 | medium | https://arxiv.org/abs/2409.13906 |
| ref-893 | Qiang, Z., Taylor, K., & Wang, W. | OM4OV: Leveraging Ontology Matching for Ontology Versioning | 논문 | medium | https://arxiv.org/abs/2409.20302 |
| ref-439 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | submodel-templates — IDTA Submodel Templates for AAS (README) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates |
| ref-895 | Eichelberger, H., & Weber, A. | Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible? | 논문 | medium | https://arxiv.org/abs/2406.14470 |
| ref-896 | Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M. | OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying | 논문 | medium | https://arxiv.org/abs/2609.08869 |
| ref-897 | Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026) | Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation | 논문 | medium | https://arxiv.org/abs/2604.03496 |
| ref-898 | Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J. | Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models | 논문 | medium | https://arxiv.org/abs/2604.16258 |
| ref-899 | 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)) | 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617 |
| ref-900 | Osmani, A. | From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance | 논문 | medium | https://arxiv.org/abs/2605.08185 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 논문 | medium | https://arxiv.org/abs/2406.07962 |
| ref-880 | Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel) | HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/ |
| ref-228 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050/json_schemas/factsheet.schema (main) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| update | oq-147 | 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? | 4, 45, 7 | 조사 중 | — |
| new | — | 로봇 능력 온톨로지에 대해 펌웨어·매뉴얼 개정을 감지해 영향받는 작업·현장을 찾고 재검증 대기열에 넣는 절차를 구현한 공개 구현이나 현장 사례가 있는가? | 7, 57, 4 | 열림 | — |
| new | — | 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? | 7, 54, 36 | 열림 | — |
| new | — | 국내에서 역량 질문·추론기·SHACL 로 로봇 온톨로지를 검증하거나 버전을 관리한 연구·현장 사례가 있는가(이번 조사에서 확인된 국내 자료는 학술용어사전 온톨로지 검증 연구 1건이다)? | 7, 5 | 열림 | — |
| new | — | IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? | 7, 21, 4 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 가정 | 시작 조건 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 가정 | 작업 대상 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 가정 | 수행 자원 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 가정 | 제약 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 가정 | 완료·인계 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 병원 | 시작 조건 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 병원 | 작업 대상 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 병원 | 수행 자원 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |
| 병원 | 제약 | docs/categories/robot-ontology/ontology-verification-and-change-management.md#5-적용-사례-현장-유형-명시 | 7. 온톨로지 검증·변경 관리 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OWL 2 Web Ontology Language Structural Specification (Second Edition) | 표준 | W3C | 7, 5, 57 | ref-886 | https://www.w3.org/TR/owl2-syntax/ |
| IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 | 표준 | IDTA(Industrial Digital Twin Association) | 7, 21, 4 | ref-439 | https://github.com/admin-shell-io/submodel-templates |
| KGCL (Knowledge Graph Change Language) | 프레임워크 | Hegde, H. 외 (Database, Oxford) | 7 | ref-892 | https://arxiv.org/abs/2409.13906 |

## 추가 조사 요청

- 7절 SHACL 행에 필요한 사실: W3C 가 진행 중인 SHACL 1.2 Core 작업 초안(2026-06-22)에서 검증 보고서 구조(sh:conforms·sh:result·sh:resultSeverity)가 바뀌는지 확인 — 검증이 언급했으나 브리프에 없어 본문에 쓰지 않았다
- 5절에 필요한 사실: 제조 공장·물류창고·상업 시설·실외·기타 현장 유형의 온톨로지 검증·변경 관리 적용 사례 — 특히 Köcher·Vieira da Silva·Fay 'Constraint Checking of Skills using SHACL'(INDIN 2021)의 서지 확인(제조 공장 사례 후보)
- 6·11절에 필요한 사실: 분류 원문의 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 검증 수준·성숙도 체계를 정의한 출처
- 4절에 필요한 사실: Zablith 외(2013) 온톨로지 진화 서베이의 단계 이름(초록에서 확인되지 않아 본문에 쓰지 않았다)
- 6·11절(oq-147)에 필요한 사실: 로봇 매뉴얼·URDF 에서 추출한 능력 항목에 매뉴얼 절·줄 근거를 붙여 확정·반려하는 공개 구현 — IDTA 'How to write a SMT v1.1' 지침, Dibowski 'Full Traceability and Provenance for Knowledge Graphs'(FOIS 2024), MDPI 'Grounded Knowledge Graph Extraction via LLMs' 원문 열람
- 8절에 필요한 사실: 국내에서 로봇 온톨로지를 역량 질문·추론기·SHACL 로 검증하거나 버전을 관리한 연구·현장 사례(이번 조사는 문헌정보학 온톨로지 검증 연구 1건뿐)
- 4·8절에 필요한 사실: 역량 질문의 원 제안(Grüninger·Fox 1995)과 요구사항 기반 검증 도구 Themis 의 서지 — 원문·서지를 확인하지 못해 쓰지 않았다
- 5절 가정 사례 완료·인계 행에 필요한 사실: OntoBOT(ref-891)이 역량 질문 평가의 완료 기준(어떤 조건이 충족되면 평가를 마쳤다고 보는지)을 정의했는지 — 초록에 없어 2차 수정에서 평가 사실만 남겼다

## 이행한 수정 지시

- f21 강등 — 6절 '원문 근거를 붙인 검토'에서 TRACE-KG 의 '원문 근거에 대한 완전한 추적 가능성 유지' 문장만 [사실][^ref-897]로 두고, 사람 검토자가 원문과 대조해 검증하는 용도는 별도 문장으로 나눠 [추정][^ref-897]로 썼다
- f23 문구 정정 — 7절 VDA 5050 팩트시트 행을 'VDA 5050 프로토콜 판([Major].[Minor].[Patch])을 뜻하는 version 을 필수 속성으로 두고' 로 고쳤고, mobileRobotConfiguration 의 하드웨어·소프트웨어 판 서술은 그대로 두었다
- f4·f17 소속 표현 제거 — 3·6절에서 '포즈난 공과대학교·케이프타운 대학교 연구진', '유럽 연구진', '생물의학 온톨로지 연구진', '호주 국립대학교 계열'을 쓰지 않고 Wiśniewski 외·Martorana 외·고영만 외·Zablith 외·Hegde 외·Qiang 외 저자명으로 발행 주체를 구분했다. f2 는 '암스테르담 자유대학교'를 5절과 각주에 썼다
- SHACL 기준 판 명시 — 4·6·7절과 7절 표 아래 문장에서 'W3C 권고안 2017-07-20' 을 기준 판으로 적었고, SHACL 1.2 작업 초안은 본문에 쓰지 않고 additional_research_requests 첫 항목에 '검증 보고서 구조가 바뀌는지 확인'으로 올렸다
- f10 모델명 — 6절에서 'Kimi K2' 로 표기했다
- f18 문구 — 3·8절에서 '2024년 2월 기준 IDTA 가 발표한 84개·공개한 18개 명세' 로 썼다
- 5절 적용 사례 — 가정 사례에 현장 배치가 아니라 네 로봇 플랫폼 대상 역량 질문 평가임을, 병원 사례에 임상 배치 없는 시뮬레이션 시나리오임을 표와 서술에 명시했고, 5절 첫 단락에 제조 공장·물류창고·상업 시설·실외·기타 사례는 확인되지 않았다고 적었다. site_matrix_updates 는 가정·병원 두 현장 유형만 냈다
- f7·f9 중복 처리 — HERON 은 5절 병원 사례와 6절 '자동 평가 도구'에서 SHACL 검증 관점으로만 짧게 다루고 6. 온톨로지 기반 시스템·로봇 연동 페이지로 링크했으며, Vieira da Silva 외는 6절 '언어 모델을 결합한 검증'에서 검증 단계 관점으로만 쓰고 4. 이기종 로봇 등록 페이지로 링크했다. 각주 id 는 ref-880·ref-465 를 그대로 재사용했다
- 원문 미열람 표시 제거 — ref-439·ref-465·ref-880 의 13절 각주에 '(원문 미열람)' 을 붙이지 않았고 reference_updates 의 source_unopened 를 모두 false 로 냈다
- f19·f20 조건 — 6절과 8절에서 Osmani(2026)를 단독 저자의 이론적 프리프린트이며 실험·현장 적용이 없다고 적었고, OntoKG-EQ 를 금융(신흥 주식시장) 도메인의 선례라고 밝혔다
- 9절 — 첫 문장에 어느 출처도 ROP 책임 범위를 직접 말하지 않아 리서치 에이전트의 종합이며 전부 추정임을 밝히고 f25·f26 을 [추정]으로 두었으며, f26 은 표의 '외부와 연계하는 것' 열에 '연계 대상:' 으로 짧게 다뤘다
- 11절 — oq-147 을 해결로 바꾸지 않고 '상태: 조사 중' 에 부분 진전(원문 근거 추적·사람 최종 검토 구성은 확인, 로봇 매뉴얼 절·줄 근거 구현은 미확인)을 적었고, open_question_updates 에 update(조사 중)로 냈다. open_questions_new 4건은 질문 문장·관련 영역 번호를 그대로 new 로 등록했다
- 참고문헌 번호 충돌 — changelog_entry 에 'ref-886~ref-890 이 같은 날 실행 2026-09-29-08 의 다른 URL 과 번호가 겹쳐 퍼블리셔가 URL 기준으로 번호를 재배정해야 함' 을 남겼고, 페이지 각주는 브리프 id 를 그대로 쓰되 reference_updates 18건 모두에 URL 을 적었다
- 분량 초과 자동 분리: 7. 온톨로지 검증·변경 관리 본문 12,274자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,482자
- 2차: 10절 태그 되돌림 — docs/topics/2026/2026-09-29-area07-s10.md 3. 본문에서 6. 온톨로지 기반 시스템·로봇 연동, 21. 상호운용 표준·적합성, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리 네 항목의 [사실]을 [추정]으로 되돌렸고 각주는 그대로 두었다. 45·47 항목과 63·65 항목은 [사실]로 유지했다. 세부영역 페이지 10절의 요약 문장은 이미 [추정]이어서 바꾸지 않았다
- 2차: 5절 가정 사례 완료·인계 행 — 출처에 없는 완료 기준 해석을 빼고 '온톨로지를 역량 질문으로 평가하고 네 로봇에 대해 검증했다. [사실][^ref-891]' 로 고쳤다
- 2차: 3절 번호 목록 오독 — docs/topics/2026/2026-09-29-area07-s3.md 3. 본문 두 번째 단락 첫머리를 '핵심 질문(2절)의 앞부분' 으로 고쳐 줄 첫머리에 '숫자.' 이 오지 않게 했다
- 2차: 11절 질문 문장 태그 — docs/topics/2026/2026-09-29-area07-s11.md 3. 본문 신규 질문 4번째를 'IDTA 서브모델 템플릿의 이전 판은 새 판 발행 6개월 뒤 deprecated 로 옮겨진다. [사실][^ref-439]' 진술 문장 뒤에 질문을 잇는 형태로 고쳐 질문 문장에서 태그를 뗐다
