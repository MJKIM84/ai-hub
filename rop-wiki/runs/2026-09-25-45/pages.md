# 스토리텔러 산출 2026-09-25-45

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-09 부분 답에 실행 2026-09-25-45 보강(충전 요소 출처 충돌 병기, ECLASS 16.0 규모, ECLASS-in-AAS 지침, AAS 능력 모델→PDDL 선례, 두 층 식별자 추정), 후속 질문 q4-14, 완료 조건·이력·출처 갱신 |
| update | docs/ideas/robot-capability-ontology.md | draft | 4절: '충전 속성 템플릿에 없음' [추정] 뒤에 명세 PDF 검색 요약과의 출처 충돌 병기, 충전 요소·두 층 의미 식별자 보강 문단(실행 2026-09-25-45) 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-09 부분 답 보강(IDTA 02047 충전 요소 출처 충돌 병기, ECLASS 16.0 규모, ECLASS-in-AAS 지침, AAS 능력 모델→PDDL 선례, 두 층 의미 식별자 추정), 새 질문 q4-14, 온톨로지 변경 없음 | run 2026-09-25-45
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: q1-09 부분 답 보강(IDTA 02047 충전 요소 출처 충돌, ECLASS 16.0 규모, ECLASS-in-AAS 지침), 새 질문 q4-14
- 대분류 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: 5. 로봇 능력·작업 온톨로지 관련 q1-09 부분 답 보강과 IDTA 02047 충전 요소 출처 충돌 열린 질문 등록
- 세부영역 최근 업데이트: —

## 용어집 갱신

- 없음

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-437 | IDTA(Industrial Digital Twin Association) | IDTA 02047-1-0 Technical Data for AGV in Intralogistics | 표준 | medium | https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf |
| ref-438 | IDTA / ECLASS e.V. | GUIDELINE How to transport ECLASS in the Asset Administration Shell (IDTA ECLASS Semantic Transport, 1.0) | 표준 | medium | https://industrialdigitaltwin.org/wp-content/uploads/2024/10/2024-10_IDTA_ECLASS_Semantic_Transport_ECLASS_in_AAS_1.0.pdf |
| ref-439 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 논문 | medium | https://arxiv.org/abs/2606.02167 |
| ref-245 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json |
| ref-243 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020_Template_Capability_Description.json | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json |
| ref-185 | ECLASS e.V. | The latest ECLASS Release | 표준 | medium | https://eclass.eu/en/eclass-standard/releases |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 출처 충돌: IDTA 02047 1.0 에 충전 관련 요소(ChargingTimeAsSpecified, ChargingDeviceRequirements, BatteryInformation)가 있는가? 명세 PDF 검색 요약은 있다고 전하지만, 공식 저장소 템플릿 JSON 의 잘린 열람 응답에서는 확인되지 않았다. | 5, 16 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 1 q1-09: ECLASS 콘텐츠 데이터베이스(15.0·16.0)와 IEC CDD 트리를 직접 조회해 무인운반차·자율이동로봇 분류 클래스와 범위 능력(이동·계단·적재·도어 조작·충전) 항목의 존재 여부를 확인해야 한다(질문의 핵심이 미확인이라 답함 처리 불가).
- 출처 충돌 해소: IDTA 02047 템플릿 JSON 을 잘리지 않게(파일 분할 열람 또는 inbox/sources 원문 투입) 끝까지 읽어 ChargingTimeAsSpecified·ChargingDeviceRequirements·BatteryInformation 요소 존재 여부와 식별자를 확인해야 한다. 명세 PDF 텍스트(inbox)도 필요하다.
- 충전 시간 속성의 ECLASS IRDI(검색 요약상 제시된 값)는 검증 검색에서 확인되지 않아 본문에 쓰지 않았다. 템플릿 원문이나 ECLASS 데이터베이스로 확인해야 한다.
- ECLASS-in-AAS 지침(ref-438)의 semanticId 가 로컬 개념 기술·IEC CDD 를 가리킬 수 있다는 서술을 원문으로 확인해야 한다(현재 검색 요약 기준).
- 세부영역 반영 제안(5. 로봇 능력·작업 온톨로지 7절, 16. 공용 자원·충전·에너지 최적화 7절)은 다음 해당 영역 실행에서 반영한다.

## 이행한 수정 지시

- f1 강등 — 단계 1 페이지 q1-09 '실행 2026-09-25-45 보강'과 아이디어 페이지 4절에서 충전 요소 문장을 [추정]으로 쓰고 문장 끝에 'IDTA 명세 PDF 검색 요약 기준, 원문 미열람'을 밝혔으며, ECLASS IRDI 값은 본문에 쓰지 않고 'IRDI 미확인'으로 두었다.
- f7 전제 수정 — 두 층 의미 식별자 문장의 전제를 '실행 2026-09-25-35 에서 원문 확인한 IDTA 02047 의 속성 단위 ECLASS IRDI 사용(최대 적재 질량 등)'으로 바꾸고 [추정]을 유지했으며, 충전 시간 속성의 IRDI 는 미확인이라고 밝혔다(각주 ref-245·ref-243·ref-438).
- f3 병기 — 단계 1 페이지 q1-09 부분 답 '범위 능력' 문단과 아이디어 페이지 4절(실행 2026-09-25-35 문단)의 기존 [추정] '충전·계단·도어 조작 속성은 템플릿에 없는 것으로 보인다' 문장을 지우지 않고 바로 뒤에 절단·명세 요약 병기 문장을 [추정]으로 더했다. 계단·도어 조작 서술은 그대로 두었다.
- 출처 충돌 열린 질문 — open_question_updates 에 '출처 충돌:' 질문을 관련 영역 5·16, 상태 열림으로 등록했다(IRDI 값은 fix 1 에 맞춰 질문 문장에서 뺐다).
- f5 — 지침의 semanticId 설명 구절을 '검색 요약 기준'으로 밝혔고, 범위와 ECLASS 14.0 예시만 확인된 사실로 썼다.
- f6 — Nabizada 외(2026)를 생산 시스템 대상의 방법 선례로만 서술하고 'IEEE CASE 2026 채택(검색 결과 기준)'을 병기했다.
- 인용 — ref-437 에서 직접 인용을 쓰지 않고 f1·f2 모두 재서술했다.
- f4 — 새 각주 없이 ref-185 를 재사용해 단계 1 페이지 실행 2026-09-25-41 보강의 Release 16.0 발행 문장에 약 50,000 클래스·23,000 속성·140,000 키워드를 [사실] 단일 출처로 더했고, 이동로봇 클래스 포함 여부는 미확인으로 유지했다.
- 각주 원문 미열람 표기 — ref-437·ref-438·ref-439 각주에 '(원문 미열람)'을 붙이고 reference_updates 에서 ref-437·438·439·185·243 을 source_unopened: true 로 두었다. ref-185 기존 각주는 이미 표기돼 있다. ref-243 의 기존 각주 줄은 실행 2026-09-25-35 원문 열람 기록에 근거한 인용들이 함께 쓰므로 페이지 줄은 바꾸지 않았다(부분 이행, 2차 검증 판단 요청). ref-245 는 본문에 '열람 응답 절단'을 밝혔다.
- q1-09 부분 답 — 답함으로 바꾸지 않고 백로그 '조사 중'(answer_link null), 단계 페이지 2절 '열림' 유지, 3절 '(부분 답)' 소제목 아래 '실행 2026-09-25-45 보강' 소절로만 더하고 명시 앵커 id 는 붙이지 않았다.
- 세부영역 반영 제안 — 세부영역 페이지를 고치지 않고 area_reflection_proposals 와 트랙 로그 '세부영역 반영 제안'으로만 남겼으며, 충전 요소 관련 제안 문장은 [추정]으로 썼다.
- 새 질문 — IDTA 02047 충전 요소와 VDA 5050 3.0.0 batteryCharging 대응 질문을 q4-14(단계 4, origin f1, 상태 열림)로 backlog_updates 에 등록하고 단계 페이지 5절 표에 더했다.
- 단계 페이지 6절·상태 줄 — 두 완료 조건 모두 '미충족'·'미승인', '다음 단계로 전환: 아니오(모델·표준 비교표 미조사 칸 잔존, 요구 목록 일부 미반영, 막힌 질문 q1-09)'로 쓰고 상태 줄의 답한 질문 8건은 바꾸지 않았다. 온톨로지 초안은 pages 에 넣지 않고 v0.3 을 유지했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: 없음(q1-09 부분 답 보강 — ECLASS·IEC CDD 데이터베이스가 네트워크 정책으로 열리지 않아 핵심 미확인; 근거 f1·f2·f3·f4·f5·f6·f7) / 새 질문: q4-14(단계 4. 온톨로지를 실행에 연결하는 방법 조사, 근거 f1) / 온톨로지 변경: 없음(v0.3 유지 — 능력 단위 의미 식별자 근거 없음, 충전 속성은 출처 충돌) / 완료 조건 평가: 미충족(부족: 모델·표준 비교표 PDDL·OPC UA Robotics·MassRobotics·AAS·Open-RMF 행과 후보 밖 행의 미조사 칸, 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건 미반영, 막힌 질문 q1-09) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지(7. 관련 표준·프레임워크·오픈소스), 16. 공용 자원·충전·에너지 최적화(7. 관련 표준·프레임워크·오픈소스) 2건 / 출처 충돌: IDTA 02047 충전 요소(명세 PDF 검색 요약 대 잘린 템플릿 JSON 열람) 열린 질문 등록 / 다음 실행 제안: q1-09(ECLASS·IEC CDD 직접 조회 또는 inbox 원문 투입, 템플릿 JSON 전체 열람) — 원문 확보 전에는 비교표 미조사 칸 채우기 질문을 우선 검토
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 1, 답함 8, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-09 | 조사 중 | — | — | — | — |
| q4-14 | 열림 | — | IDTA 02047 의 충전 관련 요소(충전 시간, 충전 장치 요구, 배터리 정보)를 VDA 5050 3.0.0 팩트시트의 batteryCharging(임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간)과 대응시켜 범위 능력 '충전'의 판 무관 속성으로 정규화할 수 있는가? (q1-09 에서 파생) | 4 | f1 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 7. 관련 표준·프레임워크·오픈소스 | IDTA 02047 명세가 AGV 를 인트라로지스틱스 무인 차량·로봇의 총칭으로 쓴다는 점([사실], ref-437 검색 요약 기준), 충전 시간·충전 장치 요구·배터리 정보 요소([추정], 템플릿 열람과 출처 충돌), IDTA·ECLASS 의 ECLASS-in-AAS 지침 1.0(2024-10, ref-438)을 반영 제안(실행 2026-09-25-45). |
| 16 | 7. 관련 표준·프레임워크·오픈소스 | IDTA 02047 의 충전 시간·충전 장치 요구·배터리 정보 요소가 충전기 배분·충전 시점 계획의 입력 후보가 될 수 있다는 [추정](명세 PDF 검색 요약 기준, 출처 충돌 열린 질문 참조, ref-437)을 반영 제안(실행 2026-09-25-45). |
