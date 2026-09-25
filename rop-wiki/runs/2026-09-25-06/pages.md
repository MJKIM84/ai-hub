# 스토리텔러 산출 2026-09-25-06

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-04·q1-05 답함(3절 소제목 {#q1-04}·{#q1-05}), q1-03 부분 답을 공식 저장소 원문 기준으로 교체, q1-02의 팩트시트 서술을 3.0.0 main 기준으로 바꾸고 3.0.0 오류 등급 문장 추가, 후속 질문 3건(q1-09·q2-06·q2-07), 완료 조건 미충족(막힌 질문에 q1-09 포함), 출처 ref-062~ref-074 추가, 상태 줄 숫자 갱신. 상태 줄(H1 아래)을 고쳐야 해서 patches 대신 content로 보냄 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | draft | v0.1 → v0.2: 개념 '실행 상태' 추가, '오류' 등급(3.0.0 네 값)·참조·조치 힌트 속성 추가, '기능' 속성 '의미 참조' 추가, 관계 3건 추가, 다이어그램 갱신, 6절에 제약 종류 질문 추가. H1 버전 표기를 고쳐야 해서 patches 대신 content로 보냄 |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | draft | VDA 5050(3.0.0 기준)·MassRobotics 행을 공식 저장소 원문으로 채워 '확인', IDTA 02020 칸의 ConditionContainer 를 ConstraintSet·PropertyConstraintContainer·TransitionConstraintContainer 로 교체(원문 미열람 유지), SOMA·OPC UA Robotics·Open-RMF 칸 보강, 후보 밖 2행(CaSkMan, OPC 30050 PackML) 추가, 5절 빠진 정보 요약 갱신. 상태 줄(H1 아래)을 고쳐야 해서 patches 대신 content로 보냄 |
| update | docs/tracks/manual-capability-ontology/index.md | draft | 6. 살아있는 산출물 링크: 온톨로지 초안 v0.2, 비교표 실행 2026-09-25-06 갱신, 백로그 수치, 아이디어 페이지 3·4절 반영 표시 갱신(상태 줄은 값이 바뀌지 않아 그대로) |
| update | docs/ideas/robot-capability-ontology.md | draft | 3. 선행 연구·제품 사례, 4. 필요한 데이터와 표준을 트랙 실행 2026-09-25-06의 검증된 finding으로 처음 채움(각주 7건) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-04·q1-05 답함, q1-03 부분 답을 공식 저장소 원문 기준으로 보강, 온톨로지 초안 v0.1 → v0.2, 모델·표준 비교표 3행 확인·후보 밖 2행 추가, 새 출처 ref-062~ref-074 | run 2026-09-25-06
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: q1-04(능력 기술과 실행 인터페이스의 연결)·q1-05(같은 이름 기능의 의미 차이) 답함, VDA 5050 3.0.0 팩트시트·상태 스키마 원문 확인, 능력 온톨로지 초안 v0.2
- 대분류 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: 5. 로봇 능력·작업 온톨로지 관련 VDA 5050 3.0.0·IDTA 02020·CaSkMan·AAS semanticId 조사, 능력 온톨로지 초안 v0.2(실행 상태 개념, 기능 일반화·구성 관계)
- 세부영역 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: 6. 대표 접근법과 기술(능력–스킬–상태 기계 연결, 같은 이름 기능의 의미 고정)과 7. 관련 표준·프레임워크·오픈소스(IDTA 02020, CaSkMan, AAS semanticId, VDA 5050 3.0.0 팩트시트) 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| update | VDA 5050 | VDA 5050 | 독일자동차산업협회(VDA)와 VDMA가 정한 이동로봇과 상위 관제(fleet control) 사이의 통신 인터페이스 권고안이다. | 5, 7, 9 | ref-031, ref-062, ref-063 |
| new | 팩트시트 | Factsheet (VDA 5050) | VDA 5050 에서 이동로봇이 유형 명세·물리 파라미터·지원 동작·적재 명세 등을 관제에 미리 알리는 메시지이다. | 5, 9 | ref-062 |
| new | 자산관리셸 | Asset Administration Shell (AAS) | 산업 자산의 정보를 서브모델 단위로 표준화해 디지털로 표현·교환하게 하는 인더스트리 4.0 의 디지털 트윈 구조로, 요소의 의미를 semanticId 로 외부 사전에 연결한다. | 5, 28 | ref-072 |
| new | 의미 식별자 | semanticId | 자산관리셸의 요소가 ECLASS·IEC 공통 데이터 사전 같은 외부 사전의 어떤 개념을 뜻하는지 가리키는 참조 식별자이다. | 5, 28 | ref-072 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 표준 | medium | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-036 | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 논문 | medium | https://arxiv.org/abs/2209.09632 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html |
| ref-062 | VDA / VDMA (VDA5050 GitHub) | VDA5050/json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-063 | VDA / VDMA (VDA5050 GitHub) | VDA5050/json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-064 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description/1/0 |
| ref-065 | IDTA(Industrial Digital Twin Association) | IDTA 02020_Template_Capability_Description.json | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description/1/0 |
| ref-066 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-067 | CaSkade-Automation (GitHub) | CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README) | 오픈소스 문서 | high | https://github.com/CaSkade-Automation/CaSkMan |
| ref-068 | EASE CRC (ease-crc/soma) | SOMA — owl/SOMA-ACT.owl | 오픈소스 문서 | high | https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl |
| ref-069 | OPC Foundation / VDMA | UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv | 표준 | high | https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv |
| ref-070 | Dussard, B. 외 | Ontological Component-based Description of Robot Capabilities | 논문 | medium | https://arxiv.org/abs/2306.07569 |
| ref-071 | Li, X. 외(Sensors, MDPI) | SWARMs Ontology: A Common Information Model for the Cooperation of Underwater Robots | 논문 | medium | https://doi.org/10.3390/s17030569 |
| ref-072 | IDTA(Industrial Digital Twin Association) | Specification of the Asset Administration Shell Part 1: Metamodel (IDTA-01001-3-0-1) | 표준 | medium | https://industrialdigitaltwin.org/wp-content/uploads/2024/06/IDTA-01001-3-0-1_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf |
| ref-073 | OPC Foundation / OMAC | OPC-30050 – OPC UA for PackML - Common Object Model: PackML | 표준 | medium | https://reference.opcfoundation.org/specs/OPC-30050 |
| ref-074 | Jungbluth, S., Barth, T., Nußbaum, J., Hermann, J., & Ruskowski, M. | Developing a skill-based flexible transport system using OPC UA | 논문 | medium | https://www.degruyterbrill.com/document/doi/10.1515/auto-2022-0115/html?lang=en |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 로봇 관제·물류 현장에서 제조사별 동작 이름(운반·도킹·리프트)을 공통 의미로 맞추는 사전이나 표준화 작업(ECLASS 부합, KS 등)이 있는가? | 5, 28 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02020 Capability Description (1.0) | 표준 | IDTA(Industrial Digital Twin Association) | 5, 28 | ref-064 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description/1/0 |
| Asset Administration Shell Part 1: Metamodel (IDTA-01001-3-0-1) | 표준 | IDTA(Industrial Digital Twin Association) | 5, 28 | ref-072 | https://industrialdigitaltwin.org/wp-content/uploads/2024/06/IDTA-01001-3-0-1_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf |
| CaSkMan (capability and skill ontology for manufacturing) | 오픈소스 | CaSkade-Automation | 5 | ref-067 | https://github.com/CaSkade-Automation/CaSkMan |
| OPC UA for PackML (OPC 30050) | 표준 | OPC Foundation / OMAC | 9, 28 | ref-073 | https://reference.opcfoundation.org/specs/OPC-30050 |
| SOMA (Socio-physical Model of Activities) 온톨로지 저장소 | 오픈소스 | EASE CRC | 5 | ref-068 | https://github.com/ease-crc/soma |

## 추가 조사 요청

- q1-03 잔여(단계 1 페이지 3절·비교표 4절): IEEE 1872-2015 CORA, IEEE 1872.2-2021, W3C SSN/SOSA, PDDL, KnowRob 원문(또는 공식 공개 초안·OWL 파일)으로 다섯 정보 항목(전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미)의 담김 여부 확인 — 단계 1 완료 조건(비교표 작성)과 q1-03 답함 처리에 필요
- q1-07(단계 1 페이지 3절): VDA 5050 2.0.0 태그 원문(raw.githubusercontent.com/VDA5050/VDA5050/2.0.0/…)의 팩트시트 스키마와 3.0.0 main 필드 대조(agvGeometry → mobileRobotGeometry, agvActions → mobileRobotActions 등) — 이번 실행은 2.0.0 대조를 하지 않았다
- q1-08(단계 1 페이지 3절): 이번 실행 f8(MassRobotics JSON 스키마 필드)이 적재량·지원 작업·부착 장비 기술에 해당하는지 판정하고 스키마 판 번호 확인
- q1-09(단계 1): ECLASS·IEC CDD 에 이동로봇의 운반·도킹·리프트·충전 능력을 가리키는 클래스·속성이 있는지 조사 — 단계 1 막힌 질문
- q1-06(온톨로지 초안·단계 1 완료 조건): 분류 원문 5. 로봇 능력·작업 온톨로지 정의 요소 기준의 ROP용 능력 개념 요구 목록 초안 근거 조사 — 단계 1 두 번째 완료 조건에 필요
- OPC UA for Robotics 노드셋의 메서드 목록과 형식별 소속 부(Part), OPC 40010-1 판·발행일 확인(비교표 OPC UA Robotics 행)
- CSS 계열 스킬의 PreconditionCheck·ContextCheck·FeasibilityCheck 설명의 출처 논문 확정(온톨로지 초안 6절 스킬 속성 질문)
- q4-06 조사 메모: 이번 실행 f21(두 연결 방식 매핑 표준을 검색 범위에서 찾지 못함)과 f20(Jungbluth 외 2023, VDA 5050 MQTT와 OPC UA 스킬 병행)을 q4-06 조사에서 재인용할 것
- 한국 자료 우선 규칙: 로봇 능력·스킬 기반 작업 기술이나 이종 로봇 의미 상호운용을 다룬 국내 학술·표준(KS, ECLASS 부합) 자료 — 이번 실행 한·영 검색에서 찾지 못했다
- pipeline 담당 요청: 실행 컨텍스트 next_ref_id 가 게시·미게시 참고문헌 id(최대 ref-061)와 충돌했다(검증이 ref-062~ref-074 로 재부여). next_ref_id 산출 점검 필요
- pipeline 담당 요청: 단계 페이지·온톨로지 초안·비교표는 H1 아래 상태 줄·H1 버전 표기를 바꿔야 해서 patches(H2 절 단위) 대신 content 로 보냈다. H1·머리 영역을 고칠 수 있는 패치 형식이 필요하다
- corr-001(7. 화물·재고·자산 식별과 추적 7절 VDA 5050 행)은 이번 대상 페이지 밖이라 다음 해당 영역 갱신 실행에서 처리해야 한다. 이번 실행의 ref-062(3.0.0 팩트시트)·ref-031(3.0.0 명세)이 근거로 쓰일 수 있다

## 이행한 수정 지시

- 참고문헌 id 충돌 — 브리프의 ref-044~ref-056 을 ref-062~ref-074 로 바꿔 단계 페이지·온톨로지 초안·비교표·아이디어 페이지의 각주, 프런트매터 sources, reference_updates 에 일관되게 썼고 재사용 출처 ref-022·ref-031·ref-036·ref-040 은 그대로 두었다(기존 ref-044~ref-050 은 건드리지 않음).
- q1-03 부분 답 — 단계 페이지 2절 상태 '열림', 3절 소제목 '### q1-03 … (부분 답)'(명시 id 없음), backlog_updates 에 {q1-03, 조사 중, null} 로 냈다.
- q1-04·q1-05 답함 — 3절에 '### q1-04 … {#q1-04}', '### q1-05 … {#q1-05}' 소제목을 두고 2절·backlog_updates 를 답함으로 냈으며, 결론 문장 f21·f26 은 [추정]으로 썼다.
- f20 강등 — 단계 페이지 q1-04 절의 Jungbluth 외 문장을 [추정]으로 쓰고 '스킬을 운반 단위의 자기 기술 대안으로 논의' 구절을 뺐다(저자·at 71(2) 163–175·VDA 5050 MQTT·GetTransporter·ReleaseSpecificShuttle 만 사용).
- f22 — Position 좌표 예시를 본문에 쓰지 않았고 저자는 'Li, X. 외'로 두었다.
- f15 — INVALID_ORDER_ACTION 을 등급 WARNING 으로 보고한다고 단계 페이지 q1-04 절과 비교표 VDA 5050 행에 적었다.
- 인용 — ref-031·ref-067 을 포함한 모든 출처에서 직접 인용을 쓰지 않고 재서술했다.
- 단계 페이지 q1-02 절 — agvGeometry [추정][^ref-031] 문장을 f1 의 3.0.0 main 기준 [사실][^ref-062] 문장(기준일 2026-09-25)으로 바꾸고 agvGeometry 는 '2.0.0 원문과의 필드 대조는 실시하지 않았다'로 남겼으며, ref-032 의 CRITICAL·URGENT [추정] 문장은 태그를 그대로 두고 f6 의 3.0.0 오류 등급 [사실][^ref-063] 문장을 별도로 더했다.
- 비교표 — AAS 행의 ConditionContainer 표기를 ConstraintSet·PropertyConstraintContainer·TransitionConstraintContainer 로 바꾸고 상태는 '원문 미열람' 유지, fetched=true 출처만 쓴 VDA 5050·MassRobotics·CaSkMan 행을 '확인'으로, CaSkMan(f19·f24)·OPC 30050 PackML(f18) 을 '후보 밖' 행으로 근거 finding id 와 함께 추가했다.
- 각주 원문 미열람 표기 — ref-022·ref-036·ref-064·ref-065·ref-070~ref-074 각주에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 로 두었으며, ref-031·ref-040 각주에서는 이 표기를 뺐다.
- 온톨로지 초안 v0.2 — 승인 변경 6건만 반영: 오류 등급(2.0.0 WARNING·FATAL 병기, 3.0.0 WARNING·URGENT·CRITICAL·FATAL)·errorReferences·errorHint(f6), 개념 실행 상태 '확정'(f5·f11, 보조 f18), 관계 스킬 / 실행 상태를 드러낸다 / 실행 상태(f19, 보조 f17·f18)·기능 / 일반화된다 / 기능(f10·f24)·기능 / 구성된다 / 기능(f10), 기능 속성 '의미 참조'(f14·f23·f24); H1 '(v0.2)', 프런트매터 ontology_version '0.2', track_updates.ontology_draft_version '0.2', 4절 다이어그램 갱신.
- 온톨로지 초안 — 제약 종류 수정(f9)은 반영하지 않고 6절에 미해결 질문으로 두었으며, 6절 '스킬 상태 기계 속성' 항목을 새 관계로 다뤘다고 갱신했다.
- f21 새 질문 — q4-06 과 중복이라 backlog_updates 에 넣지 않고 track_updates.log_entry 에 q4-06 조사 메모로만 남겼다.
- f4 새 질문 — 단계 2 로 고쳐 q2-06(stage 2)으로 등록하고 단계 페이지 5절의 보낼 단계를 '단계 2. 로봇 문서 유형과 정보 구조 조사'로 썼다.
- 용어집 — 'VDA 5050' 정의를 지시 문장 그대로 update 로 냈고, '팩트시트'(차량 대신 이동로봇)·'자산관리셸'·'의미 식별자'를 new 로 냈다.
- corr-001 — 대상 페이지 밖이라 처리하지 않았고 additional_research_requests 에 다음 갱신 실행으로 넘긴다고 적었다(corrections 반영 없음).
- 단계 페이지 6절·상태 줄 — 두 완료 조건 '미충족'·검증 판정 '미충족 · 미승인', 전환 '아니오(…막힌 질문 …)'로 썼고, 상태 줄을 답한 질문 4건·열린 질문 5건(q1-03·q1-06·q1-07·q1-08·q1-09)으로 맞췄다.
- docs/ideas/robot-capability-ontology.md: 각주 정의 7개를 참고문헌에서 만들어 붙임: ref-031, ref-062, ref-064, ref-066, ref-067, ref-070, ref-072
- 2차: 막힌 질문 q1-09 추가 — 단계 1 페이지 6절 표 아래 줄을 '다음 단계로 전환: 아니오(비교표의 IEEE 1872 계열·SSN·PDDL·KnowRob 행 다섯 정보 항목 미조사, ROP용 능력 개념 요구 목록 초안 미반영, 막힌 질문 q1-03·q1-06·q1-07·q1-08·q1-09)'로 고치고, track_updates.log_entry 의 '완료 조건 평가' 항목의 막힌 질문 목록도 같게 고쳤다(상태 줄 숫자는 그대로).
- 2차: 태그 뒤 괄호 — area_reflection_proposals 다섯 항목의 summary 에서 '[추정](ref-…)'·'[사실](ref-…)' 형식을 '[추정] — 근거 ref-…'·'[사실] — 근거 ref-…' 형식으로 바꿔 태그와 괄호를 떼었다(문장 내용·태그 값은 그대로).
- docs/ideas/robot-capability-ontology.md: 각주 정의 7개를 참고문헌에서 만들어 붙임: ref-031, ref-062, ref-064, ref-066, ref-067, ref-070, ref-072

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-04(f14~f21), q1-05(f22~f26); q1-03 은 부분 답 보강(f1~f13, IEEE 1872 계열·SSN·PDDL·KnowRob 원문 미열람으로 조사 중 유지) / 새 질문: q1-09(f23), q2-06(f4, 검증 지시로 단계 1 → 2), q2-07(f16); f21 제안 질문은 q4-06 과 중복이라 등록하지 않음 — q4-06 조사 메모: VDA 5050 사전 정의 동작과 IDTA 02020 능력·VDI 2860 분류를 매핑한 표준은 검색 범위에서 찾지 못함(f21), VDA 5050 MQTT 와 OPC UA 스킬 병행 사례 있음(f20, 추정) / 온톨로지 변경: v0.1 → v0.2 (2026-09-25, 근거 실행 2026-09-25-06): 개념 '오류' 수정(f6, 3.0.0 등급 WARNING·URGENT·CRITICAL·FATAL 과 참조·조치 힌트 속성), 개념 '실행 상태' 추가(f5·f11, 보조 f18), 관계 '스킬 / 실행 상태를 드러낸다 / 실행 상태' 추가(f19, 보조 f17·f18), 관계 '기능 / 일반화된다 / 기능' 추가(f10·f24), 관계 '기능 / 구성된다 / 기능' 추가(f10), 개념 '기능' 속성 '의미 참조' 추가(f14·f23·f24); 거부: 개념 '제약' 종류 수정(f9) → 6절 미해결 질문 / 완료 조건 평가: 미충족(부족: 비교표 IEEE 1872 계열·SSN·PDDL·KnowRob 행 다섯 정보 항목 미조사, ROP용 능력 개념 요구 목록 초안 미반영; 막힌 질문 q1-03·q1-06·q1-07·q1-08·q1-09) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지 2건, 9. 로봇·제조사 관제 연동 2건, 28. 표준·상호운용성·다사업자 거버넌스 1건 / 다음 실행 제안: q1-06, q1-07, q1-08(이번 f1~f3·f8 재인용 가능), q1-09, q1-03 잔여(IEEE 1872 계열·SSN·PDDL·KnowRob 원문)
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 5, 답함 4, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-03 | 조사 중 | — | — | — | — |
| q1-04 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-04 | — | — | — |
| q1-05 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-05 | — | — | — |
| q1-09 | 열림 | — | ECLASS 나 IEC 공통 데이터 사전에 이동로봇의 운반·도킹·리프트·충전 능력을 가리킬 수 있는 클래스·속성이 있는가? | 1 | f23 |
| q2-06 | 열림 | — | VDA 5050 3.0.0 팩트시트의 동작 파라미터에 허용 범위 필드가 없을 때, 제조사는 리프트 높이 같은 동작 한계를 물리 파라미터·적재 명세의 최소·최대 필드와 자유 문장 설명 가운데 어디에 적는가? | 2 | f4 |
| q2-07 | 열림 | — | 제조사 매뉴얼·통합 가이드는 VDA 5050 추가 동작이나 Open-RMF 사용자 정의 동작의 의미·파라미터·완료 조건을 어떤 형식으로 설명하는가? | 2 | f16 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 6. 대표 접근법과 기술 | 능력 기술과 실행 인터페이스의 연결은 인터페이스 안 동작 이름 기반(VDA 5050·Open-RMF)과 능력–스킬–상태 기계 기반(CSS·IDTA 02020·CaSkMan·PackML) 두 방식으로 나뉘는 것으로 보인다 [추정] — 근거 ref-062·ref-040·ref-064·ref-067·ref-036. 같은 이름 기능의 의미 차이는 고정 어휘·외부 사전 식별자(AAS semanticId)·표준 분류 하위 클래스·능력 계층·핵심 온톨로지·구성요소 기반 추론으로 다뤄진다 [추정] — 근거 ref-031·ref-072·ref-067·ref-065·ref-071·ref-070. 근거: 트랙 실행 2026-09-25-06 f21·f26. |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | IDTA 02020 능력 기술 서브모델 1.0(능력·속성·속성 제약·전이 제약·스킬, 일반화·구성 관계; ref-064·ref-065, 원문 미열람 표시), CaSkMan 정렬 온톨로지(ref-067), AAS 메타모델 semanticId 의 외부 사전 참조(ref-072), VDA 5050 3.0.0 팩트시트 적재 명세·지원 동작 목록(ref-062). 근거: f1·f2·f9·f10·f19·f23·f24. |
| 9 | 6. 대표 접근법과 기술 | VDA 5050 3.0.0은 사전 정의 동작을 규격이 정하고 옮길 수 없는 동작만 제조사가 추가 정의해 팩트시트에 같은 형식으로 선언하게 하며, 수행 불가 동작 주문은 INVALID_ORDER_ACTION(등급 WARNING)으로 보고한다 [사실] — 근거 ref-031·ref-062. Open-RMF 는 rmf_fleet actions 이름 목록 선언과 execute_action 콜백·execution.finished() 로 사용자 정의 동작을 실행한다 [사실] — 근거 ref-040. 근거: f14·f15·f16. |
| 9 | 7. 관련 표준·프레임워크·오픈소스 | VDA 5050 3.0.0 공식 저장소 JSON 스키마: 지원 동작(mobileRobotActions)의 적용 범위·파라미터·차단 유형, 동작 상태 일곱 값(RETRIABLE 포함), 오류 등급 WARNING·URGENT·CRITICAL·FATAL(ref-062·ref-063). 동작별 완료 판정(pick·startCharging, ref-031). VDA 5050 MQTT 와 OPC UA 스킬을 함께 쓴 운반 시스템 사례 [추정] — 근거 ref-074. 근거: f3·f5·f6·f7·f20. |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | MassRobotics AMR 상호운용 표준 공식 JSON 스키마(identityReport·statusReport 필드, 판 미확인; ref-066), OPC UA for Robotics 공식 노드셋 형식(TaskControlType·SafetyStateType·LoadType 등; ref-069), OPC 30050 PackML 상태 기계(ref-073, 원문 미열람), AAS semanticId 를 통한 ECLASS·IEC CDD 의미 참조(ref-072, 원문 미열람). 근거: f8·f12·f18·f23. |
