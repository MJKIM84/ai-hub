# 스토리텔러 산출 2026-09-25-16

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-04·q1-05 답함, q1-03 부분 답을 원문 근거로 교체, q1-02 의 IDTA 02020 표기·VDA 5050 3.0.0 오류 등급 보강, 후속 질문 3건, 완료 조건 미충족, 상태 줄 갱신. 2차: 4절 출처 표기 정정, ref-318 → ref-229, 기존 참고문헌 각주 줄을 색인 문자열로 통일 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | draft | v0.1 → v0.2: 개념 오류 수정(f5), 개념 스킬 인터페이스 추가(f19·f20·f21), 관계 2건 추가(f19·f20, f31), 거부 2건은 6절 질문, H1·도입문 버전 갱신. 2차: ref-318 → ref-229, ref-231 각주 줄을 색인 문자열로 통일 |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | draft | VDA 5050·MassRobotics·OPC UA Robotics·AAS·Open-RMF 행을 원문 근거로 보강, 후보 밖 3행(IDTA 02047, SkiROS2, CaSkMan) 추가, 빠진 정보 요약 갱신, 상태 줄 갱신. 2차: ref-318 → ref-229, ref-230·ref-231 각주 줄을 색인 문자열로 통일 |
| update | docs/ideas/robot-capability-ontology.md | draft | 3절 선행 연구와 4절 필요한 표준을 단계 1 실행 2026-09-25-16 근거로 채움. 2차: 범위 능력(충전·적재)과 표준 항목의 대응을 [추정]으로 분리, ref-318 → ref-229, 기존 참고문헌 각주 줄을 색인 문자열로 통일 |
| update | docs/tracks/manual-capability-ontology/index.md | draft | 6. 살아있는 산출물 링크: 온톨로지 초안 v0.2, 비교표 보강, 백로그 수치 갱신(상태 줄은 값 변화 없음). 2차 변경 없음 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-04·q1-05 답함, q1-03 부분 답을 공식 저장소 원문 근거로 갱신, 온톨로지 초안 v0.1 → v0.2, 비교표 산업 규격 행 보강·후보 밖 3행 추가, 새 질문 3건. ref-228·ref-230·ref-231·ref-236·ref-138 은 기존 참고문헌과 같은 출처로 재사용했고, 신규 id 는 ref-319~ref-326 이다 | run 2026-09-25-16
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: 능력 기술과 실행 인터페이스의 연결(q1-04)과 같은 이름 기능의 의미 차이(q1-05)에 답하고, VDA 5050·IDTA 02020 등 공식 저장소 원문으로 비교표와 능력 온톨로지 초안(v0.2)을 갱신했다.
- 대분류 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1(중심 영역 5. 로봇 능력·작업 온톨로지): q1-04·q1-05 답함, q1-03 부분 답 갱신, 능력 온톨로지 초안 v0.2, 세부영역 반영 제안 3건(5. 로봇 능력·작업 온톨로지, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스).
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| update | 자산 관리 셸 | Asset Administration Shell (AAS) | 산업 자산의 정보를 서브모델 단위로 기술하는 표준 체계로, IDTA가 능력 기술(IDTA 02020)·무인운반차 기술 데이터(IDTA 02047) 같은 서브모델 템플릿을 공개한다. | 5, 28, 9 | ref-229, ref-319, ref-321, ref-323 |
| new | VDA 5050 팩트시트 | VDA 5050 factsheet | VDA 5050에서 이동로봇이 관제에 자신의 유형·물리 파라미터·적재 명세·지원 action을 알리는 메시지이다. | 5, 9 | ref-228, ref-031 |
| new | 의미 식별자 | Semantic ID (semanticId) | AAS 요소의 의미를 외부 사전(ECLASS·IEC CDD 등)의 개념 기술이나 IDTA 자체 식별자로 가리키는 식별자이다. | 5, 28 | ref-323, ref-321 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-025 | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 표준 | medium | https://ieeexplore.ieee.org/document/7084073/ |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-036 | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 논문 | medium | https://arxiv.org/abs/2209.09632 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 논문 | medium | https://www.nature.com/articles/s41598-025-16649-3 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 표준 | high | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-319 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020_Template_Capability_Description.json | 표준 | high | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json |
| ref-231 | CaSkade-Automation (GitHub) | CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README) | 오픈소스 문서 | high | https://github.com/CaSkade-Automation/CaSkMan |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-320 | OPC Foundation (UA-Nodeset GitHub) | UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv | 표준 | high | https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv |
| ref-321 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 표준 | high | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json |
| ref-322 | Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. | An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2351978921002249 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-323 | IDTA(Industrial Digital Twin Association) | Specification of the Asset Administration Shell Part 3a: Data Specification – IEC 61360 (IDTA-01003-a-3-0-2) | 표준 | medium | https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf |
| ref-324 | ISO | ISO 22166-202:2025 - Robotics — Modularity for service robots — Part 202: Information model for software modules | 표준 | medium | https://www.iso.org/standard/84589.html |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 |
| ref-325 | Dussard, B. 외 | Ontological Component-based Description of Robot Capabilities | 논문 | medium | https://arxiv.org/abs/2306.07569 |
| ref-326 | RVMI lab, Aalborg University (SkiROS2 GitHub) | SkiROS2 — README (skill-based robot control platform) | 오픈소스 문서 | high | https://github.com/RVMI/skiros2 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) | 28, 5 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02020 Capability Description (AAS 서브모델 1.0) | 표준 | IDTA(Industrial Digital Twin Association) | 5, 28 | ref-319 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json |
| IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) | 표준 | IDTA(Industrial Digital Twin Association) | 5, 9 | ref-321 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json |
| AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) | 표준 | IDTA(Industrial Digital Twin Association) | 28, 5 | ref-323 | https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf |
| ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 | 표준 | ISO | 28, 5 | ref-324 | https://www.iso.org/standard/84589.html |
| KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 표준 | 국가표준인증통합정보시스템(KSSN) | 28, 5 | ref-138 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 |
| CaSkMan | 오픈소스 | CaSkade-Automation (GitHub) | 5 | ref-231 | https://github.com/CaSkade-Automation/CaSkMan |
| SkiROS2 | 오픈소스 | RVMI lab, Aalborg University | 5 | ref-326 | https://github.com/RVMI/skiros2 |

## 추가 조사 요청

- 단계 1 페이지 q1-03 과 비교표 학술 온톨로지 행: IEEE 1872 계열·KnowRob·SOMA·SSN/SOSA 의 다섯 정보 항목(전제조건·파라미터 범위·적재·환경 제약·완료 확인 방법·오류의 의미)을 원문으로 대조한 근거가 필요하다(완료 조건 미충족의 주된 원인).
- q1-06: 분류 원문 5. 로봇 능력·작업 온톨로지 정의 요소를 기준으로 ROP용 능력 개념 요구 목록 초안을 만들 근거 finding 이 필요하다(두 번째 완료 조건).
- q1-07: VDA 5050 2.0.0 과 3.0.0 팩트시트 필드 차이를 판별로 대조한 근거가 필요하다(이번에는 main 스키마만 열어 변경점은 미확인).
- q1-08: 이번 실행의 MassRobotics 공식 스키마 finding(f8)을 q1-08 답으로 쓰도록 다음 트랙 실행에서 정리가 필요하다.
- IDTA 02020 요소 이름 충돌(공식 1.0 템플릿의 ConstraintSet·CapabilityRealizedBy 대 제3자 논문의 ConditionContainer·realizedBy)이 판 차이인지 확인할 근거가 필요하다.
- 아이디어 페이지 4절: 범위 능력(이동·계단·적재·도어 조작·충전)과 표준 항목(VDA 5050 action·팩트시트 필드 등)의 대응을 사실로 쓸 수 있는 근거 finding 이 필요하다(현재 충전·적재 대응은 [추정]).
- 모든 산업 규격 주장이 발행 주체 한 곳의 자료에만 기대므로, 독립 출처(구현 라이브러리·학술 비교 연구)로 교차 확인이 필요하다.
- KS B 7321-2 의 제정일·ISO 22166-202 부합화 여부와 국내 적용 사례(한국 자료 우선 규칙).
- VDA 5050 3.0.0 정확한 발행일(oq-005).

## 이행한 수정 지시

- f30 강등 — 단계 1 페이지 q1-05 와 아이디어 페이지 4절에서 [추정]으로 쓰고 '속도'를 뺀 뒤 '제조사명(0173-1#02-AAO677)·최대 적재 질량(0173-1#02-ABJ258) 같은 일부 속성에 ECLASS IRDI 를 붙이고, 속도 속성에는 IDTA 자체 식별자를 쓴다'로 고쳐 썼고, 용어집 '의미 식별자' 정의도 맞췄다.
- f31 분리 — q1-05 에서 일반화·구성·SameProperty 관계는 [사실] 문장으로, '제조사별 구체 능력을 공통 상위 능력에 연결할 수 있다'는 별도 [추정] 문장으로 썼다.
- f35 한정 — q1-05 정리 문단과 4절 결론에서 (3)을 '속성 단위의 외부 사전 식별자(AAS 의미 식별자, ECLASS·IEC CDD)'로 한정했다.
- q1-03 부분 답 — 2절 표 '열림'(답한 실행 id·답 위치 비움), backlog_updates 에 조사 중·answer_link null, 3절 소제목 '(부분 답)'을 유지한 채 내용을 f1~f15(중심 f13) 원문 근거로 교체했다.
- q1-04·q1-05 답함 — 2절 표에 답함·2026-09-25-16·#q1-04/#q1-05, 3절에 '### q1-04 … {#q1-04}'·'### q1-05 … {#q1-05}' 소제목을 두었고 q1-07·q1-08 상태는 바꾸지 않았다.
- IDTA 02020 표기 — 3절 q1-02 와 비교표 AAS 행을 공식 템플릿 이름(ConstraintSet, CapabilityRealizedBy)으로 쓰고, ref-037 표기(ConditionContainer, realizedBy)는 '제3자 논문 표기이며 1.0 템플릿에서 확인되지 않음 — 판 차이 여부 미확인'으로 함께 제시했으며 4절 남은 불확실성에도 적었다.
- q1-03 완료 확인 — '완료 확인 방법을 명시하는 항목 미확인' 판단을 f4·f6·f10·f13 근거로 고치고, 이전 판단이 검색 범위의 추정이었음을 한 줄로 밝혔다(단계 페이지 3절, 비교표 5절).
- VDA 5050 3.0.0 오류 등급 — q1-02 에 main 상태 스키마(ref-051) 근거로 'WARNING·URGENT·CRITICAL·FATAL 넷' [사실] 문장을 더했고, 4절의 '3.0.0 기능 목록 미확인'을 오류 등급·사전 정의 action 29종 확인과 나머지 확장 미대조로 줄였다.
- f19 판 표기 — q1-04 와 아이디어 페이지 3절에 '2022년 arXiv, 저널판 Automatisierungstechnik 71(2), 2023'으로 적고 ref-036 각주는 기존 줄을 재사용했다.
- f29 판 표기 — q1-05 와 아이디어 페이지 4절에 'IDTA-01003-a 3.0.2(2024-07)를 인용했고 최신판 3.1.1 이 있다'고 명시했다.
- f33 주체 — q1-05 에 'RCO 논문(Naqvi 외, 2025) 저자는 … 라고 주장한다' [의견]으로 썼다.
- f10·f11 범위 — SkiROS2 는 스킬 조건 표현 사례로만(연계 대상 명시), OPC UA Robotics 의 모션 장치·안전 정지 유형은 능력 기술 유무 판단 용도로만 서술했다(단계 페이지 3절, 비교표, 아이디어 페이지).
- 원문 미열람 표기 — ref-025·ref-036·ref-041·ref-322~ref-325 각주에 ' (원문 미열람)'을 두고 reference_updates 에 source_unopened: true 를 넣었으며, ref-031·ref-040·ref-051·ref-228~ref-321·ref-326 각주에서는 '(원문 미열람)'을 뺐다.
- 직접 인용 — ref-031 을 포함해 어느 출처도 원문을 직접 인용하지 않고 모두 재서술했다.
- 온톨로지 v0.2 — 오류 등급을 3.0.0 값으로 고치고 2.0.0 값을 판 표기와 함께 남기며 해결 힌트와 'action 상태 RETRIABLE 에서 온 값'인 재시도 가능 여부를 더했고(f5, 확정), 개념 스킬 인터페이스(속성: 프로토콜 OPC UA·REST, 상태 기계, 호출 방법; VDA 5050 action·Open-RMF 동작 제외, 확정), 관계 '스킬 / 노출된다 / 스킬 인터페이스'(f19·f20, 확정)와 '기능 / 일반화된다 / 기능'(f31, 확정)을 더했으며, 6절의 출처 미확정 항목을 해소로 고쳤다. 버전은 프런트매터·H1·ontology_draft_version 을 0.2 로 맞췄다.
- 거부 2건 — 제약의 적용 시점 구분(f6·f10)은 6절 실행 조건·제약 경계 질문에 합쳤고, 기능의 의미 식별자 속성과 AsSpecified·AsOperated 값 메모(f29·f30·f14)는 표에 넣지 않고 6절 질문으로 두었다.
- 새 질문 — 파라미터 범위 보완 질문은 q4-06 과 중복이라 backlog_updates 에 넣지 않았고(단계 페이지 5절에 사유 기재), 나머지 세 건을 q4-09(origin f26), q1-09(origin f30), q5-07(origin f35)로 등록했다.
- 열린 질문 — KS B 7321-2 질문 문장에 oq-004 와의 연결을 적었고 단계 페이지 4절에도 함께 언급했다.
- 단계 페이지 6절 — 두 완료 조건 '미충족', 검증 판정 '미충족 · 미승인', 아래 줄을 지시 문구 그대로 적었고, 상태 줄 질문 수를 2절 표와 맞췄다(열린 질문 5건·답한 질문 4건).
- 세부영역 반영 — 5. 로봇 능력·작업 온톨로지, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그 항목에만 남겼다.
- 참고문헌 id — reference_updates 에 브리프 id 를 그대로 쓰고 changelog_entry 에 'ref-228~ref-326 은 2026-09-25-15 브리프와 id 가 충돌할 수 있어 퍼블리셔 확인이 필요하다'를 남겼다.
- 2차: 단계 1 페이지 4절 출처 표기 — 남은 불확실성 마지막 줄의 중복 'ref-138'을 하나로 줄이고 'ref-133'을 'ref-236'으로 고쳤다.
- 2차: 아이디어 페이지 4절 범위 능력 대응 — 'VDA 5050 3.0.0의 사전 정의 action 에는 startCharging·stopCharging 이 있다' [사실]과 '범위 능력 충전은 이 action 에 대응하는 것으로 보인다' [추정]으로 나눴고, 적재 문장을 '팩트시트의 적재 명세로 기술되는 것으로 보인다' [추정]으로 내렸다.
- 2차: 용어집 '자산 관리 셸' — action 을 update 로 바꾸고 term_ko 를 '자산 관리 셸'로 갱신했으며 기존 표기 '자산관리셸'과 원제 '자산관리쉘'을 설명에 병기했다.
- 2차: ref-318 → ref-229 — 단계 1 페이지(3절 q1-03 전제조건·완료 확인, q1-04 연결 없음 문단, 8절, 프런트매터), 온톨로지 초안(6절, 각주, 프런트매터), 비교표(AAS 행 출처, 5절 두 곳, 7절, 프런트매터), 아이디어 페이지(4절, 각주)에서 모두 바꾸고, 각주는 참고문헌 ref-229 줄을 '(원문 미열람)' 없이 썼으며 reference_updates 에서 ref-318 을 빼고 ref-229(source_unopened: false)를 넣었다.
- 2차: 기존 참고문헌 각주 통일 — ref-138·ref-230·ref-231·ref-236 의 각주 정의(단계 1 페이지 8절, 비교표 7절, 온톨로지 초안, 아이디어 페이지)와 reference_updates 의 org·title 을 참고문헌 색인 문자열 그대로 바꿨고, ref-230·ref-231 에는 '(원문 미열람)'을 붙이지 않았다(standards_updates 의 KS·CaSkMan 기관명도 같게 맞췄다).
- 2차: changelog_entry — id 충돌 문구를 'ref-228·ref-230·ref-231·ref-236·ref-138 은 기존 참고문헌과 같은 출처로 재사용했고, 신규 id 는 ref-319~ref-326 이다'로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-04(f16~f26), q1-05(f27~f35); q1-03 은 부분 답 갱신(f1~f15, 산업 규격·서브모델·오픈소스만 원문 대조, IEEE 1872 계열·KnowRob·SOMA·SSN/SOSA 대조 없음) / 새 질문: q1-09(f30), q4-09(f26), q5-07(f35); action 파라미터 범위 보완 질문은 q4-06 과 중복이라 등록하지 않음 / 온톨로지 변경: v0.1 → v0.2 (2026-09-25, 근거 실행 2026-09-25-16): 개념 '오류' 수정(3.0.0 등급 WARNING·URGENT·CRITICAL·FATAL, 2.0.0 값 병기, 해결 힌트·재시도 가능 여부 추가, f5), 개념 '스킬 인터페이스' 추가(f19·f20·f21), 관계 '스킬 / 노출된다 / 스킬 인터페이스' 추가(f19·f20), 관계 '기능 / 일반화된다 / 기능' 추가(f31); 거부: 제약의 적용 시점 구분(f6·f10), 기능의 의미 식별자·능력 출처 값 메모(f29·f30·f14) — 6절 질문으로 둠 / 완료 조건 평가: 미충족(부족: 비교표의 IEEE 1872 계열·KnowRob·SOMA·SSN/SOSA 행 다섯 정보 항목, ROP용 능력 개념 요구 목록 초안 미반영; 막힌 질문 q1-03·q1-06·q1-07·q1-08) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지(4·6·7절), 9. 로봇·제조사 관제 연동(6·7절), 28. 표준·상호운용성·다사업자 거버넌스(7절) 6건 / 다음 실행 제안: q1-06, q1-07, q1-08(이번 f8 을 답 근거로 활용), q1-03 학술 온톨로지 대조
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 5, 답함 4, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-03 | 조사 중 | — | — | — | — |
| q1-04 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-04 | — | — | — |
| q1-05 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-05 | — | — | — |
| q1-09 | 열림 | — | ECLASS·IEC CDD 에 이동로봇의 범위 능력(이동·계단·적재·도어 조작·충전)과 그 속성을 기술하는 항목이 있는가, 있으면 능력 온톨로지의 의미 식별자로 쓸 수 있는가? | 1 | f30 |
| q4-09 | 열림 | — | CSS 참조 모델의 스킬 상태 기계(SkillType·SkillStateMachine)와 VDA 5050 action 상태(WAITING~FAILED·RETRIABLE), Open-RMF execute_action 완료 신호를 하나의 스킬 실행 상태 모델로 대응시킬 수 있는가? | 4 | f26 |
| q5-07 | 열림 | — | 서로 다른 제조사가 정의한 사용자 정의 action(예: 도킹·리프트)이 같은 동작인지를 파라미터·완료 정의·효과 비교로 판정하는 시험 절차를 어떻게 둘 것인가? | 5 | f35 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 4. 핵심 개념과 용어 | 능력·스킬·스킬 인터페이스의 구분(CSS 참조 모델, CaSkMan), IDTA 02020 속성 제약(전제·불변·사후조건)과 전이 제약, 속성 단위 의미 식별자(AAS semanticId, ECLASS·IEC CDD)를 용어로 소개한다(단계 1 실행 2026-09-25-16, f6·f19·f20·f29). |
| 5 | 6. 대표 접근법과 기술 | 능력 기술과 실행 인터페이스의 연결 3방식(같은 프로토콜 안 이름 맞물림, 능력–스킬–스킬 인터페이스 모델, 연결 없음)과 같은 이름 기능의 의미 차이 대응 4방식을 이 위키의 [추정] 분류로 소개하고, SCM 질문에 답하려면 화물 속성과 로봇 적재 명세의 대조 규칙이 필요하다는 추정을 더한다(f13·f15·f26·f35). |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | VDA 5050 팩트시트(main 스키마의 적재 명세·action 정의), IDTA 02020·02047 서브모델, MassRobotics 공식 스키마, CaSkMan, SkiROS2(스킬 조건 표현 사례, 연계 대상)를 추가한다(f1·f2·f6·f7·f8·f9·f10·f20). |
| 9 | 6. 대표 접근법과 기술 | 어댑터가 능력 선언을 명령으로 옮기는 방식: VDA 5050 팩트시트 action 정의와 주문 action 의 이름 맞물림(관제 사전 검증 의무는 미확인), 제조사 정의 추가 action, Open-RMF 선언 동작–execute_action–execution.finished()(f16·f17·f18·f34). |
| 9 | 7. 관련 표준·프레임워크·오픈소스 | VDA 5050 3.0.0 오류 등급 WARNING·URGENT·CRITICAL·FATAL, 해결 힌트, action 상태 7종(RETRIABLE 포함), 사전 정의 action 29종(dock·lift 없음), MassRobotics 가 식별·상태 보고만 두고 명령 메시지가 없다는 점을 반영한다(f5·f23·f28). |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | 공통 참조 어휘(IEEE 1872-2015의 목적), 의미 식별자(AAS Part 3a IEC 61360, 인용 판 3.0.2·최신 3.1.1, IDTA 02047 의 일부 속성 ECLASS IRDI), 서비스 로봇 모듈 정보 모델(ISO 22166-202:2025, KS B 7321-2 — 부합화 미확인)을 반영한다(f24·f25·f27·f29·f30·f35). |
