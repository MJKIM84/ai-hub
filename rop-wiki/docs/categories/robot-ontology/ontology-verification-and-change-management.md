---
title: "7. 온톨로지 검증·변경 관리"
type: area
category: "B. 로봇 온톨로지"
area_no: 7
related_areas: [4, 5, 6, 21, 45, 47, 54, 57, 63, 65]
tags: [역량 질문, SHACL, 버전 IRI, 온톨로지 진화, 피트폴 스캐너, 서브모델 템플릿 폐기]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-886, ref-459, ref-887, ref-888, ref-889, ref-890, ref-891, ref-892, ref-439, ref-893, ref-894, ref-895, ref-896, ref-897, ref-898, ref-465, ref-880, ref-228]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 7. 온톨로지 검증·변경 관리

# 7. 온톨로지 검증·변경 관리

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-29 · 마지막 실행: 2026-09-29
<!-- auto:page-status:end -->

## 1. 한 줄 정의

온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **온톨로지 검증**: 역량 질문, 원문 대조, 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)로 완전성과 정확성을 확인한다
- **온톨로지 버전·변경 관리**: 문서·펌웨어 개정에 따라 능력 정의의 버전을 관리하고, 영향받는 작업·현장을 찾아 다시 검증한다

## 2. 핵심 질문

온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]

## 3. 왜 중요한가

온톨로지를 검증하는 수단과 판을 표기하는 규칙은 여러 발행 주체에서 확인되지만, 로봇 능력 온톨로지에 대해 문서·펌웨어 개정 시 영향받는 작업·현장을 찾아 재검증하는 절차를 통째로 다룬 자료는 없어 ROP 가 판 식별·변경 표현·펌웨어 판 보고를 이어 '변경 감지 → 영향 목록 → 재검증 대기열' 절차를 스스로 설계해야 할 것으로 보인다. [추정][^ref-886][^ref-439][^ref-891][^ref-892][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 왜 중요한가](../../topics/2026/2026-09-29-area07-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 검증 쪽(역량 질문·피트폴·형상 검증)과 변경 쪽(버전 IRI·온톨로지 진화·변경 언어)으로 나뉜다. [사실][^ref-889][^ref-888][^ref-459][^ref-886][^ref-887][^ref-891]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area07-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 적용 사례는 가정(네 로봇 플랫폼 대상 역량 질문 평가)과 병원(임상 배치 없는 시뮬레이션) 두 건뿐이며, 둘 다 현장 배치 사례가 아니다. [사실][^ref-890][^ref-880] 제조 공장·물류창고·상업 시설·실외·기타 현장 유형의 온톨로지 검증·변경 관리 사례는 확인되지 않았다.

**현장 유형:** 가정

**사례:** 가정용 개인 서비스 로봇 온톨로지를 네 로봇 플랫폼에 대해 역량 질문으로 평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 서로 다른 네 로봇 플랫폼의 작업·행동·환경·능력을 한 온톨로지에 통합 표현해야 할 때, 온톨로지가 요구를 충족하는지 역량 질문으로 평가한다. [사실][^ref-890] |
| 작업 대상 | 정보 — SOMA·DOLCE 를 확장한 온톨로지 OntoBOT 의 작업·행동·환경·능력 표현. [사실][^ref-890] |
| 수행 자원 | 평가 대상 로봇은 TIAGo·HSR·UR3·Stretch 네 종이며, 검증 수단은 역량 질문과 형식적 추론이다. [사실][^ref-890] |
| 제약 | 노인과 지원이 필요한 사람을 돕는 가정 내 개인 서비스 로봇이 대상이며, 현장 배치가 아니라 온톨로지 평가다. [사실][^ref-890] |
| 완료·인계 | 온톨로지를 역량 질문으로 평가하고 네 로봇에 대해 검증했다. [사실][^ref-890] |
| 예외·성과 | 해당 없음 |

Martorana·Urgese·Tiddi·Schlobach(암스테르담 자유대학교, 2025)의 OntoBOT 은 SOMA·DOLCE 를 확장해 가정용 개인 서비스 로봇의 작업·행동·환경·능력을 통합 표현하는 온톨로지이며, 역량 질문으로 평가하고 TIAGo·HSR·UR3·Stretch 네 로봇에 대해 검증했다. [사실][^ref-890] 이 사례는 가정에 배치한 운영 사례가 아니라 네 로봇 플랫폼을 대상으로 한 온톨로지 평가이며, 가정 현장 배치 여부는 초록에서 확인되지 않았다. 이 영역의 관점에서 보면 역량 질문이 '온톨로지가 빠짐없는가'를 묻는 완료 기준 역할을 한다.

**현장 유형:** 병원

**사례:** 의료센터 물류 운반·다중 로봇 플릿 조정 시뮬레이션에서 온톨로지로 자격·정책을 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료센터의 물류 운반과 다중 로봇 플릿 조정 시뮬레이션 시나리오에서 작업이 요청된다. [사실][^ref-880] |
| 작업 대상 | 의료센터 물류 운반 대상과, 에이전트 자격·전제조건·기관 정책이라는 정보. [사실][^ref-880] |
| 수행 자원 | 시뮬레이션 안의 다중 로봇 플릿과 상위 온톨로지 HERON 의 SPARQL·SHACL 추론. [사실][^ref-880] |
| 제약 | SPARQL 질의로 작업에 대한 에이전트 자격·전제조건을 검사하고, SHACL 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증한다. [사실][^ref-880] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

Ioannidou 외(2025)의 의료 로봇 상위 온톨로지 HERON 은 임상 배치 없이 의료센터의 시뮬레이션 시나리오로 시연되었다. [사실][^ref-880] 이 페이지에서는 SHACL 형상 검증의 적용 사례로만 짧게 다루며, 온톨로지 기반 연동 자체는 [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)에 같은 출처로 실려 있다. 역할 기반 권한 정책의 내용은 [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)의 범위다.

## 6. 대표 접근법과 기술

확인된 접근법은 역량 질문 기반 완전성 확인, 자동 평가 도구, 언어 모델 결합 검증, 판 식별·호환 표기, 변경 표현·탐지·허용성 판단, 원문 근거를 붙인 검토의 여섯 갈래이며, 어느 것도 로봇 능력 온톨로지의 개정 영향·재검증 절차 전체를 다루지는 않는다. [추정][^ref-886][^ref-439][^ref-891][^ref-892][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area07-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

판 식별은 OWL 2, 인스턴스 제약 검증은 SHACL 권고안(2017-07-20), 결함 탐지는 OOPS!, 템플릿 폐기 규칙은 IDTA 저장소, 변경 기술은 KGCL, 로봇 펌웨어·소프트웨어 판 보고는 VDA 5050 팩트시트가 맡는다. [사실][^ref-886][^ref-459][^ref-888][^ref-439][^ref-891][^ref-228]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area07-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 검증 쪽 5건, 변경 쪽 5건, 국내 1건이며 로봇 능력 온톨로지를 직접 다루는 것은 OntoBOT 과 RoSO/SMGI 뿐이다. [사실][^ref-889][^ref-890][^ref-888][^ref-887][^ref-891][^ref-892][^ref-893][^ref-898][^ref-894][^ref-895][^ref-897]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 대표 연구와 자료](../../topics/2026/2026-09-29-area07-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 절의 경계 판단은 어느 출처도 ROP 의 책임 범위를 직접 말하지 않으므로 리서치 에이전트가 확인된 수단을 묶은 종합이며, 전부 추정이다. [추정][^ref-889][^ref-459][^ref-886][^ref-891]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 팩트시트의 하드웨어·소프트웨어 판 정보를 받아 온톨로지 재검증을 촉발하고, 영향받는 작업·현장의 재검증 목록을 관리한다. [추정][^ref-228] | 연계 대상: 로봇 펌웨어·소프트웨어의 릴리스 관리와 펌웨어 검증 자체는 제조사가 맡는다. [추정][^ref-228] |
| 업종별 조건 | 표준 발행 기관의 템플릿 폐기 통보를 받아 그 판에 묶인 능력 정의를 재검증 대기열에 넣는다. [추정][^ref-439] | 연계 대상: 서브모델 템플릿의 개정·폐기 일정과 유지보수는 IDTA 같은 표준 발행 기관이 맡는다. [추정][^ref-439] |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 능력 온톨로지의 역량 질문 목록과 그 SPARQL 테스트 실행 기록, SHACL 형상과 검증 보고서, 추론기 일관성 검사, 온톨로지 판 식별자와 이전 판 관계 표기, 변경 기술(변경 언어)과 영향받는 작업·현장의 재검증 목록이며, 원문 근거를 붙인 검토·확정 기록은 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md)의 검토·승인과 같은 기록을 공유해야 할 것으로 보인다. [추정][^ref-889][^ref-459][^ref-886][^ref-891] 이 경계는 제품 전략에 따라 이동할 수 있으며, 이종 제조사를 연결하는 ROP 는 펌웨어와 표준 템플릿을 만들지 않고 그 판 정보를 받아 재검증을 촉발하는 인터페이스와 실행 보장에 머무는 것이 분류 원문 19장의 취지와 맞다. 범위 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 앞뒤의 온톨로지 영역, 판 규칙을 다루는 표준·수명주기 영역, 테스트 방법을 다루는 검증 영역, 언어 모델 방법을 다루는 AI 영역과 이어진다. [추정][^ref-439][^ref-459][^ref-465][^ref-896]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area07-s10.md)에 있다.

## 11. 열린 질문

기존 질문 oq-147 은 원문 근거 추적과 사람 최종 검토 구성만 확인되어 조사 중으로 남고, 개정 감지·재검증 절차, 지원 단계 표시 체계, 국내 사례, IDTA 폐기 판 이관 기준의 새 질문 4건을 올린다. [추정][^ref-894][^ref-895][^ref-465]

자세한 내용은 주제 페이지 [7. 온톨로지 검증·변경 관리 — 열린 질문](../../topics/2026/2026-09-29-area07-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-29 · 갱신 · [7. 온톨로지 검증·변경 관리](ontology-verification-and-change-management.md) — 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건·2차 수정 4건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area07-s6.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "6. 대표 접근법과 기술" 절(2,811자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 연구와 자료](../../topics/2026/2026-09-29-area07-s8.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "8. 대표 연구와 자료" 절(1,834자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area07-s4.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "4. 핵심 개념과 용어" 절(1,478자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 열린 질문](../../topics/2026/2026-09-29-area07-s11.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "11. 열린 질문" 절(1,150자)을 옮겼다. 2차 수정: 신규 질문 4번째의 태그를 진술 문장으로 옮김 (실행 2026-09-29-09)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-886]: W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition), 2012-12-11, https://www.w3.org/TR/owl2-syntax/, 접근일 2026-09-29
[^ref-459]: W3C (RDF Data Shapes Working Group), Shapes Constraint Language (SHACL), 2017-07-20, https://www.w3.org/TR/shacl/, 접근일 2026-09-29
[^ref-887]: Zablith, F., Antoniou, G., d'Aquin, M., Flouris, G., Kondylakis, H., Motta, E., Plexousakis, D., & Sabou, M. (The Knowledge Engineering Review), Ontology evolution: a process-centric survey, 2013-08-28, https://www.cambridge.org/core/product/identifier/S0269888913000349/type/journal_article, 접근일 2026-09-29
[^ref-888]: Poveda-Villalón, M., Gómez-Pérez, A., & Suárez-Figueroa, M. C. (Universidad Politécnica de Madrid, IJSWIS 10(2)), OOPS! (OntOlogy Pitfall Scanner!): an on-line tool for ontology evaluation, 2014-04, https://oa.upm.es/35873/, 접근일 2026-09-29
[^ref-889]: Wiśniewski, D., Potoniec, J., Ławrynowicz, A., & Keet, C. M., Competency Questions and SPARQL-OWL Queries Dataset and Analysis, 2018-11-23, https://arxiv.org/abs/1811.09529, 접근일 2026-09-29
[^ref-890]: Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics, 2025-09-26, https://arxiv.org/abs/2509.22434, 접근일 2026-09-29
[^ref-891]: Hegde, H. 외 (Database, Oxford), A Change Language for Ontologies and Knowledge Graphs, 2024-09-20, https://arxiv.org/abs/2409.13906, 접근일 2026-09-29
[^ref-892]: Qiang, Z., Taylor, K., & Wang, W., OM4OV: Leveraging Ontology Matching for Ontology Versioning, 2024-09-30, https://arxiv.org/abs/2409.20302, 접근일 2026-09-29
[^ref-439]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, submodel-templates — IDTA Submodel Templates for AAS (README), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-29
[^ref-893]: Eichelberger, H., & Weber, A., Model-driven realization of IDTA submodel specifications: The good, the bad, the incompatible?, 2024-06-20, https://arxiv.org/abs/2406.14470, 접근일 2026-09-29
[^ref-894]: Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying, 2026-09-08, https://arxiv.org/abs/2609.08869, 접근일 2026-09-29
[^ref-895]: Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation, 2026-04-03, https://arxiv.org/abs/2604.03496, 접근일 2026-09-29
[^ref-896]: Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models, 2026-04-17, https://arxiv.org/abs/2604.16258, 접근일 2026-09-29
[^ref-897]: 고영만, 송민선, 이승준, 김비연, 민혜령 (한국문헌정보학회지 49(3)), 구조적 학술용어사전 “STNet”의 추론규칙 생성에 의한 의미 검색에 관한 연구, 2015, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002022617, 접근일 2026-09-29
[^ref-898]: Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance, 2026-05-05, https://arxiv.org/abs/2605.08185, 접근일 2026-09-29
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29
[^ref-880]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
