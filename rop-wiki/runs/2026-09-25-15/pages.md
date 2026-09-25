# 스토리텔러 산출 2026-09-25-15

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | draft | 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 13절 각주 27건, 트랙 반영 제안 3건(4·7·8절) 반영 |
| create | docs/topics/2026/2026-09-25-area05-s7.md | draft | 자동 분리: 5. 로봇 능력·작업 온톨로지 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,658자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area05-s6.md | draft | 자동 분리: 5. 로봇 능력·작업 온톨로지 의 "6. 대표 접근법과 기술" 절(1,396자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area05-s4.md | draft | 자동 분리: 5. 로봇 능력·작업 온톨로지 의 "4. 핵심 개념과 용어" 절(1,115자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area05-s8.md | draft | 자동 분리: 5. 로봇 능력·작업 온톨로지 의 "8. 대표 연구와 자료" 절(1,010자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 5. 로봇 능력·작업 온톨로지 | 영역 심화: 3~11절 신규 작성(능력·스킬 구분, VDA 5050 팩트시트·MassRobotics·Open-RMF 능력 선언, IDTA 02020·CaSkMan·SSN·IEEE 1872 계열·ISO 22166-201·KS B 7321-2, 적치 시나리오, 열린 질문 2건 신규·oq-004 연결), 트랙 반영 제안 3건 반영 | run 2026-09-25-15
- 홈 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 영역 심화 초안 작성(능력·스킬 구분, 제조사 능력 선언 규격 비교, 적치 시나리오, 열린 질문 2건 추가)
- 대분류 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 3~11절 신규 작성, VDA 5050 팩트시트·MassRobotics·IDTA 02020 등 능력 표현 표준 정리
- 세부영역 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 3~11절 신규 작성, 트랙 반영 제안 3건(4·7·8절) 반영, oq-004 연결

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 스킬 | Skill | 구현과 무관하게 명세한 능력(capability)을 실제로 실행하는 캡슐화된 구현으로, OPC UA 같은 호출 인터페이스를 가지며 상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계). | 5, 9, 12 | ref-126, ref-128 |
| new | 팩트시트 | Factsheet (VDA 5050) | VDA 5050에서 이동로봇이 유형 명세·물리 파라미터·지원 동작·적재 명세를 관제에 미리 알리는 메시지이다. | 5, 9 | ref-125 |
| new | 자산관리셸 | Asset Administration Shell (AAS) | 산업 자산의 정보를 서브모델 단위로 표준화해 디지털로 표현·교환하게 하는 인더스트리 4.0의 디지털 표현 구조이다. | 5, 28 | ref-126, ref-131 |
| new | 형상 제약 언어 | Shapes Constraint Language (SHACL) | RDF 그래프가 정해진 구조·값 조건을 지키는지 검증하는 W3C 제약 언어로, 생성된 온톨로지의 품질 검사에 쓰인다. | 5, 27 | ref-135 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-125 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-126 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-127 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-128 | CaSkade-Automation (GitHub) | CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README) | 오픈소스 문서 | high | https://github.com/CaSkade-Automation/CaSkMan |
| ref-129 | Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub) | IndustrialStandard-ODP-IEEE1872-2 — README (IEEE 1872.2 AuR ontology OWL implementation) | 오픈소스 문서 | medium | https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2 |
| ref-130 | EASE CRC (ease-crc/soma) | SOMA — README (Socio-physical Model of Activities) | 오픈소스 문서 | high | https://github.com/ease-crc/soma |
| ref-131 | IDTA(Industrial Digital Twin Association) | IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles |
| ref-132 | W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub) | ssn/integrated/ssn-system.ttl (SSN System Capabilities module) | 표준 | medium | https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl |
| ref-133 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-134 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 논문 | medium | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems |
| ref-135 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | On the Use of Large Language Models to Generate Capability Ontologies | 논문 | medium | https://arxiv.org/abs/2404.17524 |
| ref-136 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 논문 | medium | https://arxiv.org/abs/2606.17073 |
| ref-137 | ISO | ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules | 표준 | medium | https://www.iso.org/standard/82334.html |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 |
| ref-139 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 논문 | medium | https://arxiv.org/abs/2501.08726 |
| ref-025 | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 표준 | medium | https://ieeexplore.ieee.org/document/7084073/ |
| ref-026 | IEEE | IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology | 표준 | medium | https://standards.ieee.org/standard/1872_2-2021.html |
| ref-027 | Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G. | KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents | 논문 | medium | https://ai.uni-bremen.de/papers/beetz18knowrob.pdf |
| ref-028 | Beßler, D. 외 | Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents | 논문 | medium | https://arxiv.org/pdf/2011.11972 |
| ref-029 | McDermott, D. 외 | PDDL - The Planning Domain Definition Language | 논문 | medium | https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language |
| ref-035 | Plattform Industrie 4.0 | Information Model for Capabilities, Skills & Services | 정부·연구기관 | medium | https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html |
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. | A Capability and Skill Model for Heterogeneous Autonomous Robots | 논문 | medium | https://arxiv.org/abs/2209.10900 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 논문 | medium | https://www.nature.com/articles/s41598-025-16649-3 |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. | A survey of ontology-enabled processes for dependable robot autonomy | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full |
| ref-043 | 신민종, 한영석, 정재윤 | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | VDA 5050 팩트시트의 loadType 과 MassRobotics 의 cargoType 이 자유 문자열일 때 팔레트·용기 같은 적재물 유형을 제조사 사이에 같은 의미로 맞출 공통 어휘나 코드 체계가 있는가? | 5, 7 | 열림 | — |
| new | — | 제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가? | 5, 8, 13 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 적치 | 시작 조건 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |
| 적치 | 작업 대상 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |
| 적치 | 수행 자원 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |
| 적치 | 제약 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |
| 적치 | 완료·인계 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |
| 적치 | 예외·성과 | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 5. 로봇 능력·작업 온톨로지 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02020 Capability Description 1.0 | 표준 | IDTA(Industrial Digital Twin Association) | 5, 28 | ref-126 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 | 표준 | IDTA(Industrial Digital Twin Association) | 5, 28 | ref-131 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles |
| CaSkMan | 오픈소스 | CaSkade-Automation (GitHub) | 5 | ref-128 | https://github.com/CaSkade-Automation/CaSkMan |
| SOMA (Socio-physical Model of Activities) | 오픈소스 | EASE CRC | 5 | ref-130 | https://github.com/ease-crc/soma |
| IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) | 오픈소스 | Helmut Schmidt University, Institute of Automation Technology | 5, 28 | ref-129 | https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2 |
| ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 | 표준 | ISO | 5, 28 | ref-137 | https://www.iso.org/standard/82334.html |
| KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 표준 | 국가표준인증통합정보시스템(KSSN) | 5, 28 | ref-138 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 |

## 추가 조사 요청

- 7절: IDTA 02047 Technical Data for AGV 1.0 의 세부 필드(적재량·치수·속도 등)가 README 범위에서 미확인이라, 명세 본문을 열어 VDA 5050 팩트시트 적재 명세와 비교할 근거가 필요하다.
- 7·11절: KS B 7321-2 의 제정일, ISO 22166-202 부합 여부, 제1부 존재 여부를 확인해야 oq-004 의 부분 근거를 보강할 수 있다.
- 8절: ref-133(Electronics 2026) 저자 미확인 — 참고문헌 기관 표기를 채울 서지 확인이 필요하다.
- 6절: 물류 로봇 매뉴얼에서 능력 모델을 LLM 으로 추출한 공개 사례를 찾지 못했다 — 매뉴얼 해석 적용 사례가 있으면 6절과 21. 온보딩·설정·현장 시운전 연결을 보강할 수 있다.
- 출처 기록: ref-126·ref-131 은 1차 검증자가 raw 경로로 열어 일치를 확인했으나 브리프에 fetched false 로 기록돼 원문 미열람 표시를 유지했다. 다음 실행에서 fetched 기록을 바로잡을지 확인이 필요하다.
- 6절: VDA 5050·Open-RMF 의 이름 기반 동작 선언과 IDTA 02020·CaSkMan 의 능력–스킬 모델을 서로 매핑한 표준·구현이 있는지 조사가 필요하다(현재 [추정]).

## 이행한 수정 지시

- f15 문구 수정 — 7절 표의 IEEE 1872.2 행을 'IEEE 1872.2 AuR 온톨로지(표준은 상위 온톨로지 DUL·SUMO를 씀)의 OWL 구현으로, SUMO는 OWL 표현이 없어 제외하고 DUL만 포함한 제3자 구현'으로 썼다.
- f10 CSS 계열 한정 — 4절 스킬 항목에서 능력·스킬 구분만 IDTA 02020·CaSkMan 공통 [사실]로 두고, CSS 참조 모델 기반은 CaSkMan(ref-128)에만 [사실]로, IDTA 02020 과 CSS 의 관계는 ref-035 근거 [추정]으로 썼다.
- f33 적용 분야 삭제 — 8절 Meseguer Valenzuela·Blanes Noguera 항목을 '이동로봇 플릿의 작업 배정 문제'로 쓰고 '의료·물류 등'을 넣지 않았다.
- f13 인용 — 4절 운용 범위·생존 범위 항목과 7절 SSN 행에서 원문을 직접 인용하지 않고 재서술했다.
- ref-134 발행일 — 13절 각주와 reference_updates 의 발행일을 2022 로 썼다.
- ref-137 발행일 — 13절 각주와 reference_updates 의 발행일을 2024-02 로 썼다.
- ref-135 저자 — 13절 각주와 reference_updates 의 기관을 'Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.'로 썼다.
- 원문 미열람 표기 — fetched false 출처(ref-025~029, ref-035, ref-038, ref-041~043, ref-126, ref-131, ref-133~139) 각주에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 와 '원문 미열람. ' 요약 머리를 넣었으며, fetched true 출처(ref-040, ref-105, ref-125, ref-127~130, ref-132)에는 붙이지 않았다.
- 재인용 범위 — f16~f22·f28 을 7·8절에서 존재·제목·게재 사실 범위로만 쓰고, f22(신민종 외) 항목에 '능력 기술을 포함하는지는 미확인'을 함께 적었다.
- f24 위치 — 5절 시나리오에 넣지 않고 6·8절에서 제조 조립(라인리스 이동 조립 시스템) 대상 연구로 밝혀 방법 참고로만 썼다.
- f25·f26·f31 교차 연결 — 6절에 교차 규칙을 밝히고 10절에 27. AI·학습·적응과 모델 운영과 21. 온보딩·설정·현장 시운전을 모두 연결했으며, f25 의 '오류가 거의 없었다'를 저자들의 보고로 썼다.
- f5·f19 연결 — 10절의 8. 실시간 세계 상태·데이터 일관성 항목을 현재 상태 표현으로만 쓰고 22. 시뮬레이션·예측용 디지털 트윈은 언급하지 않았다.
- 용어 — 4절 능력 항목 첫 등장에서 용어집 CSS 항목·온톨로지 초안의 '기능(Capability)'과 같은 뜻임을 밝혔고, glossary_updates 의 스킬 정의를 '상태 기계를 가질 수 있다(예: CaSkMan 의 ISA 88 상태 기계)'로 고쳤다.
- oq-004 — 해결로 바꾸지 않고(open_question_updates 에 상태 변경 없음) 11절에서 열림으로 연결하며 f27·f28(ISO 22166-201, KS B 7321-2)을 부분 근거로 적었다.
- 트랙 반영 제안 3건 — 4절(능력·스킬, 전제조건·효과, 광고·운용 능력), 7절(IEEE 1872 계열, SSN System Capabilities, IDTA 02020), 8절(KnowRob 2.0, SOMA, RCO, 서베이, 이종 자율 로봇 능력·스킬 모델, 국내 KCI)에 반영했고, 7절 IDTA 02020 은 제3자 논문 경유 [추정]이 아니라 f9(ref-126, 원문 미열람 표기)를 근거로 [사실]로 썼다.
- 분량 초과 자동 분리: 5. 로봇 능력·작업 온톨로지 본문 8,395자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,815자
