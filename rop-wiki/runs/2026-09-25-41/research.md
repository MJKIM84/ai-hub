# 리서치 브리프 2026-09-25-41

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-41 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 온톨로지 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 1 · 답한 질문 —

## 갭(비어 있거나 약한 섹션)

- 단계 1 질문 q1-09 조사 중(실행 2026-09-25-35 부분 답) — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 1건 중 오래된 순)
- q1-09 핵심 미확인: ECLASS 데이터베이스·IEC CDD 에 이동로봇 분류 클래스와 범위 능력(이동·계단·적재·도어 조작·충전) 항목이 있는지
- 완료 조건: ROP용 능력 개념 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건이 온톨로지 초안 6절 질문으로 남아 있음(미반영)
- 온톨로지 초안 6절: 기능의 의미 식별자 속성 제안 보류 상태

## 조사 질문

1. 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]
2. q1-09 ECLASS·IEC CDD 에 이동로봇의 범위 능력(이동·계단·적재·도어 조작·충전)과 그 속성을 기술하는 항목이 있는가, 있으면 능력 온톨로지의 의미 식별자로 쓸 수 있는가?
3. ECLASS 최근 판(15.0·16.0)의 로봇 관련 분류 구조(27-38-01 등)와 전문가 그룹 활동은 이동로봇·무인운반차를 다루는가? (섹션 3 q1-09 소제목 겨냥)
4. IEC CDD 는 어떤 제품 도메인을 제공하며 로봇 도메인이 있는가? (q1-09 IEC CDD 부분 겨냥)
5. AAS 능력 모델 연구는 능력의 의미 식별자를 ECLASS 분류 클래스로 가리키는 방법을 어떻게 제시하는가? (온톨로지 초안 6절 의미 식별자 질문 겨냥)
6. 국내 자료에 ECLASS 기반 물류로봇 분류·속성 사전을 다룬 것이 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ECLASS e.V. 는 Release 15.0 에서 그룹 27-38-01 '로봇(Roboter)'의 클래스를 재구성하고 산업용 로봇 구조에 속성을 추가했으며, 새로 만든 전문가 그룹 'Robotic'이 2024-04-30 첫 회의를 열었다고 알렸다. | ref-888 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | ECLASS 는 4단계 계층의 8자리 코드로 제품 클래스를 분류하며, 각 분류 클래스는 고유 식별자(IRDI)·우선 명칭·코드를 갖고 IRDI 의 코드 공간 01 이 분류 클래스를 뜻한다. | ref-890, ref-392 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f3 | [추정] | 이번 한·영 검색 범위에서는 ECLASS 에 무인운반차·자율이동로봇 자체를 가리키는 분류 클래스나 범위 능력(이동·계단·적재·도어 조작·충전)을 능력 단위로 가리키는 항목을 확인하지 못했고, 최근 판 공지에 드러난 로봇 관련 작업은 산업용 로봇 그룹 27-38-01 에 한정된 것으로 보인다. | ref-888, ref-890 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f4 | [사실] | IEC TC 3 의 공통 데이터 사전(CDD) 안내 페이지는 제품 온톨로지 도메인으로 IEC 61987(공정 자동화), IEC 62683(저압 개폐장치·제어장치), IEC 63213(전기·전자기량 측정 장비)과 단위 도메인 IEC 62720 을 든다. | ref-889 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f5 | [추정] | IEC CDD 안내에 든 도메인에 로봇 도메인이 없어, IEC CDD 에서 이동로봇 범위 능력을 가리키는 항목을 가져올 수 있을 가능성은 낮아 보인다(CDD 데이터베이스 자체는 조회하지 못함). | ref-889 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f6 | [사실] | Vieira da Silva 외(2023) 프리프린트는 DIN 8580·VDI 2860 공정 유형을 능력의 semanticId 로 해당 ECLASS 분류를 써서 나타낼 수 있다고 적어, 능력 단위 의미 식별자를 ECLASS 분류 클래스로 가리키는 방법을 제시한다. | ref-037 | 아니오 | low | 2023-07 | — | 원문 미열람 |
| f7 | [사실] | IDTA 02047 무인운반차 기술 데이터 1.0 README 는 이 서브모델을 IDTA 가 처음 공식 발행한 1.0 판(AAS 메타모델 3.0 호환)으로 소개하며, ECLASS 분류 클래스·IEC CDD 나 충전·계단·도어·리프트 같은 능력을 언급하지 않는다. | ref-234 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [추정] | IDTA 02020·02047 이 능력 단위 사전을 지정하지 않고 ECLASS·IEC CDD 에서도 이동로봇 범위 능력 항목이 확인되지 않았으므로, ROP 는 당분간 범위 능력의 의미 식별자를 자체 네임스페이스로 정하고 ECLASS 클래스가 생기면 대응시키는 방식을 택해야 할 것으로 보인다. | ref-243, ref-245, ref-888, ref-889, ref-037 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f9 | [사실] | ECLASS Release 16.0 은 2025-11-28 발행되었고 새 분류 클래스 137개를 포함한다. | ref-891 | 아니오 | medium | 2025-11-28 | — | 원문 미열람 |

### 근거 발췌

- **f1**: 검색 요약: Release 15.0 은 27-38-01 산업용 로봇 구조의 클래스 재구성과 속성 추가를 포함하고, 신설 전문가 그룹 'Robotic'이 2024년 4월 킥오프. 이동로봇·무인운반차 클래스 언급은 요약에 없음. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f2**: 검색 요약: every classification class has a unique identifier (IRDI), a preferred name and a coded name; 4단계 중 앞 3단계는 폴더 구조. 두 출처 모두 ECLASS e.V. 기술 명세 페이지라 독립 교차 아님. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f3**: ECLASS 콘텐츠 검색(eclass.eu)은 열 수 없어 데이터베이스를 직접 조회하지 못함. 부재 관찰은 검색 결과 기준이며 부재 확정 아님(ECLASS 16.0 콘텐츠 포함 미확인).
- **f4**: 검색 요약: IEC 61987 – Process automation, IEC 62683 – Low-voltage switchgear and controlgear, IEC 62720 – Units of Measurement, IEC 63213 – Measuring equipment. 원문 미열람. (발행일 미확인, 확인일 기준)
- **f5**: f4 의 도메인 목록에서 도출. cdd.iec.ch 트리를 열지 못해 다른 도메인에 로봇 관련 클래스가 있는지는 미확인.
- **f6**: 검색 요약(arXiv 2307.00827): 'Process types can be represented with a semanticId of a capability using a respective ECLASS classification.' 제조 공정 대상이며 이동로봇 능력 사례는 요약에 없음. 원문 미열람.
- **f7**: README 원본(github_raw 열람): 'the first version officially published by IDTA', AAS 메타모델 3.0. 발행일 표기 없음. 부재 관찰은 README 기준. (발행일 미확인, 확인일 기준)
- **f8**: f3·f5·f6·f7 과 실행 2026-09-25-35 의 IDTA 템플릿 관찰(재인용: 2026-09-25-35)을 결합한 추론. 자체 네임스페이스 방식을 권고한 출처는 없음.
- **f9**: 검색 요약: Release 16.0 published November 28, 2025, 995 new Classes 중 137 new Classification Classes. 16.0 에 이동로봇 클래스가 있는지는 미확인. 원문 미열람.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-888 | ECLASS e.V. | Neuer Content für ECLASS Release 15.0 | 미확인 | 표준 | medium | 2026-09-25 | https://eclass.eu/aktuelles/news/neuer-content-fuer-eclass-release-150 | 예 |
| ref-889 | IEC TC 3 | Common Data Dictionary – CDD – TC 3 | 미확인 | 표준 | medium | 2026-09-25 | https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/ | 예 |
| ref-890 | ECLASS e.V. | Classification Class - ECLASS Technischer Support | 미확인 | 표준 | medium | 2026-09-25 | https://eclass.eu/support/technical-specification/structure-and-elements/classification-class | 예 |
| ref-891 | ECLASS e.V. | The latest ECLASS Release | 미확인 | 표준 | medium | 2026-09-25 | https://eclass.eu/en/eclass-standard/releases | 예 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | 논문 | low | 2026-09-25 | https://arxiv.org/abs/2307.00827 | 예 |
| ref-234 | IDTA(Industrial Digital Twin Association) | IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles | 예 |
| ref-243 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020_Template_Capability_Description.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json | 예 |
| ref-245 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json | 예 |
| ref-392 | ECLASS e.V. | IRDI - ECLASS Technischer Support | 미확인 | 표준 | medium | 2026-09-25 | https://eclass.eu/support/technical-specification/structure-and-elements/irdi | 예 |

### 출처 요약

- **ref-888**: 원문 미열람. ECLASS Release 15.0 의 새 콘텐츠 공지로, 로봇 그룹 27-38-01 클래스 재구성·속성 추가와 전문가 그룹 'Robotic' 신설을 알린다(검색 요약 기준).
- **ref-889**: 원문 미열람. IEC 공통 데이터 사전의 도메인(IEC 61987, IEC 62683, IEC 62720, IEC 63213)과 역할을 설명하는 IEC TC 3 페이지(검색 요약 기준).
- **ref-890**: 원문 미열람. ECLASS 분류 클래스의 구조(4단계 계층, IRDI·우선 명칭·코드)를 설명하는 기술 명세 페이지(검색 요약 기준).
- **ref-891**: 원문 미열람. ECLASS 최신 판 안내 페이지로 Release 16.0(2025-11-28)의 새 클래스 수 등을 알린다(검색 요약 기준).
- **ref-037**: 원문 미열람. AAS 능력·스킬 서브모델과 온톨로지 사이 매핑을 다룬 프리프린트.
- **ref-234**: IDTA 02047 무인운반차 기술 데이터 서브모델 1.0 README. 이번 실행에서 원본을 열어 판 표기와 ECLASS·능력 언급 부재를 확인했다.
- **ref-243**: 원문 미열람. 이번 실행에서 다시 열지 않았다(실행 2026-09-25-35 원문 확인). 능력 기술 서브모델 1.0 템플릿.
- **ref-245**: 원문 미열람. 이번 실행에서 다시 열지 않았다(실행 2026-09-25-35 원문 확인). 무인운반차 기술 데이터 서브모델 템플릿.
- **ref-392**: 원문 미열람. ECLASS 식별자 IRDI 의 구조(기관 식별자 0173, 코드 공간 01 = 분류 클래스 등)를 설명하는 기술 명세 페이지.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q1-09 부분 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 — 2절 q1-09 열림 유지(백로그 조사 중), 3절 q1-09 '(부분 답)' 소제목에 ECLASS 로봇 그룹 27-38-01·전문가 그룹(f1·f9), ECLASS 분류 구조(f2), 이동로봇 클래스 미확인(f3), IEC CDD 도메인(f4·f5), 능력 semanticId 의 ECLASS 분류 참조 방법(f6), IDTA 02047 README(f7), 자체 네임스페이스 시사점(f8) 추가, 4절 불확실성(ECLASS·CDD 데이터베이스 미조회), 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md | 7 | 트랙 manual-capability-ontology 단계 1 반영 제안 (f1, f4, f9): ECLASS 로봇 그룹 27-38-01 재구성과 전문가 그룹 'Robotic', IEC CDD 도메인에 로봇 도메인이 없음 |
| update | docs/ideas/robot-capability-ontology.md | 4 | 아이디어 페이지 4절: 범위 능력의 의미 식별자 소절에 ECLASS·IEC CDD 에서 이동로봇 범위 능력 항목 미확인(f3·f5), 능력 semanticId 로 ECLASS 분류를 가리키는 방법(f6), 자체 네임스페이스 시사점(f8) 보강 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| ECLASS | ECLASS | ECLASS e.V. 가 관리하는 제품·서비스 분류·속성 사전 표준으로, 4단계 계층의 8자리 코드와 IRDI 로 분류 클래스와 속성을 식별한다. |
| IEC 공통 데이터 사전 | IEC Common Data Dictionary (IEC CDD) | IEC TC 3 이 운영하는 IEC 61360 기반 온라인 데이터 사전으로, 공정 자동화·저압 개폐장치·측정 장비 등 도메인별 제품 분류와 속성을 제공한다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 9 · 교차 확인: 0
- 예산 사용량: 검색 21회 · 신규 출처 4건
- 미확인 항목:
    - q1-09 부분 답: ECLASS 콘텐츠 데이터베이스(15.0·16.0)와 IEC CDD 트리를 열 수 없어 이동로봇 분류 클래스·범위 능력 항목의 존재 여부를 직접 확인하지 못함
    - f3·f5·f7 은 검색 결과·README 기준의 부재 관찰이며 부재 확정 아님
    - IDTA 02020 명세 PDF 는 raw 경로로 받았으나 압축 바이너리라 ECLASS 참조 규정을 읽지 못함
    - ref-888~ref-891 원문 미열람, 발행일 미확인
    - 모든 finding 교차 확인 실패
- 범위 경계 위반 의심:
    - 없음
- 한계: 답한 질문 없음: q1-09 는 ECLASS·IEC CDD 원 데이터베이스가 네트워크 정책(mirror_only)으로 열리지 않고 검색 결과에도 이동로봇 클래스 목록이 나오지 않아 핵심(항목 존재 여부)을 확정하지 못함 — 부분 답 f1~f9 만 냄. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처는 재사용 ref-234(IDTA 02047 README)뿐이며, IDTA 02020 PDF 는 바이너리라 읽지 못함. 신규 ref-888~ref-891(예약 구간 안)과 재사용 ref-037·ref-243·ref-245·ref-392 는 원문 미열람(신뢰도 상한 medium). 검색 21회/40, 신규 출처 4건/20. 한국어 검색 1회에서는 ECLASS 기반 물류로봇 분류를 다룬 국내 자료를 찾지 못함(블로그·기사만). 온톨로지 변경 없음: 능력 단위 의미 식별자를 뒷받침할 사전 항목을 확인하지 못해 초안 6절 '기능의 의미 식별자 속성' 질문을 유지함(f6·f8 은 근거 보강). 후속 질문 1건. 27. AI·학습·적응과 모델 운영, 8. 실시간 세계 상태·데이터 일관성, 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음.

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 1
- 답한 질문 id: —

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | ECLASS 에 이동로봇 범위 능력(이동·계단·적재·도어 조작·충전) 클래스·속성이 없을 때 ROP 는 자체 의미 식별자를 어떤 네임스페이스·버전 규칙으로 두고, ECLASS 변경 요청(전문가 그룹 'Robotic' 등)으로 등록을 제안하는 책임은 누가 지는가? (q1-09 에서 파생) | 6 | f8 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - q1-09 부분 답: ECLASS·IEC CDD 직접 조회 필요
    - ROP용 능력 개념 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건이 온톨로지 초안에 미반영(6절 질문)
    - 모델·표준 비교표의 PDDL·OPC UA Robotics·MassRobotics·AAS·Open-RMF 행과 후보 밖 행의 '미조사' 칸 잔존
