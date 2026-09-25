# 스토리텔러 산출 2026-09-25-35

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-08 답함(3절 {#q1-08} 신설), q1-09 부분 답 소제목 추가, 4·5·6·7·8·9절 갱신, 상태 줄 열린 질문 1건·답한 질문 8건, 후속 질문 2건(q4-13·q2-06) |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | draft | MassRobotics 행에 화물 최대값 형식·보고 전용 구조·지원 작업·부착 장비 부재 보강, IDTA 02047 행에 특수 능력·ECLASS 식별자 사용 범위 메모, 빠진 정보 요약·출처·이력 갱신 |
| update | docs/ideas/robot-capability-ontology.md | draft | 4절에 범위 능력의 의미 식별자 미확인·특수 능력 자유 텍스트(IDTA 02047)와 MassRobotics 화물 최대 중량·충전기 유형 보강, ref-245 각주의 원문 미열람 표기 제거 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-08 답함, q1-09 부분 답, 후속 질문 2건(q4-13·q2-06), 비교표 MassRobotics·IDTA 02047 행 보강, 온톨로지 변경 없음(v0.3 유지) | run 2026-09-25-35
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: q1-08(MassRobotics 식별·상태 보고의 능력 필드) 답함, q1-09(ECLASS·IEC CDD 의 범위 능력 항목) 부분 답, 후속 질문 2건
- 대분류 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지(트랙 매뉴얼 기반 로봇 기능 온톨로지 단계 1): MassRobotics 식별 보고의 적재 필드 확인과 지원 작업·부착 장비 필드 부재 관찰, IDTA 템플릿의 ECLASS 식별자 사용 범위 확인
- 세부영역 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 트랙 단계 1 실행에서 MassRobotics 식별 보고의 능력 필드 범위와 IDTA 02020·02047 의 의미 식별자 사용 범위를 확인해 7절 반영을 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 국제 등록 데이터 식별자 | International Registration Data Identifier (IRDI) | ECLASS·IEC CDD 같은 데이터 사전이 속성·분류 클래스를 기관 식별자와 코드 공간·항목 코드·버전으로 고유하게 가리키는 식별자 형식이다(예: 최대 적재 질량 속성의 ECLASS IRDI 0173-1#02-ABJ258#001). | 5, 28 | ref-709, ref-245 |
| update | 의미 식별자 | Semantic ID (semanticId) | AAS 요소의 의미를 외부 사전(ECLASS·IEC CDD 등)의 개념 기술이나 IDTA 자체 식별자로 가리키는 식별자이다. | 5, 28 | — |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-708 | MassRobotics | What Is the MassRobotics AMR Interoperability Standard? | 표준 | medium | https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/ |
| ref-709 | ECLASS e.V. | IRDI - ECLASS Technischer Support | 표준 | medium | https://eclass.eu/support/technical-specification/structure-and-elements/irdi |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-245 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 표준 | high | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json |
| ref-243 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020_Template_Capability_Description.json | 표준 | high | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json |
| ref-247 | IDTA(Industrial Digital Twin Association) | Specification of the Asset Administration Shell Part 3a: Data Specification – IEC 61360 (IDTA-01003-a-3-0-2) | 표준 | medium | https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 1 q1-09(3절·4절): ECLASS 데이터베이스(eclass.eu 검색)와 IEC CDD(cdd.iec.ch)를 직접 조회해 무인운반차·이동로봇 분류 클래스와 범위 능력(이동·계단·적재·도어 조작·충전) 속성의 존재 여부를 확인해야 한다 — 질문의 핵심이 미확인이라 답함으로 처리하지 못했다.
- 단계 1 q1-09(3절): IDTA 02047 템플릿의 '주행 방식' 요소 semanticId 를 원문 인용으로 확인해야 한다 — 검증자가 확인하지 못해 이번 본문에서 뺐다.
- 단계 1 q1-08·비교표 MassRobotics 행: MassRobotics 표준 본문 PDF 의 판 번호·메시지 의미 설명과 전제조건·파라미터 범위·완료 확인 방법에 해당하는 서술 유무 — 비교표 칸이 미조사로 남아 있다.
- 이 실행의 핵심 사실은 모두 발행 기관 한 곳의 산출물에만 기대어 교차 확인이 0건이다. MassRobotics 필드와 IDTA 식별자 사용에 대한 독립 출처(제3자 구현·해설)가 있으면 조사가 필요하다.

## 이행한 수정 지시

- q1-08 답함 처리 — 단계 페이지 2절 표를 답함·2026-09-25-35·[#q1-08](#q1-08)로 바꾸고, 3절에 '### q1-08 MassRobotics 식별·상태 보고의 능력 필드 {#q1-08}' 소제목을 두어 적재량은 화물 최대 중량·부피 필드로 있음([사실])과 지원 작업·부착 장비 필드는 없는 것으로 보임([추정])을 요지로 썼으며, backlog_updates 에 답함과 answer_link 를 냈다.
- q1-09 부분 답 처리 — 백로그 '조사 중'·answer_link null 로 내고, 단계 페이지 2절은 '열림'을 유지했으며, 3절 소제목에 '(부분 답)'을 붙이고 명시 id 를 붙이지 않았다. 남는 finding f7~f12 만 쓰고 ECLASS·IEC CDD 미조회를 이유로 적었다.
- f7 식별자 예 제한 — IDTA 자체 식별자 예로 측경사 각(MaxLateralInclinationMaxLoad)·기구학 유형(AgvKinematic)만 쓰고 특수 능력은 별도 문장으로 썼으며 '주행 방식'은 모든 페이지에서 뺐다.
- f9 위치 표현 — '0173-1#01-' 식별자 위치를 '제조사명·제조사 제품 명칭 등 일반 정보 요소와 제품 이미지의 복합 semanticId'로 적고, 코드 공간 01 의 의미 문장에 ref-709 각주를 붙였으며 각주 정의에 '(원문 미열람)'을 표기했다.
- 각주 원문 미열람 표기 — 단계 페이지·비교표에서 ref-708·ref-709·ref-247·ref-228 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다. ref-230·ref-243·ref-245 는 표기를 붙이지 않았고(단계 페이지·비교표·아이디어 페이지의 ref-245 기존 표기 제거), ref-229 는 reference_updates 에 넣지 않고 기존 각주 줄을 재사용했다.
- ref-708 등록 — 기관 'MassRobotics', 요약에 '같은 제목 기사가 Robotics 24/7 등에도 게재됨, 원문 미열람'을 적었다. f4 본문은 위치·속도·방향·상태·작업·가용 상태 공유와 관찰 용도의 보고 방식 범위로만 썼고, 운용 상태 값은 f2(ref-230) 문장으로 근거를 달았다.
- 비교표 MassRobotics·IDTA 02047 행 — MassRobotics 적재·환경 제약 칸에 화물 최대 중량 문자열·최대 부피 객체와 정규화 필요([추정])를, 종류 칸에 보고 전용 구조(원문 미열람)와 지원 작업·부착 장비 필드 부재([추정])를 더하고 오류의 의미 칸은 유지, 전제조건·파라미터 범위·완료 확인 방법 칸은 '미조사'로 두었다. IDTA 02047 행에는 특수 능력 자유 텍스트와 ECLASS 속성 IRDI 사용 범위만 메모했다.
- 단계 페이지 6절·상태 줄 — 비교표 '충족'(미조사 칸 잔존 명시), 요구 목록 '미충족', 검증 판정 '미충족(단계 전체) · 미승인'과 '미충족 · 미승인', 아래 줄 '다음 단계로 전환: 아니오(요구 목록 일부 미반영, 막힌 질문 q1-09)', 상태 줄 '열린 질문: 1건 · 답한 질문: 8건'으로 썼다.
- 세부영역 페이지 제안 — 5. 로봇 능력·작업 온톨로지, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 페이지는 pages 에 넣지 않고 area_reflection_proposals 로만 냈다.
- 새 질문 2건 등록 — backlog_updates 에 q4-13(단계 4, origin f6)과 q2-06(단계 2, origin f8)을 열림으로 내고 단계 페이지 5절 표에도 더했다.
- 용어 등록 — '국제 등록 데이터 식별자(IRDI)'를 새 용어로 내고 정의의 예시가 최대 적재 질량 속성임을 밝혔으며 sources 에 ref-709·ref-245 를 넣고, 설명에 의미 식별자 링크를 두었다. 기존 '의미 식별자' 항목에도 IRDI 링크를 더하는 update 를 냈다.
- 온톨로지 초안 — pages 에 넣지 않고 ontology_draft_version '0.3'을 유지했으며, 6절 의미 식별자 질문의 근거 보강(f11·f12)은 다음 버전 갱신 때 반영할 사항으로 트랙 로그(log_entry)에만 적었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: q1-08(근거 f1·f2·f3·f4·f5·f6) / q1-09 부분 답(f7~f12, 백로그 조사 중 — ECLASS 데이터베이스·IEC CDD 미조회) / 새 질문: q4-13(단계 4, f6), q2-06(단계 2, f8) / 온톨로지 변경: 없음(v0.3 유지). 6절 '기능의 의미 식별자 속성' 질문의 근거 보강(f11: IDTA 02020 이 능력 사전을 지정하지 않음, f12: 범위 능력 의미 식별자는 구현자가 정해야 함)은 다음 버전 갱신 때 반영할 사항 / 완료 조건 평가: 미충족(부족: ROP용 능력 개념 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건 미반영, 비교표 일부 행의 미조사 칸 잔존, 막힌 질문 q1-09) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 3건(모두 7. 관련 표준·프레임워크·오픈소스) / 다음 실행 제안: q1-09(ECLASS·IEC CDD 직접 조회)
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 1, 답함 8, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-08 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-08 | — | — | — |
| q1-09 | 조사 중 | — | — | — | — |
| q4-13 | 열림 | — | MassRobotics 식별 보고의 화물 최대 중량(문자열)·최대 부피(객체) 값을 VDA 5050 팩트시트 적재 세트의 수치 필드와 같은 단위·형식으로 정규화해 화물 요구와 비교하는 어댑터 규칙을 어떻게 둘 것인가? (q1-08 에서 파생) | 4 | f6 |
| q2-06 | 열림 | — | 제조사는 IDTA 02047 의 특수 능력(SpecialCapabilities) 같은 자유 텍스트 항목이나 매뉴얼에 계단·도어 조작·충전 같은 범위 능력을 실제로 어떻게 적는가? (q1-09 에서 파생) | 2 | f8 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 7. 관련 표준·프레임워크·오픈소스 | MassRobotics AMR 상호운용 표준 공식 JSON 스키마의 식별 보고는 적재량을 화물 최대 중량·부피 필드로 담지만(사실, ref-230) 지원 작업·부착 장비 필드는 없는 것으로 보여(추정) 팩트시트·서브모델·매뉴얼 보완이 필요하고(추정, ref-230·ref-228·ref-245), IDTA 02020 능력 기술 템플릿은 능력 단위 사전을 지정하지 않는다(사실, ref-243·ref-229). 근거: 트랙 단계 1 실행 2026-09-25-35 f1·f3·f5·f11. |
| 9 | 7. 관련 표준·프레임워크·오픈소스 | MassRobotics 식별 보고의 필수·선택 필드와 상태 보고의 운용 상태 9종·적재 여유 비율·오류 코드(사실, ref-230), 화물 최대 중량(문자열)·최대 부피(객체) 값을 수치 비교하려면 어댑터의 형식·단위 정규화가 필요함(추정, ref-230). 근거: 트랙 단계 1 실행 2026-09-25-35 f1·f2·f6. |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | IDTA 02047 템플릿은 제조사명·최대 적재 질량·실외 사용 적합 등 속성에 ECLASS 속성 IRDI 를, 측경사 각·기구학 유형 같은 무인운반차 고유 속성에 IDTA 자체 식별자를 쓰고, ECLASS 분류 클래스 코드는 일반 정보 요소·제품 이미지에만 나타난다(사실, ref-245·ref-709 원문 미열람). 범위 능력의 의미 식별자는 구현자가 정해야 할 것으로 보인다(추정, ref-247·ref-243·ref-245). 근거: 트랙 단계 1 실행 2026-09-25-35 f7·f9·f12. |
