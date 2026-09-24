# 스토리텔러 산출 2026-09-25-02

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md | draft | q1-01·q1-02 답함, q1-03 부분 답, 후속 질문 4건(q1-07·q1-08·q4-06·q5-05), 완료 조건 미충족 평가, 출처 20건(원문 미열람), 이력 행 추가 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | draft | 온톨로지 v0 → v0.1: 개념 효과·스킬·오류 추가(확정), 기능 속성에 능력 출처 구분 추가(초안 → 확정), 관계 기능 / 구현된다 / 스킬 추가, 다이어그램 갱신, 전제조건·스킬 상태 기계 등은 6절 질문으로 |
| update | docs/tracks/manual-capability-ontology/model-standard-comparison.md | draft | 비교표 초안: 후보 10행의 발행 기관·종류 채움, 근거 finding이 있는 정보 항목 칸만 태그와 함께 채움(나머지 미조사), 모든 행 원문 미열람, 후보 밖 2행(RCO, 이종 자율 로봇 능력·스킬 모델) 추가, 빠진 정보 요약·출처·이력 갱신 |
| update | docs/tracks/manual-capability-ontology/index.md | draft | 상태 줄의 마지막 트랙 실행을 2026-09-25로 갱신(현재 단계 유지), 6절 산출물 링크의 현재 상태(온톨로지 v0.1, 비교표 초안, 백로그 수치) 갱신, ref-004 각주에 원문 미열람 표시 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 | q1-01·q1-02 답함, q1-03 부분 답, 후속 질문 4건, 모델·표준 비교표 초안, 능력 온톨로지 초안 v0 → v0.1(모든 출처 원문 미열람) | run 2026-09-25-02
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 1: q1-01·q1-02 답함, q1-03 부분 답, 모델·표준 비교표 초안, 능력 온톨로지 초안 v0 → v0.1(원문 미열람 환경)
- 대분류 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 트랙 매뉴얼 기반 로봇 기능 온톨로지 단계 1에서 기존 능력 표현 모델·표준(IEEE 1872 계열, SSN/SOSA, CSS·AAS, VDA 5050 등)을 조사하고 이 영역 4·7·8절 반영을 제안
- 세부영역 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 트랙 단계 1 결과의 반영 제안(4. 핵심 개념과 용어, 7. 관련 표준·프레임워크·오픈소스, 8. 대표 연구와 자료) — 반영은 다음 영역 실행에서

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 로봇·자동화 핵심 온톨로지 | Core Ontology for Robotics and Automation (CORA) | IEEE 1872-2015가 정한 로봇·자동화 분야의 가장 일반적인 개념·관계·공리를 담은 핵심 온톨로지이다. | 5, 28 | ref-025, ref-026 |
| new | 능력·스킬·서비스 모델 | Capabilities, Skills and Services (CSS) Model | Plattform Industrie 4.0 작업반이 제안한 정보 모델로, 구현과 무관한 기능 명세(능력)와 그 실행 가능한 구현(스킬), 제공 형태(서비스)를 구분한다. 이 위키의 온톨로지 초안에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다. | 5, 28 | ref-035, ref-036 |
| new | 팩트시트 | Factsheet (VDA 5050) | VDA 5050에서 차량이 자신의 기능 정보를 상위 관제에 미리 알리는 메시지(토픽)이다. | 9, 5 | ref-022 |
| new | 계획 도메인 정의 언어 | Planning Domain Definition Language (PDDL) | 자동 계획 문제에서 행동을 파라미터·전제조건·효과로 기술하고 도메인과 문제 인스턴스를 분리해 표현하는 언어이다. | 5 | ref-029 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 표준 | medium | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| ref-025 | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 표준 | medium | https://ieeexplore.ieee.org/document/7084073/ |
| ref-026 | IEEE | IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology | 표준 | medium | https://standards.ieee.org/standard/1872_2-2021.html |
| ref-027 | Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G. | KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents | 논문 | medium | https://ai.uni-bremen.de/papers/beetz18knowrob.pdf |
| ref-028 | Beßler, D. 외 | Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents | 논문 | medium | https://arxiv.org/pdf/2011.11972 |
| ref-029 | McDermott, D. 외 | PDDL - The Planning Domain Definition Language | 논문 | medium | https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 표준 | medium | https://www.w3.org/TR/vocab-ssn/ |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 표준 | medium | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN |
| ref-033 | MassRobotics | Autonomous Mobile Robot Standards Published by MassRobotics | 표준 | medium | https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/ |
| ref-034 | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 표준 | medium | https://reference.opcfoundation.org/specs/OPC-40010-1 |
| ref-035 | Plattform Industrie 4.0 | Information Model for Capabilities, Skills & Services | 정부·연구기관 | medium | https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html |
| ref-036 | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 논문 | medium | https://arxiv.org/abs/2209.09632 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 논문 | low | https://arxiv.org/abs/2307.00827 |
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. | A Capability and Skill Model for Heterogeneous Autonomous Robots | 논문 | medium | https://arxiv.org/abs/2209.10900 |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/task_types.html |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 논문 | medium | https://www.nature.com/articles/s41598-025-16649-3 |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. | A survey of ontology-enabled processes for dependable robot autonomy | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full |
| ref-043 | 신민종, 한영석, 정재윤 | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? | 28, 5 | 열림 | — |
| new | — | 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. | 9, 28 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) | 표준 | IEEE | 5, 28 | ref-025 | https://ieeexplore.ieee.org/document/7084073/ |
| IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology | 표준 | IEEE | 5, 28 | ref-026 | https://standards.ieee.org/standard/1872_2-2021.html |
| W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) | 표준 | W3C / OGC | 5 | ref-030 | https://www.w3.org/TR/vocab-ssn/ |
| VDA 5050 (3.0.0) | 표준 | VDA(Verband der Automobilindustrie) | 9, 28 | ref-032 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN |
| MassRobotics AMR Interoperability Standard (1.0) | 표준 | MassRobotics | 9, 28 | ref-033 | https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/ |
| OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) | 표준 | OPC Foundation / VDMA | 9, 28 | ref-034 | https://reference.opcfoundation.org/specs/OPC-40010-1 |
| Information Model for Capabilities, Skills & Services (CSS) | 프레임워크 | Plattform Industrie 4.0 | 5, 28 | ref-035 | https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html |

## 추가 조사 요청

- 단계 1 q1-03(비교표 4절의 다섯 정보 항목 열): 후보별 전제조건·파라미터 범위·적재·환경 제약·완료 확인 방법·오류의 의미 충족 정도를 원문으로 확인해야 한다 — 이번 실행은 원문 미열람으로 대부분 미조사로 남았다.
- VDA 5050 3.0.0 원문: 정확한 발행일, 확장 기능 목록(구역·경로 공유·오류 등급·절전 action), 팩트시트 필드의 2.0.0 대비 변경 — f12의 기능 목록이 [추정]으로 강등됐고 GitHub main 브랜치 판이 미확인이다(q1-07).
- IDTA 02020 Capability Description 서브모델을 IDTA 발행 원문으로 확인 — 현재는 제3자 논문(ref-037) 경유 [추정]이다.
- CSS 계열 스킬의 FeasibilityCheck·PreconditionCheck, 상태 기계·OPC UA/REST 호출 설명의 정확한 출처 확정 — 출처 미확정으로 본문과 온톨로지 초안에 넣지 못했다.
- OPC 40010-1의 현재 판·발행일과 Part 2 이후 부의 범위 — 작업 단위 능력·완료 확인이 범위 밖인지(f24) 확인이 필요하다.
- MassRobotics AMR 상호운용 표준 setup·status 메시지 필드 목록과 2.0 현재 상태(q1-08).
- 국내 KCI 논문(신민종·한영석·정재윤, 2024)의 본문 내용 — 5. 로봇 능력·작업 온톨로지 8절 반영에 필요하다.
- 핵심 주장의 독립 2차 출처 교차 확인 — 이번 실행은 교차 확인 0건이다.
- q1-06(ROP용 능력 개념 요구 목록) 조사 — 단계 1 완료 조건 둘째 항목에 필요하다.
- ref-025 id가 이전 실행 2026-09-25-01의 미등록 출처와 겹치는지 퍼블리셔 확인 필요(리서치·검증 기록).

## 이행한 수정 지시

- 모든 각주 원문 미열람 표시 — 네 페이지의 모든 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙였고(트랙 개요 ref-004 포함), reference_updates 20건 모두에 source_unopened: true를 넣었다.
- f10 강등 — 단계 페이지 q1-02에서 [추정]으로 쓰고 제조사 제공 의무 문구를 빼고 '팩트시트 토픽으로 기능을 관제에 미리 알린다'까지만, 'VDA 5050 2.0.0(2022년 1월판) 기준'을 명시했다.
- f12 분리 — '3.0.0판이 2026년에 발행되어 자율도 높은 이동로봇 통합을 위해 인터페이스를 확장했다'는 [사실]로, 구역·경로 공유·CRITICAL/URGENT·절전 action 목록은 '검색 요약 기준이며 원문 미열람'을 병기한 [추정]으로 썼다.
- ref-032 발행일 — 각주·reference_updates 발행일을 2026-04로 적고 본문에 '3.0.0 발행 2026-03, 보도자료 2026-04'로 쓰며 정확한 일자는 단정하지 않았다(남은 불확실성에 요약 일자와 URL 불일치 기재).
- 판 명시 — f10·f22 문장은 2.0.0 기준, f11 문장과 비교표 칸은 '판 미확인 — GitHub main 브랜치, 구현 라이브러리 문서 혼재'로 적고, 단계 페이지와 비교표 VDA 5050 행에 3.0.0 발행 사실을 함께 적었다.
- f16 — 본문 사실·추정 문장에서 빼고 단계 페이지 4절 남은 불확실성에 'CSS 계열 스킬의 FeasibilityCheck·PreconditionCheck 설명은 출처 미확정'으로만 두었다.
- f17 강등 — 단계 페이지 q1-02에서 [추정]과 'IDTA 원문 미열람, 제3자 논문 경유'를 병기하고, 비교표 AAS 행의 해당 칸에도 같은 표시를 했다.
- ref-037 — 기관을 'Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A.', 발행일을 2023-07로 고치고 신뢰도는 low로 두었다(각주·reference_updates).
- ref-041 — 기관을 'Naqvi, M. R. 외(Scientific Reports)', 발행일을 2025-10-02로 고쳤다(각주·reference_updates).
- f25 — 'CSS 계열 스킬 모델이 전제조건·효과를 담는다'를 빼고 전제조건·효과는 PDDL로만 적었으며, IDTA 02020 부분은 제3자 논문 경유 [추정] 문장으로 따로 두었다(단계 페이지 q1-03, 비교표 5절).
- f21 — 저자·학술지·권호·쪽·2024 게재 사실만 쓰고 '논문 본문 내용은 미확인'을 병기했으며 본문 내용은 서술하지 않았다.
- 발행일 미확인 — ref-031·ref-034·ref-039·ref-040 각주 발행일 자리에 '미확인'을 쓰고, OPC 40010-1은 본문과 비교표에 '판·발행일 미확인'으로 적었다.
- 전제조건 개념 거부 — 개념 표에 넣지 않고 온톨로지 초안 6절 '실행 조건과 제약의 경계' 항목에 '전제조건(PDDL 행동 전제조건, f5)을 실행 조건과 별도 개념으로 둘지'를 덧붙였다.
- 효과 승인 — 개념 표에 상태 '확정'으로 넣고 근거 출처 칸에 f5·f15와 각주 ref-029·ref-035를 두었다.
- 스킬 승인 — 정의를 '기능(능력)의 실행 가능한 구현'으로 한정해 '확정'으로 넣고, 상태 기계·OPC UA·REST 호출 설명은 6절 미해결 질문으로 옮겼다.
- 관계 기능 / 구현된다 / 스킬 — 관계 표에 넣고 근거 칸에 ref-035·ref-037과 'ref-037은 원문 미열람, IDTA 원문 아님'을 병기했다.
- 오류 승인 — 속성을 유형, 등급(VDA 5050 2.0.0의 WARNING·FATAL), 설명, 복구 가능성(미확인)으로 적고 3.0 등급은 뺐으며 상태 '확정'으로 넣었다.
- 기능 수정 — 속성에 '능력 출처 구분(광고 능력 / 운용 능력)'을 더하고 상태를 초안 → 확정으로 바꿨으며(근거 f8), 매뉴얼 값이 광고 능력이라는 해석(f27)은 [추정]으로 병기했다.
- 온톨로지 버전 — 프런트매터 ontology_version, H1 '(v0.1)', 상태 줄 'v0.1', JSON ontology_draft_version 네 곳을 '0.1'로 맞추고 페이지 version을 2로 올렸으며 다이어그램에 효과·스킬·오류와 '구현된다' 관계를 반영했다.
- 자산관리셸 용어 — glossary_updates에 넣지 않았고, 본문 표기는 '자산관리셸'로 통일하고 국내 논문 제목만 원문 표기 '자산관리쉘'로 두었다.
- 팩트시트 용어 — 정의를 'VDA 5050에서 차량이 자신의 기능 정보를 상위 관제에 미리 알리는 메시지(토픽)이다.'로 줄이고 블록 목록은 넣지 않았다.
- 능력·스킬·서비스 모델 용어 — 정의 끝에 '이 위키의 온톨로지 초안에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다.'를 더했고, 단계 페이지·온톨로지 초안 본문에도 대응 관계를 한 번 밝혔다.
- 질문 상태 — 단계 페이지 2절에서 q1-01·q1-02를 답함(2026-09-25-02, #q1-01·#q1-02)으로, 3절 소제목에 {#q1-01}·{#q1-02}를 붙였고, q1-03은 표에서 열림·백로그 조사 중·answer_link null로 두었으며 q1-04~q1-06은 바꾸지 않았다.
- 비교표 — 발행 기관·종류는 finding이 있는 행만 채우고, 정보 항목 칸은 f5·f7·f11·f17·f22·f26이 직접 뒷받침하는 칸만 태그와 함께 채우고 나머지는 미조사로 두었으며, 모든 행 상태를 '원문 미열람'으로 하고 RCO(f8)·이종 자율 로봇 능력·스킬 모델(f18) 행을 근거 finding id와 함께 후보 밖 행으로 추가했다.
- 세부영역 반영 제안 — 5. 로봇 능력·작업 온톨로지, 9. 로봇·제조사 관제 연동, 28. 표준·상호운용성·다사업자 거버넌스 페이지는 고치지 않고 area_reflection_proposals와 트랙 로그에만 남겼으며, 28. 표준·상호운용성·다사업자 거버넌스 제안의 VDA 5050 3.0 기능 목록은 [추정]으로 표시했다.
- 완료 조건 — 단계 페이지 6절 두 행을 모두 미충족(검증 판정 '미충족 · 미승인')으로, 상태 줄 완료 조건을 미충족으로, 전환 줄을 지시 문구 그대로 '아니오(…막힌 질문 q1-03·q1-04·q1-05·q1-06)'로 썼고, 트랙 개요 상태 줄은 마지막 트랙 실행 2026-09-25, 현재 단계 '단계 1. 기존 능력 표현 모델과 표준 조사'로 유지했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
- 온톨로지 초안 버전: 0.1
- 트랙 로그 항목: 답한 질문: q1-01, q1-02 (q1-03 부분 답 — 후보별 다섯 정보 항목 충족 정도를 원문으로 확인하지 못함) / 새 질문: q1-07(f12), q1-08(f13), q4-06(f17), q5-05(f27) / 온톨로지 변경: v0 → v0.1: 개념 '효과' 추가(f5·f15), 개념 '스킬' 추가(f15·f17, 정의 축소), 개념 '오류' 추가(f22·f26, 3.0 등급 제외), 관계 '기능 / 구현된다 / 스킬' 추가(f15·f17), 개념 '기능'에 속성 '능력 출처 구분(광고 능력 / 운용 능력)' 추가·초안 → 확정(f8); 거부: '전제조건'(기존 '실행 조건'과 정의가 겹쳐 6절 미해결 모델링 질문으로 이동) / 완료 조건 평가: 미충족(부족: 모델·표준 비교표의 다섯 정보 항목 열 대부분 미조사, ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 미반영 — q1-06 미조사) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지 3건, 9. 로봇·제조사 관제 연동 1건, 28. 표준·상호운용성·다사업자 거버넌스 1건 / 다음 실행 제안: q1-06, q1-04, q1-05, q1-03 보완(원문 열람 가능 환경), q1-07, q1-08 / 비고: 모든 출처 원문 미열람(web_fetch_available: false), 교차 확인 0건, ref-025 id가 이전 실행 2026-09-25-01의 미등록 출처와 겹치는지 퍼블리셔 확인 필요
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 6, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-01 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-01 | — | — | — |
| q1-02 | 답함 | docs/tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md#q1-02 | — | — | — |
| q1-03 | 조사 중 | — | — | — | — |
| q1-07 | 열림 | — | VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가? | 1 | f12 |
| q1-08 | 열림 | — | MassRobotics AMR 상호운용 표준의 setup·status 메시지 스키마에는 로봇 능력(적재량, 지원 작업, 부착 장비)을 기술하는 필드가 있는가? | 1 | f13 |
| q4-06 | 열림 | — | IDTA 02020 능력 서브모델의 속성·제약(ConditionContainer)과 VDA 5050 팩트시트의 적재 명세·지원 action 을 서로 매핑할 수 있는가, 매핑하면 무엇이 남는가? | 4 | f17 |
| q5-05 | 열림 | — | 제조사 매뉴얼에서 추출한 광고 능력과 현장 시험으로 확인한 운용 능력의 차이를 어떤 지표로 측정하고 온톨로지에 함께 기록할 것인가? | 5 | f27 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 4. 핵심 개념과 용어 | 5. 로봇 능력·작업 온톨로지: 능력(구현 독립 기능 명세)과 스킬(실행 가능한 구현)의 구분(CSS, f15), 행동의 전제조건·효과(PDDL, f5), 광고 능력·운용 능력 구분(RCO, f8)을 용어로 반영한다. 모두 원문 미열람(실행 2026-09-25-02). |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | 5. 로봇 능력·작업 온톨로지: IEEE 1872-2015 CORA(f1), IEEE 1872.2-2021(f2), W3C/OGC SSN/SOSA와 System Capabilities 모듈(f6·f7), Plattform Industrie 4.0 CSS 토론 문서(f15), IDTA 02020 능력 서브모델([추정], IDTA 원문 미열람·제3자 논문 경유, f17)을 반영한다. |
| 5 | 8. 대표 연구와 자료 | 5. 로봇 능력·작업 온톨로지: KnowRob 2.0(f3), SOMA(f4), RCO(f8), 온톨로지 기반 자율 로봇 신뢰성 서베이(f9), 이종 자율 로봇 능력·스킬 모델(f18), 국내 KCI 논문(신민종·한영석·정재윤, 2024, 게재 사실만, f21)을 반영한다. |
| 9 | 7. 관련 표준·프레임워크·오픈소스 | 9. 로봇·제조사 관제 연동: VDA 5050 2.0.0 팩트시트로 기능을 관제에 미리 알림([추정], f10)과 상태 메시지 오류 보고·action 완료 보고(f22), VDA 5050 3.0.0 발행 사실(f12의 [사실] 부분), MassRobotics AMR 상호운용 표준 1.0 setup·status 메시지(f13), Open-RMF 작업 능력 선언·사용자 정의 동작(f19·f20)을 반영한다. |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | 28. 표준·상호운용성·다사업자 거버넌스: 능력 기술 관련 표준의 발행 기관과 현재 판 — IEEE 1872 계열(f1·f2), VDA 5050 3.0.0 발행 2026-03(보도자료 2026-04, [사실]) 및 3.0 기능 목록(구역·경로 공유·오류 등급·절전 action — [추정], 검색 요약 기준·원문 미열람, f12), MassRobotics 1.0(f13), OPC 40010-1(판·발행일 미확인, f14), CSS 토론 문서(f15)를 반영한다. |
