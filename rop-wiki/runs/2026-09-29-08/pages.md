# 스토리텔러 산출 2026-09-29-08

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md | draft | 영역 심화: 섹션 3~11 신규 작성(finding 28건 반영, 1차 조건부 승인 수정 13건·2차 수정 2건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 |
| create | docs/topics/2026/2026-09-29-area06-s6.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "6. 대표 접근법과 기술" 절(3,102자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s8.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "8. 대표 연구와 자료" 절(1,873자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s4.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "4. 핵심 개념과 용어" 절(1,115자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s11.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "11. 열린 질문" 절(1,074자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s7.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,042자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s10.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,018자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area06-s3.md | draft | 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "3. 왜 중요한가" 절(666자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 6. 온톨로지 기반 시스템·로봇 연동 | 영역 심화: 섹션 3~11 신규 작성(finding 28건 반영, 1차 조건부 승인 수정 13건·2차 수정 2건 이행), version 2. 참고문헌 번호 충돌 확인 필요(ref-038·037·880·881·883 은 실행 2026-09-29-07 의 다른 URL 과 겹치고, ref-869 는 대분류 페이지 자료 목록의 OPC 40010-1 과 겹치므로 퍼블리셔가 URL 기준으로 합쳐야 한다) | run 2026-09-29-08
- 홈 최근 업데이트: 2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 영역 심화로 3~11절 신규 작성. 능력→스킬→인터페이스 연결 구조와 실행 조건 검사는 여러 출처에서 확인되지만, 능력 모델에서 어댑터 설정을 자동 생성한 사례와 근거를 함께 돌려주는 후보 질의는 미확인
- 대분류 최근 업데이트: 2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 영역 심화로 3~11절 신규 작성(finding 28건, 1차 조건부 승인 수정 13건·2차 수정 2건 이행). 병원 사례 2건·기타(오피스 빌딩) 1건, 새 열린 질문 4건, 용어 3건 신규
- 세부영역 최근 업데이트: 2026-09-29 — 6. 온톨로지 기반 시스템·로봇 연동: 3~11절 신규 작성. 능력 기반 후보 질의·능력–실행 연결·연동 자동화·실행 시점 조건 판단 네 갈래를 정리했고, oq-150 은 부분 진전만 있어 미해결로 남았다

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 스킬 인터페이스 | Skill Interface | 능력·스킬·서비스 모델에서 스킬을 외부에서 제어하기 위해 반드시 두는 접점(예: OPC UA 서버)으로, 스킬 구현과 분리되어 같은 스킬을 여러 프로토콜로 노출할 수 있게 한다. | 5, 6, 20 | ref-882 |
| new | 전제·유지·사후 조건 | Pre-, Hold-, Post-condition | 스킬이 시작될 때 참이어야 하는 조건(전제), 실행 중 계속 유지되어야 하는 조건(유지), 끝난 뒤 성립해야 하는 조건(사후)으로 스킬을 정의해 실행 가능 여부 판단과 완료 확인에 쓰는 방식이다. | 5, 6, 29 | ref-881 |
| new | 수행 가능 동작 | Performable Action (Open-RMF perform_action) | Open-RMF 에서 플릿이 지원한다고 선언한 사용자 정의 동작으로, 플릿 어댑터가 수락 여부를 판단하고 실행하는 동안 관제는 로봇 제어를 넘기고 교통 협상에서 제외한다. | 6, 20 | ref-880 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University) | A Capability and Skill Model for Heterogeneous Autonomous Robots | 논문 | medium | https://arxiv.org/abs/2209.10900 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택) | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 논문 | medium | https://arxiv.org/abs/2606.02167 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 논문 | medium | https://arxiv.org/abs/2307.00827 |
| ref-249 | Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS) | Ontological Component-based Description of Robot Capabilities | 논문 | medium | https://arxiv.org/abs/2306.07569 |
| ref-880 | Open Robotics (Programming Multiple Robots with ROS 2) | User-defined Tasks - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task_userdefined.html |
| ref-881 | Mayr, M., Rovida, F., & Krueger, V. (Lund University, IROS 2023) | SkiROS2: A skill-based Robot Control Platform for ROS | 논문 | medium | https://arxiv.org/abs/2306.17030 |
| ref-882 | CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소 | CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README) | 오픈소스 문서 | high | https://github.com/CaSkade-Automation/CSS |
| ref-883 | Nagrath, V., Blender, T., Shaik, N., & Schlegel, C. | Industry 4.0 Asset Administration Shell (AAS): Interoperable Skill-Based Service-Robots | 논문 | medium | https://arxiv.org/abs/2208.01273 |
| ref-229 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-885 | Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel) | HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/ |
| ref-886 | ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda) | vda5050_connector - ROS Package Overview | 오픈소스 문서 | high | https://index.ros.org/p/vda5050_connector/ |
| ref-887 | Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo) | An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell | 논문 | medium | https://zenodo.org/records/5648095 |
| ref-888 | 황선명 (대전대학교, 보안공학연구논문지 8(1)) | 온톨로지 기반의 로봇 동적재구성에 관한 연구 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055 |
| ref-889 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART) | Robot-Lift Integration Challenge \| Changi General Hospital | 정부·연구기관 | medium | https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge |
| ref-890 | Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97) | Capability matchmaking software for rapid production system design and reconfiguration planning | 논문 | medium | https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/ |
| ref-153 | Open Robotics (Programming Multiple Robots with ROS 2) | Fleet Adapter Tutorial (integration_fleets_action_tutorial) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 논문 | medium | https://arxiv.org/abs/2406.07962 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? | 6, 20, 4 | 열림 | — |
| new | — | Open-RMF 사용자 정의 동작이 교통 협상에서 빠지고 문·승강기 조작을 맡지 않을 때, ROP 는 그 동작의 배터리·설비 상태 같은 실행 시점 조건을 어디에서 검사하고 실패를 어떻게 복구하는가? | 6, 28, 29 | 열림 | — |
| new | — | 국내 현장에서 온톨로지나 능력 모델로 이기종 로봇 후보를 질의해 배정·연동한 운영 사례가 있는가(이번 조사에서 확인된 국내 자료는 2011년 연구 한 건뿐이다)? | 6, 25 | 열림 | — |
| new | — | 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? | 6, 21, 5 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 병원 | 작업 대상 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 병원 | 수행 자원 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 병원 | 제약 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 기타 | 시작 조건 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 기타 | 작업 대상 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 기타 | 수행 자원 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 기타 | 제약 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |
| 기타 | 예외·성과 | docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md#5-적용-사례-현장-유형-명시 | 6. 온톨로지 기반 시스템·로봇 연동 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) | 오픈소스 | CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) | 5, 6, 20 | ref-882 | https://github.com/CaSkade-Automation/CSS |

## 추가 조사 요청

- 6. 대표 접근법과 기술: 등록된 능력 모델에서 플릿 어댑터 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례 — 1절의 '온톨로지 기반 연동 자동화' 항목을 사례 없이 추정으로만 서술했다.
- 6. 대표 접근법과 기술: 능력 기반 후보 질의가 후보와 함께 근거(설명)를 돌려주는 구현이나 연구 — 1절이 요구하는 설명 기능을 어느 출처도 명시하지 않았다.
- 6. 대표 접근법과 기술(실행 시점 조건 판단): MDPI Electronics 15(16):3562 'Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation'(배터리·층 접근 조건의 의미 기반 실행 가능성 추론)의 열람 — 브리프가 403 으로 열지 못해 이 페이지에서 쓰지 못했다. 참고문헌 색인에 ref-236 으로 같은 제목이 있으므로 원문 열람 뒤 이 영역 finding 으로 다시 내야 한다.
- 5. 적용 사례: 제조 공장·물류창고·상업 시설 현장에서 온톨로지나 능력 모델로 이기종 로봇을 연동한 사례 — 이번 조사는 병원 2건과 오피스 빌딩 1건만 확인했다.
- 5·11절: 국내 현장의 온톨로지·능력 모델 기반 이기종 로봇 배정·연동 운영 사례 — 확인된 국내 자료는 2011년 KCI 논문 1건뿐이다.
- 7·8절: Plattform Industrie 4.0 CSS 참조 모델 원문(토론 문서)과 Järvenpää 외 'Semantic rules for capability matchmaking'(IJCIM 2022)의 열람 — 브리프가 보안 검증·403 으로 열지 못해 CSS 온톨로지 README 와 탐페레 초록으로 대신했다.
- 참고문헌 정리: 이 브리프의 ref-869(Valner 외 타르투대학교병원)는 대분류 B. 로봇 온톨로지 페이지의 자료 목록에서 ref-869 가 OPC 40010-1(OPC Foundation)로 실려 있어 번호가 겹칠 수 있다. 검증이 지적한 ref-038·037·880·881·883 과 함께 퍼블리셔가 URL 기준으로 합칠 때 확인이 필요하다.

## 이행한 수정 지시

- f12 신뢰도 high → medium 과 문장 분리 — 6절 '실행 시점 조건 판단'에서 'IDTA 02020 능력 기술 서브모델은 전제조건·불변·사후조건을 능력의 속성 제약으로 기술한다'와 '실행 전에 조건을 검사하는 구조는 SkiROS2(전제·유지·사후 조건)와 HERON(SPARQL 전제조건·SHACL 정책)에서 확인된다'로 나누어 썼고, 페이지 신뢰도는 verification.json 의 medium 을 썼다.
- f12·f11 HERON 을 배터리·문·승강기 조건 예로 들지 않음 — 6절에 '배터리·문·승강기 같은 구체 상태를 실행 조건으로 쓴 예로 확인된 것은 Open-RMF 플릿 어댑터의 recharge_threshold·battery_soc 뿐이다'로 썼고, 5절 HERON 사례 서술에 '배터리·문·승강기 같은 구체 상태 조건은 이 사례에서 확인되지 않았다'를 덧붙였다.
- f3 단일 계보 병기 — f3 를 별도 교차 확인 문장으로 쓰지 않고, 4절에서 CSS 온톨로지(ref-882)와 IDTA 02020(ref-229)을 각각 [사실] 단일 출처로 서술했으며 두 모델이 같은 Plattform Industrie 4.0 참조 모델 계보라는 점은 용어집 항목 설명과 6절 능력–실행 연결에 반영했다(교차 확인으로 서술하지 않음).
- f10 'OWL 세계 모델' 교체 — 4절과 6절, 7절 표, 참고문헌 요약에서 '세계 상태와 개체를 추론하는 지식 베이스(세계 모델)'로 썼다.
- f8 문·승강기 문구 수정 — 6절과 4절, 7절 표, 11절 oq-150 항목, 용어집 '수행 가능 동작' 설명에서 '문 열기·승강기 사용은 사용자 정의 동작의 범위에 들어가지 않고 플랫폼이 맡는다'로 썼다.
- f18 직접 인용 제거 — 6절과 7절 표에서 '로봇 플랫폼마다 세 핸들러 플러그인을 정의한 어댑터 패키지를 만들어야 한다'로 재서술했다.
- ref-888 각주 URL 교체 — 13절 각주와 reference_updates 의 URL 을 https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART001533055 로 썼다.
- ref-883 기관란 수정 — 13절 각주와 reference_updates 의 org 에서 'Technische Hochschule Ulm' 을 빼고 저자만 적었다.
- 발행일 미확인·원문 미열람 표기 — ref-882·ref-229·ref-880·ref-886·ref-889(및 ref-153)는 각주 발행일 자리에 '미확인'을 쓰고 본문 기준일을 '2026-09-29 확인'으로 두었으며, ref-229·ref-869·ref-465 는 각주 접근일 뒤 ' (원문 미열람)'과 reference_updates[].source_unopened: true 를 유지했다.
- reference_updates URL 명기와 번호 충돌 기록 — 18건 모두 url 을 적었고 changelog_entry 에 '참고문헌 번호 충돌 확인 필요'를 남겼다(ref-869 의 추가 충돌 가능성도 additional_research_requests 에 적었다).
- 5. 적용 사례 분리 — 병원 사례를 HERON 시뮬레이션(임상 배치 아님 명시)과 타르투대학교병원 현장 시험으로 나눠 각각 '현장 유형: 병원'을 명시하고, f21 은 '현장 유형: 기타'(싱가포르 Galen 오피스 빌딩)로 썼으며, 제조 공장·물류창고 현장 사례는 확인되지 않았다고 서술하고 물류창고를 기본값으로 쓰지 않았다.
- 용어 처리 — 6절 PDDL 첫 등장을 '계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)'로 풀어 쓰고 docs/glossary/pddl.md 에 링크했고, 3절 Open-RMF 첫 등장을 docs/glossary/open-rmf.md 에 링크했으며, 스킬 인터페이스·전제·유지·사후 조건·수행 가능 동작 3건을 glossary_updates 에 신규로 냈다.
- 11. 열린 질문 — oq-150 은 상태를 바꾸지 않고 f28 의 부분 진전만 적었으며(open_question_updates 에 update 를 내지 않음), open_questions_new 4건을 브리프 형식 그대로 질문·관련 영역으로 옮겨 open_question_updates 에 new 로 냈다.
- 2차: changelog_entry 충돌 번호 오기 수정 — 'ref-038·878·880·881·883' 을 'ref-038·037·880·881·883' 으로 고쳤고, additional_research_requests 마지막 항목의 같은 표기도 'ref-038·037·880·881·883' 으로 고쳤다.
- 2차: 5. 적용 사례 (현장 유형 명시) 타르투대학교병원 표의 '시작 조건' 칸에서 'Open-RMF' 를 [Open-RMF](../../glossary/open-rmf.md) 로 링크했다(3절의 기존 링크는 그대로 두어, 코드가 3절을 분리해도 게시되는 세부영역 페이지의 첫 등장에 용어집 링크가 남게 했다). 이전 초안의 분리 주제 페이지 7건은 코드(validate_run)가 만든 부산물이므로 다시 내지 않고, 3~11절 전문을 원 세부영역 페이지 하나로 합쳐 원 초안 형태로 돌려보내 코드가 같은 방식으로 다시 분리하게 했다. 내용은 2차 지시 두 곳 외에 바꾸지 않았다.
- 분량 초과 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 본문 12,735자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,729자
