# 스토리텔러 산출 2026-09-25-41

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-09 부분 답에 실행 2026-09-25-41 보강(ECLASS·IEC CDD 조사) 추가, 결론·불확실성 추가, 후속 질문 q6-06, 완료 조건 판정 미충족·미승인, 세부영역 반영 제안, 출처 5건, 이력 행 추가 |
| update | docs/ideas/robot-capability-ontology.md | draft | 4절 범위 능력의 의미 식별자 소절에 실행 2026-09-25-41 보강(ECLASS·IEC CDD 항목 미확인, ECLASS 분류 semanticId 방법, 구축자 의견) 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-09 부분 답 보강(ECLASS·IEC CDD 조사, 이동로봇 범위 능력 항목 미확인), 후속 질문 q6-06, 온톨로지 변경 없음(v0.3) | run 2026-09-25-41
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: q1-09 부분 답 보강(ECLASS 로봇 그룹·IEC CDD 도메인 조사, 이동로봇 범위 능력 항목은 미확인), 후속 질문 1건
- 대분류 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: 5. 로봇 능력·작업 온톨로지의 범위 능력 의미 식별자 조사(ECLASS·IEC CDD), 핵심은 미확인으로 q1-09 조사 중 유지
- 세부영역 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 트랙 단계 1 실행에서 ECLASS·IEC CDD 에 이동로봇 범위 능력 항목이 확인되지 않았다는 관찰(부재 확정 아님)을 7. 관련 표준·프레임워크·오픈소스 절 반영 제안으로 냄

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | ECLASS | ECLASS | ECLASS e.V. 가 관리하는 제품·서비스 분류·속성 사전 표준으로, 4단계 계층의 8자리 코드와 IRDI 로 분류 클래스와 속성을 식별한다. | 5, 28 | ref-890, ref-392 |
| new | IEC 공통 데이터 사전 | IEC Common Data Dictionary (IEC CDD) | IEC 61360 기반 IEC 온라인 데이터 사전으로, 공정 자동화·저압 개폐장치·측정 장비 등 도메인별 제품 온톨로지와 측정 단위를 제공한다. | 28, 5 | ref-889 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-888 | ECLASS e.V. | Neuer Content für ECLASS Release 15.0 | 표준 | medium | https://eclass.eu/aktuelles/news/neuer-content-fuer-eclass-release-150 |
| ref-889 | IEC TC 3 | Common Data Dictionary – CDD – TC 3 | 표준 | medium | https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/ |
| ref-890 | ECLASS e.V. | Classification Class - ECLASS Technischer Support | 표준 | medium | https://eclass.eu/support/technical-specification/structure-and-elements/classification-class |
| ref-891 | ECLASS e.V. | The latest ECLASS Release | 표준 | medium | https://eclass.eu/en/eclass-standard/releases |
| ref-234 | IDTA(Industrial Digital Twin Association) | IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 논문 | low | https://arxiv.org/abs/2307.00827 |
| ref-392 | ECLASS e.V. | IRDI - ECLASS Technischer Support | 표준 | medium | https://eclass.eu/support/technical-specification/structure-and-elements/irdi |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) | 표준 | ECLASS e.V. | 5, 28 | ref-891 | https://eclass.eu/en/eclass-standard/releases |
| IEC 공통 데이터 사전(IEC CDD) | 표준 | IEC | 28, 5 | ref-889 | https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/ |

## 추가 조사 요청

- 단계 1 q1-09 핵심: ECLASS 콘텐츠 데이터베이스(15.0·16.0)를 직접 조회해 무인운반차·자율이동로봇 분류 클래스와 이동·계단·적재·도어 조작·충전 속성의 존재 여부를 확인해야 한다(원문 열람 가능한 환경 또는 inbox/sources 원문 필요).
- 단계 1 q1-09: IEC CDD 트리(cdd.iec.ch)에 로봇 관련 클래스가 다른 도메인 아래 있는지 확인해야 한다(안내 페이지 목록만으로는 부재를 일반화할 수 없다).
- IDTA 02020 명세 PDF 의 ECLASS 참조 규정(능력 의미 식별자를 외부 사전으로 두는 규칙)을 읽어야 한다(이번 실행은 압축 바이너리라 읽지 못함).
- ref-888(ECLASS 15.0 공지)·ref-891(릴리스 페이지)의 게시일과 15.0 발행일(2024-11-30)을 원문으로 확인해야 한다.

## 이행한 수정 지시

- f8 [추정]→[의견] 강등 — 단계 1 페이지 3절 '시사점'과 아이디어 페이지 4절 보강 문단 모두 '구축자 의견으로는'으로 시작하고 [의견] 태그를 붙였으며, 같은 문장 안에 ECLASS·IEC CDD 항목 부재가 검색 결과·안내 페이지 기준 관찰이라 부재 확정이 아니라는 한정을 두었다.
- f1 기준일 — 단계 1 페이지 3절 문장에 'Release 15.0 발행 2024-11-30(검색 결과 기준), 확인일 2026-09-25'를 적었다.
- f5 한정 — 단계 1 페이지 3절·4절과 아이디어 페이지 문장에 'IEC TC 3 안내 페이지에 든 도메인 기준이며 CDD 데이터베이스는 조회하지 못했다'를 병기했다.
- f6 한정 — 두 페이지 모두 이 방법이 DIN 8580·VDI 2860 제조 공정 유형 대상이며 이동로봇 범위 능력 사례가 아님을 같은 문장에 적었다.
- ref-234 표시 — 단계 1 페이지 각주 정의에 ' (원문 미열람)'을 붙이지 않았고 reference_updates 의 ref-234 를 source_unopened: false 로 두었다.
- ref-888·889·890·891·037·392 — 새로 둔 각주 정의에 ' (원문 미열람)'을 붙였고 reference_updates 에서 source_unopened: true 로 두었다. ref-243·ref-245 는 이번 실행 문장의 각주로 쓰지 않았다.
- ref-888·ref-891 발행일 — 각주 발행일 자리를 '미확인'으로 두고 JSON published 는 null 로 두었으며, 15.0 발행일 2024-11-30 은 본문 기준일로만 썼다.
- q1-09 상태 — 2절 표는 '열림'·답한 실행 id·답 위치 빈칸 그대로 두었고(패치하지 않음), 3절 소제목 '(부분 답)'을 유지하고 {#q1-09} 를 붙이지 않았으며, f1~f9 는 기존 소제목 아래 '#### 실행 2026-09-25-41 보강'으로 덧붙였다. 상단 상태 줄(열린 질문 1건·답한 질문 8건·완료 조건 미충족·마지막 실행 2026-09-25)은 바꾸지 않았다. 백로그는 q1-09 를 '조사 중', answer_link null 로 냈다.
- 6절 — 두 완료 조건의 검증 판정 칸을 '미충족 · 미승인'으로 두고 아래 줄을 '다음 단계로 전환: 아니오(요구 목록 일부 미반영, 막힌 질문 q1-09)'로 유지했으며 track_updates.stage_transition 은 넣지 않았다.
- 세부영역 반영 제안(28. 표준·상호운용성·다사업자 거버넌스 7절) — 근거를 f4·f5 로 적고 로봇 도메인 부재가 추정임을 summary 에 밝혔으며, 세부영역 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그로만 남겼다.
- 용어집 'IEC 공통 데이터 사전' — 정의에서 운영 주체 서술을 빼고 지시된 문장으로 썼으며, 'ECLASS' 는 f2 근거(ref-890·ref-392)로 등록했다.
- backlog_updates — 새 질문을 q6-06, stage 6, origin 'f8' 로 등록했다.
- 온톨로지 초안 — ontology-draft.md 를 pages 에 넣지 않고 ontology_draft_version 을 '0.3'으로 유지했으며, f6·f8 은 트랙 로그에 6절 '기능의 의미 식별자 속성' 질문의 근거 보강 후보로만 적었다.
- 2차: 용어집 'ECLASS'(slug eclass) description 에서 출처가 뒷받침하지 않는 구절 'AAS 서브모델은 속성의 의미 식별자로 ECLASS IRDI 를 쓸 수 있다'를 빼고, f2·ref-890·ref-392 범위 안의 내용(분류 클래스의 IRDI·우선 명칭·코드, 코드 공간 01 = 분류 클래스)만 남겼다. sources 는 ref-890·ref-392 그대로 두었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: 없음(q1-09 는 ECLASS 데이터베이스·IEC CDD 트리를 네트워크 정책으로 조회하지 못해 핵심인 범위 능력 항목 존재 여부가 미확인 — 부분 답 f1~f9 로 보강, 백로그 조사 중 유지) / 새 질문: q6-06(단계 6. 변경 관리·운영·거버넌스 조사, 근거 f8) / 온톨로지 변경: 없음(v0.3 유지). f6(ECLASS 분류를 능력 semanticId 로 쓰는 제조 공정 사례)·f8(자체 네임스페이스 방식, 구축자 의견)은 초안 6절 '기능의 의미 식별자 속성' 질문의 근거 보강 후보 / 완료 조건 평가: 미충족(부족: ROP용 능력 개념 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건 미반영, 모델·표준 비교표 일부 행 '미조사' 칸 잔존, 막힌 질문 q1-09) / 세부영역 반영 제안: 28. 표준·상호운용성·다사업자 거버넌스 1건(7절, f1·f9·f4·f5), 5. 로봇 능력·작업 온톨로지 1건(7절, f3·f5·f6) / 다음 실행 제안: q1-09(ECLASS·IEC CDD 원문 조회가 가능할 때 재개), 그 전에는 비교표 '미조사' 칸 보강과 요구 목록 미반영 항목(구성 버전·운용 구역·환경 조건·충전 조건) 근거 조사
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 1(q1-09 조사 중), 답함 8, 완료 조건 미충족. 답한 질문 없음(ECLASS·IEC CDD 데이터베이스 미조회로 q1-09 핵심 미확인), 후속 질문 q6-06 등록, 온톨로지 v0.3 유지

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-09 | 조사 중 | — | — | — | — |
| q6-06 | 열림 | — | ECLASS 에 이동로봇 범위 능력(이동·계단·적재·도어 조작·충전) 클래스·속성이 없을 때 ROP 는 자체 의미 식별자를 어떤 네임스페이스·버전 규칙으로 두고, ECLASS 변경 요청(전문가 그룹 'Robotic' 등)으로 등록을 제안하는 책임은 누가 지는가? (q1-09 에서 파생) | 6 | f8 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 28 | 7. 관련 표준·프레임워크·오픈소스 | ECLASS Release 15.0 이 로봇 그룹 27-38-01 클래스를 재구성·속성 추가하고 전문가 그룹 'Robotic'이 2024-04-30 첫 회의를 열었으며(15.0 발행 2024-11-30, 검색 결과 기준) Release 16.0 이 2025-11-28 발행됐다는 사실(f1·f9), IEC TC 3 CDD 안내 페이지의 도메인(IEC 61987·62683·63213, 단위 62720)과 그 안에 로봇 도메인이 없다는 추정(안내 페이지 기준, 데이터베이스 미조회, f4·f5)을 반영 제안한다. |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | ECLASS·IEC CDD 에서 이동로봇 범위 능력(이동·계단·적재·도어 조작·충전)을 능력 단위로 가리키는 항목이 이번 검색 범위에서 확인되지 않았다는 추정(부재 확정 아님, f3·f5)과, 제조 공정 유형을 능력 semanticId 로 ECLASS 분류를 써서 나타내는 제3자 논문 사례(f6)를 반영 제안한다. |
