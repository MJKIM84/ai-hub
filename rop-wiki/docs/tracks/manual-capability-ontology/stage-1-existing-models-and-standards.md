---
title: "단계 1. 기존 능력 표현 모델과 표준 조사"
type: track-stage
track: manual-capability-ontology
stage: 1
related_areas: [5, 27, 9, 28, 16]
tags: [능력 온톨로지, 산업 상호운용 규격, 모델·표준 비교표, ROP용 능력 개념, 능력 매칭]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-022, ref-025, ref-026, ref-027, ref-028, ref-029, ref-030, ref-031, ref-032, ref-033, ref-034, ref-035, ref-036, ref-037, ref-038, ref-039, ref-040, ref-041, ref-042, ref-043, ref-051, ref-228, ref-229, ref-243, ref-231, ref-230, ref-244, ref-245, ref-246, ref-236, ref-247, ref-248, ref-138, ref-249, ref-250, ref-323, ref-329, ref-235, ref-324, ref-325, ref-330, ref-326, ref-327, ref-328, ref-391, ref-392, ref-234, ref-182, ref-183, ref-184, ref-185, ref-198, ref-200, ref-201, ref-437, ref-438, ref-439]
last_run: 2026-09-25
version: 8
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 단계 1. 기존 능력 표현 모델과 표준 조사

# 단계 1. 기존 능력 표현 모델과 표준 조사

> 단계 상태: 진행 중 · 열린 질문: 1건 · 답한 질문: 8건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 로봇의 능력·스킬·작업을 표현하는 기존 온톨로지와 표준이 무엇을 담고 무엇을 못 담는가.

위 문장은 트랙 정의의 "밝힐 것"을 그대로 옮긴 것이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 이 단계는 트랙의 중심 영역인 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)에서 출발한다. 조사 결과는 [모델·표준 비교표](model-standard-comparison.md)와, 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)용 능력 개념 요구 목록 초안의 형태로 [능력 온톨로지 초안](ontology-draft.md)에 반영된다.

## 2. 질문 목록

이 단계의 시작 질문 6개와, 실행 2026-09-25-02에서 생겨 이 단계로 들어온 후속 질문 2개, 실행 2026-09-25-16에서 생겨 이 단계로 들어온 후속 질문 1개다. 시작 질문 문장은 괄호 안의 내용까지 트랙 정의 그대로다. 괄호 안의 이름은 리서치 에이전트가 실재·최신성을 확인해야 할 출처 후보이지 확인된 출처가 아니다. 후보 이름 속 약어(IEEE, PDDL, W3C, VDA, OPC UA 등)는 트랙 정의의 후보 이름 그대로 두며, 실재를 확인한 뒤 발행 기관의 공식 명칭으로 풀어 쓴다. 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. [가정] 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커(예: `#q1-01`) 또는 주제 페이지 링크를 적는다. 뒤 단계에서 되돌아온 질문은 이 단계 태그로 이 표에 추가하고 다음 트랙 실행에서 우선 처리한다. 제기 근거 칸의 값은 [질문 백로그](question-backlog.md)의 항목 형식과 같이 finding id(제안한 실행의 발견 사항 id) 또는 "사용자" 가운데 하나만 쓴다. 시드 질문은 사용자가 정의한 트랙 정의의 시작 질문이므로 백로그와 같게 "사용자"로 적는다.

페이지 상단의 단계 상태 줄(단계 상태 · 열린 질문 · 답한 질문 · 완료 조건 · 마지막 실행)은 퍼블리셔가 다시 쓰는 자동 갱신 영역이 아니라, 스토리텔러 에이전트가 이 페이지를 갱신할 때 [질문 백로그](question-backlog.md)와 맞추는 값이다. 기준값은 [트랙 개요](index.md)의 단계 진행 현황 자동 표(상태·열린 질문 수·완료 조건 충족 여부)와 최근 실행 자동 표(마지막 실행)이며, 이 줄과 그 표가 다르면 그 표를 따른다. [가정]

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q1-01 | 로봇 능력·작업을 표현하는 온톨로지·지식 모델에는 무엇이 있고 각각 무엇을 표현하는가? (후보: IEEE 1872 CORA, IEEE 1872.2 자율 로봇 온톨로지, KnowRob·SOMA, PDDL 계열 행동 모델, W3C SSN/SOSA) | 답함 | 사용자 | 2026-09-25-02 | [#q1-01](#q1-01) |
| q1-02 | 산업 상호운용 규격은 로봇 기능을 어떤 형식으로 기술하는가? (후보: VDA 5050의 팩트시트, MassRobotics AMR 상호운용 표준, OPC UA Robotics, Asset Administration Shell의 능력·스킬·서비스 모델, Open-RMF Fleet Adapter의 기능 기술) | 답함 | 사용자 | 2026-09-25-02 | [#q1-02](#q1-02) |
| q1-03 | 이 모델들은 ROP가 배정·실행·검증에 필요로 하는 정보 — 전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미 — 를 얼마나 담는가? 빠진 것은 무엇인가? | 답함 | 사용자 | 2026-09-25-23 | [#q1-03](#q1-03) |
| q1-04 | 능력 기술과 실행 인터페이스(명령·상태)는 기존 표준에서 어떻게 연결되는가? | 답함 | 사용자 | 2026-09-25-16 | [#q1-04](#q1-04) |
| q1-05 | 제조사마다 같은 이름의 기능('운반', '도킹', '리프트')이 다른 의미를 갖는 문제를 기존 모델은 어떻게 다루는가? | 답함 | 사용자 | 2026-09-25-16 | [#q1-05](#q1-05) |
| q1-06 | 부록 A 5번 정의의 요소(제조사별 기능·제약·장착 장비·실행 조건, 작업 요구)를 기준으로 ROP용 능력 개념에 무엇을 더 추가해야 하는가? | 답함 | 사용자 | 2026-09-25-23 | [#q1-06](#q1-06) |
| q1-07 | VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가? | 답함 | f12, 실행 2026-09-25-02 | 2026-09-25-23 | [#q1-07](#q1-07) |
| q1-08 | MassRobotics AMR 상호운용 표준의 setup·status 메시지 스키마에는 로봇 능력(적재량, 지원 작업, 부착 장비)을 기술하는 필드가 있는가? | 답함 | f13, 실행 2026-09-25-02 | 2026-09-25-35 | [#q1-08](#q1-08) |
| q1-09 | ECLASS·IEC CDD 에 이동로봇의 범위 능력(이동·계단·적재·도어 조작·충전)과 그 속성을 기술하는 항목이 있는가, 있으면 능력 온톨로지의 의미 식별자로 쓸 수 있는가? | 열림 | f30, 실행 2026-09-25-16 | | |

표의 질문 문장은 트랙 정의(q1-01~q1-06)와 리서치 브리프(q1-07·q1-08·q1-09) 그대로 두었다. 다음은 구축자 보충이다. q1-06의 "부록 A 5번 정의"에서 5번은 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)를 가리킨다. "부록 A"는 이 위키의 분류 원문(`_source/ROP_SCM_연구분야_분류.md`)을 뜻한다. q1-02의 AMR은 자율이동로봇(Autonomous Mobile Robot, AMR)이다. q1-03은 실행 2026-09-25-16까지 부분 답이었고, 실행 2026-09-25-23에서 학술 온톨로지 행의 원문 대조를 더해 답함으로 처리했다. q1-08은 실행 2026-09-25-35에서 답함으로 처리했다. q1-09는 같은 실행에서 부분 답을 냈으나 ECLASS 데이터베이스·IEC CDD 를 조회하지 못해 질문의 핵심(능력 항목 존재 여부)이 미확인이므로 열림으로 둔다(백로그 상태는 조사 중). 백로그에 q1-09와 같은 질문으로 중복 등록된 q1-10은 실행 2026-09-25-23에서 폐기해 이 표에 두지 않는다.

## 3. 조사 결과

실행 2026-09-25-02는 페이지 열람이 차단된 환경에서 이루어져, 그 실행의 출처는 검색 결과의 기관·제목·URL 일치로만 실재를 확인했다. 실행 2026-09-25-16은 일반 웹 열람이 막힌 대신 공식 GitHub 저장소 원문을 열 수 있어, VDA 5050 명세·상태 스키마·팩트시트 스키마, IDTA 02020·02047 템플릿과 README, MassRobotics 스키마, OPC UA Robotics 노드셋 문서, CaSkMan·SkiROS2 README, Open-RMF 튜토리얼 원본을 원문으로 대조했다. 실행 2026-09-25-23도 같은 환경에서 VDA 5050 공식 저장소 2.1.0 태그와 main 의 팩트시트 스키마, 2.0.0 태그의 명세 마크다운, W3C SSN 시스템 능력 모듈(작업반 편집본), SOMA-ACT 온톨로지 파일, IEEE 1872.2 의 제3자 OWL 구현, IEEE 1872-2015 CORA 의 제3자 OWL 번역, KnowRob README 를 원문으로 열었다. 실행 2026-09-25-35도 같은 환경에서 MassRobotics 공식 JSON 스키마와 IDTA 02047·02020 템플릿을 원문으로 다시 열었고, MassRobotics 표준 설명 페이지와 ECLASS IRDI 설명 페이지는 원문을 열지 못했다. 논문·ISO·KS·IDTA PDF 자료와 능력 매칭 논문 2건은 원문 미열람이며, 네 실행 모두 핵심 주장을 독립 출처로 교차 확인한 것은 없다. 조사 결과를 모은 표는 [모델·표준 비교표](model-standard-comparison.md)에, 반영된 개념 변경은 [능력 온톨로지 초안](ontology-draft.md) v0.3에 있다.

### q1-01 로봇 능력·작업을 표현하는 온톨로지·지식 모델 {#q1-01}

로봇 분야의 공통 어휘로는 IEEE(Institute of Electrical and Electronics Engineers)의 표준 계열이 있다. IEEE 1872-2015는 로봇·자동화 분야의 가장 일반적인 개념·관계·공리를 정한 핵심 온톨로지 CORA(Core Ontology for Robotics and Automation)와 보조 온톨로지 CORAX·POS·RPARTS로 구성되며, 상위 온톨로지 SUMO에 연결된다(2015년 발행). [사실][^ref-025] IEEE 1872.2-2021은 CORA를 확장해 자율 로봇(Autonomous Robotics, AuR)의 설계 패턴·시스템 아키텍처를 표현하는 온톨로지 표준이다(2022년 발행). [사실][^ref-026]

로봇이 작업을 추론하는 데 쓰는 지식 모델도 있다. KnowRob 2.0은 Prolog로 구현된 로봇용 지식 처리 프레임워크로, 논리 표현의 일부를 실시간 센서·운동 데이터와 모션 계획 결과에서 필요할 때 만들어 조작 행동을 추론하게 한다(2018년 논문 기준). [사실][^ref-027] 현재 공식 저장소 dev 브랜치의 README 는 KnowRob 을 RDF·RDFS·OWL 어휘의 맥락화된 트리플로 지식을 표현하고 여러 추론기의 결과를 결합하는 하이브리드 지식 베이스로 설명하며, 저장 백엔드로 Prolog 기반 저장소·MongoDB·Redland 를 들고, 현재 구현은 C++ 이고 Prolog 는 선택 지원이다(확인일 2026-09-25). [사실][^ref-326] 두 서술은 판이 다르다: 2018년 논문의 KnowRob 2.0 은 Prolog 구현이고, 현재 dev 브랜치는 C++ 구현이다. SOMA(Socio-physical Model of Activities)는 DUL 기반으로 일상 활동의 물리·사회적 맥락을 표현하는 로봇용 온톨로지이며, 행동·로봇·어포던스·실행 실패를 다루는 하위 온톨로지를 가진다(2021년 논문 기준). [사실][^ref-028]

행동을 계획 문제로 기술하는 모델로는 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)가 있다. PDDL은 1998년 AIPS-98 계획 경진대회를 위해 McDermott 등이 만든 언어로, 파라미터를 가진 행동을 전제조건(precondition)과 효과(effect)로 기술하고 도메인 기술과 문제 인스턴스를 분리한다. [사실][^ref-029] 센서·액추에이터 쪽에서는 W3C(World Wide Web Consortium)와 OGC(Open Geospatial Consortium)의 공동 표준인 Semantic Sensor Network Ontology(SSN)가 2017-10-19 W3C 권고안으로 발행되었고, 경량 핵심 모듈 SOSA와 확장 모듈 SSN으로 센서·액추에이터·샘플러와 관측·작동·샘플링 활동 및 사용된 절차(procedure)를 표현한다. [사실][^ref-030] SSN의 System Capabilities 모듈은 특정 조건(Condition) 아래의 시스템 성능(SystemCapability), 정상 운용 범위(OperatingRange), 손상 없이 견디는 범위(SurvivalRange)를 표현하는 클래스를 둔다. [사실][^ref-030]

후보 밖에서도 두 자료가 확인됐다. Robotic Capability Ontology(RCO)를 제안한 2025년 논문은 로봇 능력을 제조사가 명시한 광고 능력(advertised capability)과 실제 운용 성능을 반영한 운용 능력(operational capability)으로 구분한다. [사실][^ref-041] 자율 로봇의 신뢰성을 위한 온톨로지 활용을 조사한 2024년 서베이는 조사 대상 온톨로지가 주로 행동의 선택·배열(자율성·계획·행위 개념)과 비상 상황 극복(고장·적응 개념)에 관련된다고 정리한다. [사실][^ref-042]

### q1-02 산업 상호운용 규격의 로봇 기능 기술 형식 {#q1-02}

독일자동차산업협회(Verband der Automobilindustrie, VDA)의 VDA 5050 2.0.0(2022년 1월판) 기준으로, 차량은 팩트시트(factsheet) 토픽으로 자신의 기능(차량 유형, 구동 방식 등)을 상위 관제(master control)에 미리 알린다. [추정][^ref-022] 팩트시트의 블록 구성은 판마다 나눠 적는다. 공식 저장소 2.1.0 태그의 팩트시트 스키마(제목 'AGV Factsheet')는 version·manufacturer·serialNumber 와 유형 명세(typeSpecification), 물리 파라미터(physicalParameters), 프로토콜 한계(protocolLimits), 지원 기능(protocolFeatures), 차량 기하(agvGeometry), 적재 명세(loadSpecification) 블록을 필수로 두고, 버전·네트워크 정보를 담는 vehicleConfig 블록을 둔다(확인일 2026-09-25). [사실][^ref-323] 공식 저장소 main(3.0.0 판)의 팩트시트 스키마는 headerId·timestamp·version·manufacturer·serialNumber 와 typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 블록을 필수로, mobileRobotConfiguration 블록을 선택으로 둔다(확인일 2026-09-25). [사실][^ref-228] 2.0.0 태그의 명세 마크다운(머리말 RELEASE CANDIDATE 표기)은 팩트시트 블록으로 localizationParameters 를 적지만 2.1.0 태그와 main 스키마에서는 이 블록이 확인되지 않아, 2.0.0 게시판의 블록 구성은 확정할 수 없는 것으로 보인다. [추정][^ref-329][^ref-323][^ref-228] 실행 2026-09-25-16에서는 공식 저장소 main 브랜치의 팩트시트 스키마를 원문으로 열어 적재 명세와 지원 action 정의 블록을 확인했다(내용은 q1-03 답). [사실][^ref-228] 2.0.0 기준 상태 메시지는 오류를 유형(errorType)·등급(errorLevel: WARNING 또는 FATAL)·설명·참조로 보고하고, action 완료는 actionStatus 가 finished 로 바뀐 상태 메시지로 알린다. [사실][^ref-022]

VDA 5050은 3.0.0판이 2026년에 발행되어(3.0.0 발행 2026-03, 보도자료 2026-04) 자율도 높은 이동로봇 통합을 위해 인터페이스를 확장했다. [사실][^ref-032] 확장 내용으로 구역(zone) 개념, 경로 공유, 새 오류 등급 CRITICAL·URGENT, 절전 모드 action 추가와 기존 궤적·회랑 방식 유지가 거론되지만, 이 목록은 검색 요약 기준이며 원문 미열람이다. [추정][^ref-032] 이 가운데 오류 등급은 공식 저장소 main 브랜치의 상태 스키마 원문으로 확인했다: 3.0.0의 오류 등급은 WARNING·URGENT·CRITICAL·FATAL 넷이다(확인일 2026-09-25). [사실][^ref-051] 팩트시트 필드의 2.x 대비 변화는 q1-07 답에 있다(2.x 기준은 2.1.0 태그). 그 밖의 2.0.0 기준 서술이 3.0.0에서 어떻게 바뀌었는지는 미확인이다.

MassRobotics AMR 상호운용 표준 1.0(2021년 5월)은 식별·설정(setup) 메시지와 상태(status) 메시지 두 가지로 제조사·모델, 위치·속도·방향, 상태(health), 작업·가용 상태를 공유하게 한다. [사실][^ref-033] OPC UA(Open Platform Communications Unified Architecture) for Robotics Part 1: Vertical Integration(OPC 40010-1, 판·발행일 미확인)은 VDMA(Verband Deutscher Maschinen- und Anlagenbau)와 OPC Foundation이 만든 동반 규격으로, 모션 장치 시스템(컨트롤러 1대와 모션 장치 1..n대)의 자산 관리·상태 감시 데이터를 상위 시스템(공장 제어·제조 실행 시스템(Manufacturing Execution System, MES)·클라우드)에 제공하는 정보 모델을 정의한다. [사실][^ref-034]

Plattform Industrie 4.0의 능력·스킬·서비스(Capabilities, Skills and Services, CSS) 정보 모델 토론 문서(2022년 11월)는 능력(capability)을 구현과 무관한 기능 명세로, 스킬(skill)을 그 능력의 실행 가능한 구현으로 구분하고 서비스(service)와의 관계를 정한다. [사실][^ref-035][^ref-036] 이 위키의 [능력 온톨로지 초안](ontology-draft.md)에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다. 자산 관리 셸(Asset Administration Shell, AAS) 쪽에서는 IDTA 02020 Capability Description 1.0 서브모델의 공식 템플릿이 CapabilitySet → CapabilityContainer 아래에 Capability(한정자 Required·Offered·NotAssigned), 속성 묶음(PropertySet), 능력 관계(CapabilityRealizedBy, ComposedOfSet, GeneralizedBySet), 제약 묶음(ConstraintSet)을 두고 요소마다 의미 식별자(semanticId)를 붙인다(확인일 2026-09-25). [사실][^ref-243] 이전 실행이 인용한 제3자 논문은 같은 서브모델의 제약을 ConditionContainer로, 속성과 스킬 파라미터를 잇는 관계를 realizedBy로 적었다. [추정][^ref-037] 이 표기는 제3자 논문 표기이며 1.0 템플릿에서 확인되지 않는다 — 판 차이 여부 미확인. Vieira da Silva·Köcher·Fay(2022)는 제조 분야의 능력·스킬 모델을 이종 자율 로봇 팀에 적용·확장하고, AAS 서브모델과 능력·스킬 온톨로지 사이의 양방향 매핑 개념을 제시했다. [사실][^ref-038] 국내에서는 신민종·한영석·정재윤의 논문 「자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계」가 한국전자거래학회지 29권 4호 203-213쪽(2024)에 게재되었다(논문 본문 내용은 미확인). [사실][^ref-043]

Open-RMF는 청소(Clean)·배송(Delivery)·순회(Loop) 작업 유형을 지원하며, 플릿 어댑터 설정의 작업 능력(task capabilities) 항목으로 플릿이 수행할 수 있는 작업 유형을 선언한다(확인일 2026-09-25). [사실][^ref-039] 플릿 어댑터는 설정 파일에 수행 가능한 사용자 정의 동작(performable actions) 목록을 둘 수 있고, 해당 동작이 배정되면 execute_action 콜백이 호출되며 RMF는 완료 신호를 받을 때까지 로봇 제어를 어댑터에 넘긴다(확인일 2026-09-25). [사실][^ref-040]

### q1-03 ROP가 필요로 하는 다섯 정보의 담김 정도 {#q1-03}

원문을 연 산업 규격·서브모델·오픈소스와 학술 온톨로지 기준으로 다섯 정보 항목은 여러 모델에 흩어져 담기며, 다섯을 한 모델이 모두 담는 경우는 확인되지 않았다. [추정][^ref-228][^ref-243][^ref-051][^ref-324][^ref-235] 실행 2026-09-25-16은 산업 규격·서브모델·오픈소스를 항목별로 대조했고, 실행 2026-09-25-23은 남은 학술 온톨로지 행(IEEE 1872 CORA, IEEE 1872.2, KnowRob·SOMA, SSN/SOSA)을 공개 저장소 원문으로 대조해 이 질문을 답함으로 처리했다. 다만 KnowRob 은 README 범위에서 판정할 수 없고, PDDL 행은 검색 요약 수준이다.

**적재·환경 제약.** VDA 5050 공식 저장소 main 브랜치의 팩트시트 스키마는 적재 명세(loadSpecification)를 적재 위치 목록(loadPositions)과 적재 세트(loadSets)로 두고, 적재 세트마다 적재 유형, 적재 치수(길이·너비·높이), 최대 중량, 적재 취급 높이·깊이·기울기의 최소·최대, 적재 시 최대 속도·가감속, 적재·하역 소요 시간(pickTime·dropTime)을 기술하게 한다(확인일 2026-09-25). [사실][^ref-228] IDTA 02047 무인운반차(Automated Guided Vehicle, AGV) 기술 데이터 1.0 템플릿은 최대 적재 질량, 적재·무적재 시 최대 등판·측경사 각, 최대 속도와 가동 시간의 명세값(AsSpecified)과 운용값(AsOperated), 위치추정·정위치 정확도, 실외 사용 적합 여부와 요구 환경 조건, 부착 장비 인터페이스를 속성으로 둔다(확인일 2026-09-25). [사실][^ref-245] MassRobotics AMR 상호운용 표준의 공식 JSON 스키마는 식별 보고(identityReport)에 최대 속도·예상 가동 시간·충전기 유형·화물 최대 부피·화물 최대 중량(kg)과 자유 서술 화물 유형(cargoType)을, 상태 보고(statusReport)에 운용 상태 9종·배터리 비율·남은 적재 여유 비율·문자열 오류 코드 배열을 둔다(확인일 2026-09-25). [사실][^ref-230]

**파라미터 범위.** 같은 팩트시트 스키마는 지원 action 목록(mobileRobotActions)에 action 유형·설명, 적용 범위(INSTANT·NODE·EDGE·ZONE), 파라미터(키·데이터형·설명·선택 여부), 결과 설명, 차단 유형(NONE·SOFT·SINGLE·HARD), 일시정지·취소 허용 여부를 둔다. [사실][^ref-228] 이번에 연 스키마에서 action 파라미터는 데이터형만 두고 허용 값 범위를 두지 않으며, 전제조건이나 오류 의미를 기술하는 블록은 확인되지 않았다(스키마 전체를 글자 단위로 대조하지 않아 부재의 확정은 아니다). [추정][^ref-228] IDTA 02020 템플릿은 속성 묶음(PropertySet) 안에 속성(Property)과 범위(Range) 요소를 둔다. [사실][^ref-243]

**전제조건.** IDTA 02020 능력 기술 1.0 서브모델은 능력을 물리·가상 세계에 효과를 내는 기능의 구현 독립 명세로 정의하고, 속성(최대 속도·공차·온도 범위 등)과 두 종류의 제약 — 속성 제약(전제조건·불변조건·사후조건)과 능력 사이 순서·병행을 정하는 전이 제약 — 을 두며, 능력은 스킬로 구현된다고 설명한다. [사실][^ref-229][^ref-243] SkiROS2는 스킬을 행동 트리로 조합하는 ROS 기반 플랫폼으로, 스킬마다 실행 전 전제조건·실행 중 유지조건·실행 후 사후조건을 두고, 의미 데이터베이스 형태의 세계 모델로 스킬 파라미터를 자동 추론한다. [사실][^ref-250] SkiROS2는 로봇 내부의 실행 플랫폼이어서 분류 원문 9장의 로봇 자체 지능·제어 쪽 연계 대상이므로, 여기서는 스킬 조건을 표현하는 사례로만 쓴다.

**완료 확인 방법.** VDA 5050 3.0.0 명세는 사전 정의 action pick·drop 에 적재 장치(lhd)·스테이션 유형·스테이션 이름·적재 유형·적재 id·높이·깊이·측면을 선택 파라미터로 두고, 완료(FINISHED)를 적재물이 로봇에 들어왔거나(pick) 로봇을 떠났고(drop) 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] 이전 실행(2026-09-25-02)은 능력 기술 안에 완료 확인 방법을 명시하는 항목이 확인되지 않았다고 적었으나 이는 검색 범위에서의 추정이었고, 원문 대조 결과 VDA 5050 3.0.0의 pick·drop 완료 정의, IDTA 02020의 사후조건, SkiROS2의 사후조건이 완료 확인에 쓰일 수 있는 항목으로 보인다. [추정][^ref-031][^ref-229][^ref-250]

**오류의 의미.** VDA 5050 공식 저장소 main 의 상태 스키마는 오류 등급을 WARNING(계속 가능, 즉시 조치 불필요)·URGENT(계속 가능, 즉시 조치 필요)·CRITICAL(현재 주문 계속 불가)·FATAL(새 주문 수락 불가, 사용자 개입 필요) 넷으로 두고, 오류에 설명(errorDescription)·해결 힌트(errorHint)와 번역을, action 상태에 WAITING·INITIALIZING·RUNNING·RETRIABLE·PAUSED·FINISHED·FAILED 를 둔다(확인일 2026-09-25). [사실][^ref-051] 오류 복구 절차를 구조화한 모델은 RETRIABLE 상태와 자유 서술 해결 힌트 외에는 확인하지 못했다. [추정][^ref-051]

**다른 후보.** OPC UA for Robotics 공식 노드셋 문서는 모션 장치 시스템·컨트롤러·모션 장치·축·동력 전달계·부하·안전 상태(비상정지·보호정지) 유형과, 프로그램을 이름·노드로 적재하고 시작·정지하는 작업 제어와 운영 상태 기계를 정의하며, 목록에서 능력·스킬 유형은 확인되지 않았다(노드셋 판 표기 v100, 명세 본문 아님). [사실][^ref-244] 이 규격의 모션 장치·축·안전 정지 유형은 로봇 제어 쪽이므로 능력 기술이 있는지를 판단하는 데만 썼다. Open-RMF 문서는 플릿이 수행할 수 있는 사용자 정의 동작을 설정 파일의 actions 목록으로 선언하고, 작업 요청의 category(동작 이름)와 description(동작별 내용)을 어댑터의 execute_action 이 받아 처리한 뒤 execution.finished() 로 완료를 알리게 하며, 파라미터 스키마·전제조건·구조화된 실패 보고는 설명하지 않는다(확인일 2026-09-25). [사실][^ref-040] PDDL 행은 여전히 검색 요약 기준의 추정이다: 전제조건·효과는 PDDL이 담는 것으로 보인다. [추정][^ref-029]

**학술 온톨로지 행(실행 2026-09-25-23).** W3C SSN 의 System Capabilities 모듈(ssn-system.ttl, 작업반 편집본)은 조건 아래 시스템 성질을 기술하는 SystemCapability·OperatingRange·SurvivalRange·Condition 클래스와, 하위 성질 MeasurementRange·ActuationRange·Accuracy·Latency·ResponseTime 등, 운용 성질 MaintenanceSchedule·OperatingPowerRange, 생존 성질 SystemLifetime·BatteryLifetime 을 두고 hasSystemCapability·hasOperatingRange·inCondition 속성으로 잇는다(확인일 2026-09-25, /TR 판과 문구 차이 가능). [사실][^ref-235] 이 모듈은 다섯 항목 가운데 파라미터 범위(ActuationRange·조건 아래 성능)와 환경 제약(Condition·OperatingRange·SurvivalRange)을 담지만, 열람 범위에서 전제조건·완료 확인 방법·오류 의미·적재 제약을 기술하는 클래스는 확인되지 않았다(SOSA 핵심 모듈은 열지 않아 부재 확정이 아니다). [추정][^ref-235]

SOMA 공식 저장소의 SOMA-ACT 온톨로지는 작업 실행 상태 영역(ExecutionStateRegion)에 Active·Cancelled·Failed·Paused·Pending·Succeeded 여섯 상태를 두고, 전제 상황(hasRequiredInitialSituation)과 기대 종료 상황(hasExpectedTerminalSituation) 관계, 충족되지 않은 사후조건 같은 기대 불일치를 나타내는 NonmanifestedSituation 클래스를 둔다(확인일 2026-09-25). [사실][^ref-324] 따라서 SOMA 는 전제조건(요구 초기 상황), 완료 확인(기대 종료 상황과 Succeeded 상태), 오류 의미(Failed 상태와 기대 불일치 상황)를 담지만, 이번에 연 SOMA-ACT 파일에서 파라미터 허용 범위와 적재 제약은 확인되지 않았다(다른 모듈은 열지 않아 부재 확정이 아니다). [추정][^ref-324]

헬무트 슈미트 대학이 공개한 IEEE 1872.2 AuR 온톨로지 OWL 구현은 기능(Function)·기능 실행(FunctionExecution), 행동 분류(ArchitecturalBehavior·ManifestedBehavior·EmergentBehavior 등), 물리·정보 상호작용, 객체 중심 환경 기술 클래스를 두고 기능을 행동에 잇는 isPlayedBy 속성을 둔다. [사실][^ref-325] 이 파일은 제3자 OWL 구현이며 IEEE 표준 본문이 아니다. 이 구현에서는 능력·전제조건·사후조건·파라미터 범위·실패·작업 완료 상태를 명시하는 클래스·속성이 확인되지 않아, 다섯 정보 항목을 구조로 담지 않는 것으로 보인다(열람 파일 기준, 부재 확정 아님). [추정][^ref-325]

IEEE 1872-2015 CORA 의 공개 OWL 번역(cora-bare.owl, 제3자 수작업 번역이며 IEEE 표준 본문이 아님)은 Robot·RobotGroup·RobotInterface·RoboticEnvironment·RoboticSystem·SingleRoboticSystem·CollectiveRoboticSystem 클래스와, 부품 관계(robotPart), 로봇 환경이 로봇 시스템을 갖춘다는 관계(equippedWith), 자율성 수준(자율·반자율·원격 조종·원격 조작) 속성을 둔다. [사실][^ref-330] CORA 는 로봇·로봇 시스템의 분류, 부품 관계(robotPart)와 로봇 환경이 로봇 시스템을 갖춘다는 관계(equippedWith)를 표현할 뿐 다섯 정보 항목과 능력·작업 개념은 담지 않는 것으로 보인다(열람 파일 기준, 부재 확정 아님). [추정][^ref-330]

KnowRob README 는 전제조건·파라미터 범위·실패 같은 항목을 직접 다루지 않아, KnowRob 행의 다섯 정보 항목은 README 만으로 판정할 수 없고 KnowRob 이 쓰는 도메인 온톨로지(SOMA 등) 쪽 판정에 기대야 할 것으로 보인다. [추정][^ref-326][^ref-324]

**종합.** 원문을 연 모델 기준으로 전제조건은 IDTA 02020 속성 제약·SkiROS2 스킬 조건·SOMA 요구 초기 상황이, 파라미터 범위는 IDTA 02020 Range 속성과 SSN 시스템 능력이(VDA 5050 팩트시트는 데이터형만), 적재·환경 제약은 VDA 5050 적재 세트·IDTA 02047·MassRobotics 화물 최대값과 SSN 운용 조건이, 완료 확인은 VDA 5050 pick·drop 완료 정의·IDTA 02020 사후조건·SkiROS2 사후조건·SOMA 기대 종료 상황이, 오류 의미는 VDA 5050 오류 등급·힌트와 SOMA 실패 상태가 담으며, 다섯을 한 모델이 모두 담는 경우는 확인되지 않았다. [추정][^ref-228][^ref-031][^ref-051][^ref-243][^ref-245][^ref-230][^ref-250][^ref-324][^ref-235] 원문을 연 학술 온톨로지 기준으로 전제조건·완료 확인·오류 의미는 SOMA 가, 파라미터 범위·환경 제약은 SSN System Capabilities 가 일부 담고, CORA·IEEE 1872.2 구현은 다섯 항목을 담지 않으며, 적재 제약은 어떤 학술 온톨로지에서도 확인되지 않고 VDA 5050 적재 세트 같은 산업 규격에만 있어, ROP 는 적재 제약과 오류의 조치 의미(등급·재시도)를 산업 규격 쪽에서 가져와야 할 것으로 보인다. [추정][^ref-324][^ref-235][^ref-330][^ref-325][^ref-228] 이 판정 범위는 원문을 연 파일로 한정되며 PDDL·KnowRob 자체는 포함하지 않는다. IDTA 02047 이 속도·가동 시간을 명세값과 운용값으로 나눠 두는 것은 RCO가 구분한 광고 능력과 운용 능력에 대응하는 표현으로 보인다(IDTA 문서가 두 값의 정의를 어떻게 적는지는 미확인). [추정][^ref-245][^ref-041]

**분류 원문 질문에 대한 시사점.** 이 단계의 중심 영역은 다음 질문을 묻는다.

> 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]

Electronics(2026-08-11 게재) 연구는 이종 다중 로봇 작업 배정에서 수행 가능성 판단이 기존에는 특정 최적화기·계획기 안에 묻혀 있고 공간 통행 가능성이 적재 상태에 따른 변화를 반영하지 못한다고 지적하고, 로봇·작업·장소의 의미 모델과 선언적·절차적 혼합 추론으로 다축 능력 조건과 적재 상태별 장소 도달 가능성을 판정하는 방법을 제안했다. [사실][^ref-236] 이 질문에 답하려면 화물의 치수·중량·적재 높이를 로봇의 적재 명세(VDA 5050 적재 세트, MassRobotics 화물 최대값, IDTA 02047 최대 적재 질량)와 대조하고 적재 상태에서의 경로·장소 도달 가능성까지 판정해야 할 것으로 보이며, 어느 표준도 이 대조 규칙 자체는 정하지 않는다. [추정][^ref-228][^ref-230][^ref-245][^ref-236] 화물 쪽 속성은 [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)의 식별·적재 관계에서 와야 한다.

단계 1의 시사점으로, 매뉴얼에서 가져온 능력 정보는 RCO의 구분으로는 제조사가 명시한 광고 능력에 해당하므로, ROP가 배정에 쓰려면 현장 운용 성능(운용 능력)으로 보완·검증하는 절차가 필요할 것으로 보인다. [추정][^ref-041] 이 추정은 트랙 가설 1의 판정 근거로 쓰지 않는다.

### q1-04 능력 기술과 실행 인터페이스(명령·상태)의 연결 {#q1-04}

확인한 표준에서 능력 기술과 실행 인터페이스는 같은 프로토콜 안에서 이름으로 맞물리거나, 능력–스킬–스킬 인터페이스를 모델 안에서 잇거나, 아예 연결이 없는 세 방식으로 나뉘는 것으로 보인다. [추정][^ref-228][^ref-036][^ref-230] 아래는 방식별 근거다.

**같은 프로토콜 안에서 이름으로 맞물리는 방식.** VDA 5050 3.0.0 명세는 로봇의 능력을 팩트시트 토픽으로 관제에 알리게 하고(지원 구역 이름은 팩트시트 유형 명세의 supportedZones 에 추가), 사전 정의 action 으로 옮길 수 없는 동작은 제조사가 추가 action 을 정의해 관제가 쓰도록 한다. [사실][^ref-031] VDA 5050에서 능력 기술과 명령의 연결은 팩트시트의 action 정의(action 유형·파라미터 키·적용 범위·차단 유형)와 주문·즉시 action 의 action 유형·파라미터가 같은 이름으로 맞물리는 방식이며, 관제가 보내기 전에 팩트시트로 검증해야 한다는 규정은 이번 열람 범위에서 확인되지 않았다. [추정][^ref-228][^ref-031] Open-RMF 에서는 설정에 선언한 동작 이름을 작업 요청의 category 로 받아 어댑터의 execute_action 이 처리하고 execution.finished() 로 완료를 알린다. [사실][^ref-040]

**능력–스킬–스킬 인터페이스를 모델 안에서 잇는 방식.** Plattform Industrie 4.0 작업반의 능력·스킬 참조 모델(Köcher 외, 2022년 arXiv, 저널판 Automatisierungstechnik 71(2), 2023)은 스킬을 능력이 명세한 기능의 실행 가능한 구현으로 정의하고, 모든 스킬이 조화된 상태 기계를 따르고 그 상태 기계를 스킬 인터페이스로 노출해 현재 상태 감시와 전이 호출을 하게 하며, OPC UA 구현에서는 SkillType 객체가 실현하는 능력을 ontologyURL 로 가리킨다. [사실][^ref-036] CaSkMan 온톨로지는 기계가 능력을 제공하고(providesCapability) 능력이 스킬로 실현되며(isRealizedBy) 스킬이 ISA 88 상태 기계와 REST 또는 OPC UA 스킬 인터페이스로 실행되는 구조를 둔다(제조 기계 대상이며 README 에 이동로봇 사례는 없다). [사실][^ref-231] Sidorenko 외(Procedia Manufacturing 55, 2021)는 스킬을 유한 상태 기계로 모델링해 OPC UA 로 노출하고, I4.0 언어의 스킬 실행 상호작용 프로토콜 메시지와 상호작용 상태 기계를 자산 관리 셸에 표현하는 방법을 제시했다. [사실][^ref-246]

**연결이 없는 방식.** IDTA 02020 1.0 은 능력과 스킬 구현 사이를 CapabilityRealizedBy 관계 요소로만 잇고, README 는 스킬의 실행 인터페이스(명령·상태)를 이 서브모델에서 정하지 않는다. [사실][^ref-243][^ref-229] MassRobotics AMR 상호운용 표준의 공식 JSON 스키마는 식별 보고와 상태 보고 두 메시지 유형만 정의해, 로봇에 명령을 보내는 메시지를 두지 않는다. [사실][^ref-230] OPC UA for Robotics 노드셋 문서의 작업 제어는 프로그램 단위의 적재·시작·정지에 머물고 능력·스킬 유형은 목록에서 확인되지 않았다. [사실][^ref-244]

서비스 로봇 쪽에서는 ISO 22166-202:2025 가 서비스 로봇 소프트웨어 모듈의 정보 모델 요구사항을 정하며, 설계·개발과 실행 시점에 쓰이는 인터페이스·속성·구성·실행 관련 정보를 구조화해 기술하게 한다(2025년 발행, 이 질문의 보조 근거). [사실][^ref-248] 한국산업표준 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 국가표준 목록에 있으며, ISO 22166-202 와 같은 주제를 다루는 대응 표준으로 보인다(부합화 여부·제정일 미확인). [추정][^ref-138][^ref-248]

위 세 방식 — (1) VDA 5050 팩트시트–주문 action, Open-RMF 선언 동작–execute_action 처럼 같은 프로토콜 안에서 이름으로 맞물리는 방식, (2) CSS 참조 모델·CaSkMan·AAS 스킬 실행 프로토콜처럼 능력–스킬–스킬 인터페이스(상태 기계, OPC UA·REST)를 모델 안에서 잇는 방식, (3) 보고 전용 MassRobotics, 프로그램 단위 제어만 있는 OPC UA Robotics, 관계만 둔 IDTA 02020 처럼 연결이 없는 방식 — 은 이 위키가 묶은 분류이며, 이 분류를 제시한 단일 출처는 확인하지 못했다. 이 분류로 보면 ROP는 능력 온톨로지와 제조사 프로토콜의 action 이름·파라미터를 잇는 매핑 계층을 따로 가져야 할 것으로 보인다. [추정][^ref-228][^ref-031][^ref-040][^ref-036][^ref-231][^ref-246][^ref-230][^ref-244][^ref-243] 이동로봇 표준(VDA 5050)과 CSS 스킬 상태 기계를 잇는 공개 매핑은 찾지 못했다(후속 질문 q4-09).

### q1-05 같은 이름 기능의 제조사별 의미 차이 {#q1-05}

같은 이름 기능의 의미 차이를 기존 모델은 공통 참조 어휘, 표준이 고정한 사전 정의 동작, 속성 단위의 외부 사전 식별자, 분류 체계·일반화 관계로 다루는 것으로 보이나, 두 제조사의 '도킹'·'리프트'가 실제로 같은 동작인지를 판정하는 방법은 확인되지 않았다. [추정][^ref-025][^ref-031][^ref-247][^ref-243] 아래는 방식별 근거다.

**공통 참조 어휘.** IEEE 1872-2015 는 로봇·자동화 분야의 지식 표현·추론과 로봇–사람 사이 소통의 공식 참조 어휘로 쓰이도록, 개념을 더 정확히 정의하고 공동체의 공통 이해를 높이며 로봇 시스템 사이 데이터 통합과 정보 전달을 돕는 것을 목적으로 한다. [사실][^ref-025] RCO 논문(Naqvi 외, 2025) 저자는 참조 능력 온톨로지가 표준 어휘와 추론 규칙을 제공해 서로 다른 제조사·구성의 로봇을 같은 기준으로 비교할 수 있게 한다고 주장한다. [의견][^ref-041]

**표준이 고정한 동작과 제조사 확장의 분리.** VDA 5050 3.0.0 명세는 사전 정의 action 29종(startPause, startCharging, stopCharging, initializePosition, pick, drop, detectObject, finePositioning, waitForTrigger, cancelOrder, factsheetRequest 등)의 이름·파라미터·상태별 의미를 표로 고정하고 쓸 수 있으면 정의된 파라미터를 쓰도록 하며, 이 목록에 dock·lift 라는 이름의 action 은 없다. [사실][^ref-031] 목록 밖 동작은 q1-04 에 적은 제조사 정의 action 으로 들어간다.

**속성 단위의 외부 사전 식별자.** IDTA 의 AAS 명세 Part 3a 는 IEC 61360 데이터 명세를 두어, 속성의 의미를 ECLASS·IEC 공통 데이터 사전(CDD) 같은 IEC 61360 기반 사전의 개념 기술을 가리키는 의미 식별자로 정하게 한다(인용한 판은 IDTA-01003-a 3.0.2, 2024-07이며 최신판 3.1.1 이 있다). [사실][^ref-247] IDTA 02047 템플릿은 제조사명(0173-1#02-AAO677)·최대 적재 질량(0173-1#02-ABJ258) 같은 일부 속성에 ECLASS IRDI 를 붙이고, 속도 속성에는 IDTA 자체 식별자를 쓴다. [추정][^ref-245] 이 고정은 능력(기능) 단위가 아니라 속성 단위다.

**분류 체계·일반화 관계·구성 요소 기반 추론.** IDTA 02020 템플릿은 능력 사이에 일반화(CapabilityGeneralizedBy, 구체 능력→일반 능력)·구성(CapabilityComposedOf) 관계와 속성 사이 동일성(SameProperty) 관계를 둔다. [사실][^ref-243] 이 관계로 제조사별 구체 능력을 공통 상위 능력에 연결할 수 있을 것으로 보인다. [추정][^ref-243] CaSkMan 은 능력 분류에 VDI 2860(핸들링)·DIN 8580(제조 공정) 분류 체계와 VDI 3682 공정 모델을 쓴다. [사실][^ref-231] Dussard 외(2023)는 로봇의 구성 요소와 저수준 능력으로부터 에이전트의 능력을 추론하는 온톨로지 방법을 제안했다. [사실][^ref-249]

**자유 이름·자유 서술에 맡기는 경우.** MassRobotics 식별 보고의 화물 유형은 자유 서술 필드다. [사실][^ref-230] Open-RMF 의 사용자 정의 동작은 플릿 설정에 선언한 자유 문자열 이름이고 그 의미는 어댑터 코드의 분기 구현이 정하므로, 서로 다른 플릿이 같은 이름('clean', 'dock' 등)으로 다른 동작을 수행할 수 있을 것으로 보인다. [추정][^ref-040]

정리하면 (1) 공통 참조 어휘·상위 온톨로지(IEEE 1872, RCO), (2) 표준이 이름·파라미터·완료 의미를 고정한 사전 정의 동작과 제조사 확장의 분리(VDA 5050), (3) 속성 단위의 외부 사전 식별자(AAS 의미 식별자, ECLASS·IEC CDD), (4) 분류 체계·일반화 관계·구성 요소 기반 추론(IDTA 02020, CaSkMan, Dussard 외)이 확인되며, MassRobotics·Open-RMF 는 자유 서술·자유 이름에 맡긴다. 이 네 방식은 이 위키가 묶은 분류다. [추정][^ref-025][^ref-041][^ref-031][^ref-247][^ref-245][^ref-243][^ref-231][^ref-249][^ref-230][^ref-040] 두 제조사의 사용자 정의 동작이 같은 동작인지 판정하는 시험 절차는 후속 질문 q5-07 로 보냈다.

### q1-06 ROP용 능력 개념에 더할 것 {#q1-06}

분류 원문 5. 로봇 능력·작업 온톨로지의 정의 요소(제조사별 기능·제약·장착 장비·실행 조건, 작업 요구)를 기준으로 보면, 기능을 요구 쪽과 제공 쪽으로 나눠 속성 단위로 비교하는 표현이 먼저 필요한 것으로 보인다. [추정][^ref-229][^ref-327][^ref-228] 아래는 근거와 요구 목록 초안이다.

**요구 능력과 제공 능력의 비교.** IDTA 02020 능력 기술 1.0 README 는 이 서브모델이 공정·제품 쪽 요구 능력과 자원 쪽 제공 능력을 비교해 생산 계획·오케스트레이션을 돕는다고 설명한다. [사실][^ref-229] Järvenpää 외(IJCIM 36(1), 2023, 온라인 2022-06-07)는 제품과 자원의 온톨로지 기술과 SPIN 규칙으로 결합 자원의 결합 능력 파라미터를 추론하고 제품 특성을 자원(조합)의 능력 파라미터와 비교해 가능한 자원 조합을 찾는, 능력 매칭을 위한 의미 규칙(SPIN)을 제시했다. [사실][^ref-327] Köcher·Vieira da Silva·Fay(arXiv 2312.08801, 2023-12, AAAI 2024 CAIPI 워크숍)는 의미 능력 모델과 SMT 로 제품 생산이나 자율 로봇 임무 수행에 필요한 개별 능력의 순서를 자동으로 찾는 공정 계획 방법을 제안했다. [사실][^ref-328] 두 논문은 제조 공정 계획 연구이므로 물류 현장 적용 사례가 아니라 방법의 선례로만 쓴다.

**장착 장비·구성·운용 조건의 선언.** VDA 5050 main(3.0.0) 팩트시트는 적재 취급 장치 식별자 목록(loadPositions), 위치추정·주행 방식(localizationTypes·navigationTypes), 지원 구역 유형(supportedZones), 하드웨어·소프트웨어 버전 키-값(mobileRobotConfiguration.versions), 충전 설정(batteryCharging)을 기술하게 해, 장착 장비·운용 구역·버전·충전 조건을 로봇 선언의 일부로 둔다. [사실][^ref-228] IDTA 02047 무인운반차 기술 데이터 1.0 템플릿은 부착 장비 인터페이스(InterfacesForAttachments)와 속도·가동 시간의 명세값(AsSpecified)·운용값(AsOperated) 쌍을 속성으로 둔다(실행 2026-09-25-16 원문 확인의 재인용). [사실][^ref-245]

**요구 목록 초안.** 정의 요소를 기준으로 온톨로지 초안에 더할 ROP용 능력 개념 요구 후보는 (1) 기능의 요구·제공 구분과 속성 단위 비교, (2) 기능 속성의 값·범위, (3) 전제·사후조건, (4) 실행 상태, (5) 로봇의 하드웨어·소프트웨어 구성 버전, (6) 장착 장비의 부착 인터페이스·적재 취급 장치 위치, (7) 운용 구역·환경 조건, (8) 충전 조건, (9) 결합 자원의 결합 능력인 것으로 보인다. [추정][^ref-229][^ref-327][^ref-324][^ref-235][^ref-228][^ref-245][^ref-330] 이 목록은 이 위키의 종합이며 이 목록을 제시한 단일 출처는 없다. 내용 검증 에이전트가 승인한 것은 (1)·(4)·(6)이며 [능력 온톨로지 초안](ontology-draft.md) v0.3에 반영됐다. (5)·(7)·(8)은 초안 6절 질문으로 두었고, (2)·(3)·(9)는 이번에 변경 제안이 없다. 항목별 반영 상태는 초안 6절의 요구 목록 표에 있다.

**분류 원문 질문과의 연결.** 분류 원문의 질문(같은 운반 로봇 중 누가 이 화물을 실제로 취급할 수 있는가)에 답하려면 작업 요구를 화물 치수·중량 같은 요구 능력 속성으로 표현하고 로봇의 적재 세트 같은 제공 능력 속성과 비교하는 규칙이 필요할 것으로 보이며, 제조 분야의 능력 매칭 연구가 이 비교를 의미 규칙으로 구현한 선례가 된다. [추정][^ref-229][^ref-327][^ref-228][^ref-236] 물류 이동로봇 대상의 능력 매칭 규칙은 찾지 못했고, 비교 규칙의 질의 형식은 단계 4 질문 q4-07 에서 다룬다.

### q1-07 VDA 5050 팩트시트의 2.x 대비 3.0.0 필드 변화와 적재 제약 필드 {#q1-07}

이 답의 '2.x'는 VDA 5050 공식 저장소 2.1.0 태그의 팩트시트 스키마 기준이다. 2.0.0 태그에는 팩트시트 JSON 스키마가 없고(해당 경로가 열리지 않음) 2.0.0 태그의 명세는 RELEASE CANDIDATE 표기 문서여서, 2.0.0 게시판과 필드 단위로 대조하지 못했다. 3.0.0 은 공식 저장소 main 의 스키마 기준이다.

**블록 구성.** 2.1.0 태그 스키마는 version·manufacturer·serialNumber 와 typeSpecification·physicalParameters·protocolLimits·protocolFeatures·agvGeometry·loadSpecification 블록을 필수로 두고 vehicleConfig 블록을 둔다. [사실][^ref-323] main(3.0.0) 스키마는 headerId·timestamp·version·manufacturer·serialNumber 와 typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification 블록을 필수로, mobileRobotConfiguration 블록을 선택으로 둔다. [사실][^ref-228] 2.0.0 태그 명세가 적는 localizationParameters 블록은 2.1.0 태그와 main 스키마에서 확인되지 않아, 2.0.0 게시판의 블록 구성은 확정할 수 없는 것으로 보인다. [추정][^ref-329][^ref-323][^ref-228]

**확인된 이름 변경.** 두 스키마를 대조하면 agvGeometry→mobileRobotGeometry, vehicleConfig→mobileRobotConfiguration, agvActions→mobileRobotActions, resultDescription→actionResult, agvKinematic·agvClass·maxLoadMass→mobileRobotKinematics·mobileRobotClass·maximumLoadMass, speedMin·speedMax·accelerationMax·decelerationMax·heightMin·heightMax→minimumSpeed·maximumSpeed·maximumAcceleration·maximumDeceleration·minimumHeight·maximumHeight 로 이름이 바뀌었다. [사실][^ref-323][^ref-228] 이 목록은 확인된 변화이며 완결 목록이 아니다.

**확인된 추가 필드.** main(3.0.0) 스키마는 2.1.0 태그 스키마에 없던 action 적용 범위 ZONE, action 필수 필드 pauseAllowed·cancelAllowed, 유형 명세의 supportedZones, 구성 블록의 batteryCharging(임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간)을 더했고, 지원·필수 선택 파라미터 목록(optionalParameters: parameter·support SUPPORTED/REQUIRED·description)은 두 판 모두 둔다. [사실][^ref-323][^ref-228]

**적재 제약 필드.** 적재 제약은 두 판 모두 적재 명세(loadSpecification)의 적재 세트(loadSets)에 기술되며, 2.1.0 태그는 maxWeight, min/maxLoadhandlingHeight·Depth·Tilt, agvSpeedLimit·agvAccelerationLimit·agvDecelerationLimit, pickTime·dropTime 을, main(3.0.0)은 maximumWeight, minimum/maximumLoadhandlingHeight·Depth·Tilt, maximumSpeed·maximumAcceleration·maximumDeceleration, pickTime·dropTime 을 두고, 로봇 전체 최대 적재 질량은 유형 명세(maxLoadMass→maximumLoadMass)에 둔다. [사실][^ref-323][^ref-228] 2.1.0 태그 기준의 2.x 와 3.0.0 의 적재 제약은 적재 세트 단위(치수·최대 중량·취급 높이·깊이·기울기·적재 시 속도 한계·적재·하역 시간)라는 구조가 같고 필드 이름만 바뀐 것으로 보여, ROP 가 두 판을 함께 받으려면 필드 이름 대응표로 판 무관 속성에 정규화할 수 있을 것으로 보인다. [추정][^ref-323][^ref-228] 판이 바뀔 때의 정규화와 재검증 절차는 후속 질문 q6-05 로 보냈다.

### q1-08 MassRobotics 식별·상태 보고의 능력 필드 {#q1-08}

MassRobotics AMR 상호운용 표준의 공식 JSON 스키마에서 적재량은 식별 보고의 화물 최대 중량·화물 최대 부피 필드로 기술된다. [사실][^ref-230] 반면 로봇이 수행할 수 있는 작업·동작(지원 작업)이나 부착 장비를 기술하는 필드는 없는 것으로 보인다. [추정][^ref-230] 식별·상태 보고의 주요 필드는 [q1-03 답](#q1-03)의 적재·환경 제약 문단에 이미 적었으므로, 여기서는 실행 2026-09-25-35에서 원문으로 다시 확인한 필수·선택 구분, 값의 형식, 빠진 필드를 중심으로 쓴다.

**식별 보고.** 공식 JSON 스키마의 식별 보고(identityReport)는 uuid·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope 를 필수로 두고, 최대 속도(maxSpeed, m/s)·예상 가동 시간(maxRunTime, 시간)·충전기 유형(chargerType)·화물 설명(cargoType)·화물 최대 부피(cargoMaxVolume)·화물 최대 중량(cargoMaxWeight, kg)·제품 문서 링크(productDocumentation)를 선택 필드로 둔다(스키마에 판 번호·발행일이 없어 확인일 2026-09-25 기준). [사실][^ref-230] 이 스키마는 화물 최대 중량을 문자열(string)로, 화물 최대 부피를 객체(object)로 정의하므로, ROP 가 이 값을 화물 중량·치수와 수치로 비교하려면 어댑터에서 형식·단위를 정규화하는 규칙이 필요할 것으로 보인다. [추정][^ref-230] 이 정규화 규칙은 후속 질문 q4-13 으로 보냈다.

**상태 보고.** 같은 스키마의 상태 보고(statusReport)는 uuid·timestamp·operationalState·location 을 필수로 두고, 운용 상태 9종(navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride), 배터리 비율, 남은 가동 시간, 남은 적재 여유 비율(loadPercentageStillAvailable), 오류 코드 배열, 목적지, 약 10초 단기 경로를 둔다(확인일 2026-09-25). [사실][^ref-230] MassRobotics 의 표준 설명 페이지는 이 표준을 로봇이 위치·속도·방향·상태·작업·가용 상태를 공유하고 관찰 용도로 쓰이는 보고 방식으로 설명한다(원문 미열람, 검색 요약 기준, 발행일 미확인). [사실][^ref-391] 운용 상태의 구체 값은 위 스키마 원문에서 확인한 것이다.

**빠진 것.** 지원 작업·부착 장비 필드의 부재는 식별 보고 17개·상태 보고 11개 필드 목록 기준의 관찰이며, 스키마 전체를 글자 단위로 대조한 것이 아니어서 부재의 확정은 아니다. VDA 5050 팩트시트가 적재 세트별 치수·최대 중량·취급 높이와 지원 action 을, IDTA 02047 이 부착 장비 인터페이스를 두는 것과 달리 MassRobotics 식별 보고는 로봇 전체 수준의 최대값(화물 최대 중량·부피, 최대 속도, 가동 시간, 충전기 유형)만 두므로, 분류 원문 질문(누가 이 화물을 실제로 취급할 수 있는가)에 답하려면 ROP 는 적재 취급 방식·지원 동작·장착 장비 정보를 팩트시트·서브모델·매뉴얼 같은 다른 출처에서 보완해야 할 것으로 보인다. [추정][^ref-230][^ref-228][^ref-245]

### q1-09 ECLASS·IEC CDD 의 이동로봇 범위 능력 항목 (부분 답)

실행 2026-09-25-35는 ECLASS 데이터베이스와 IEC 공통 데이터 사전(CDD)을 직접 조회하지 못해, 질문의 핵심인 범위 능력(이동·계단·적재·도어 조작·충전) 항목의 존재 여부를 확인하지 못했다. 대신 IDTA 서브모델 템플릿이 ECLASS 식별자를 어디에 쓰는지를 원문으로 확인했으며, 아래는 그 확인된 부분만이다. 이 질문은 열림으로 둔다.

**IDTA 02047 의 식별자 사용.** IDTA 02047 무인운반차 기술 데이터 1.0 템플릿은 제조사명(0173-1#02-AAO677#004)·보호 등급 IP(0173-1#02-AAV695#003)·실외 사용 적합(0173-1#02-BAD676#009)·최대 적재 질량(0173-1#02-ABJ258#001)·가동 시간 명세값(0173-1#02-AAJ479#004)·최대 가속도(0173-1#02-ABG746#002) 같은 속성에 ECLASS 속성 IRDI 를 붙이고, 측경사 각(MaxLateralInclinationMaxLoad)·기구학 유형(AgvKinematic) 같은 무인운반차 고유 속성에는 IDTA 자체 식별자(admin-shell.io)를 쓴다(확인일 2026-09-25). [사실][^ref-245] 이 관찰은 [q1-05 답](#q1-05)의 [추정] 문장(일부 속성에 ECLASS IRDI, 속도 속성에 IDTA 자체 식별자)을 원문으로 보강한다. 같은 템플릿의 특수 능력(SpecialCapabilities) 요소는 IDTA 자체 식별자를 가진 다국어 자유 텍스트 속성(MultiLanguageProperty)으로, 무인운반차의 특수 능력·기능을 구조 없이 서술하게 한다. [사실][^ref-245]

**분류 클래스 코드의 위치.** IDTA 02047 템플릿에서 ECLASS 분류 클래스 코드 공간(0173-1#01-…) 식별자는 제조사명·제조사 제품 명칭 등 일반 정보 요소와 제품 이미지의 복합 semanticId(예: 0173-1#02-ABK161#002/0173-1#01-AHX838#002)에만 나타나고, 무인운반차·이동로봇 자체를 가리키는 클래스로 쓰인 곳은 확인되지 않았다. [사실][^ref-245] ECLASS IRDI 에서 코드 공간 01 은 분류 클래스를 뜻한다(원문 미열람, 검색 요약 기준). [사실][^ref-392]

**범위 능력.** 이번에 연 IDTA 02047 템플릿 범위에서 범위 능력을 능력 단위로 가리키는 ECLASS 식별자는 확인되지 않았고, ECLASS 는 최대 적재 질량·실외 사용 적합 같은 속성 단위에만 쓰이며 충전·계단·도어 조작 속성은 템플릿에 없는 것으로 보인다(요소 목록 기준, 부재 확정 아님). [추정][^ref-245] 템플릿 JSON 열람 응답이 DecelerationMax 에서 잘려 충전 요소 유무는 미확인이며, 명세 PDF 검색 요약은 ChargingTimeAsSpecified·ChargingDeviceRequirements·BatteryInformation 요소를 전한다(실행 2026-09-25-45 병기, 두 출처가 충돌하며 한쪽을 고르지 않는다). [추정][^ref-245][^ref-198]

**IDTA 02020 의 능력 식별.** IDTA 02020 능력 기술 1.0 템플릿의 능력(Capability) 요소와 속성 요소는 IDTA 일반 템플릿 식별자(admin-shell.io/idta/CapabilityDescription/…)만 두고 특정 능력 사전을 가리키지 않으며, 속성 설명은 값의 의미를 valueId 로 정하게 하고, README 도 표준 능력 사전·분류 체계를 지정하지 않는다. [사실][^ref-243][^ref-229]

**시사점.** AAS 는 요소의 의미를 ECLASS·IEC CDD 같은 외부 사전으로 가리킬 수 있지만 능력 서브모델은 능력 단위 사전을 지정하지 않으므로, 범위 능력의 의미 식별자는 구현자가 정해야 하며 ECLASS·IEC CDD 에 이동로봇 능력 항목이 있어야만 그것을 쓸 수 있을 것으로 보인다(항목 존재 여부는 이번 실행에서 확인하지 못함). [추정][^ref-247][^ref-243][^ref-245] 제조사가 자유 텍스트 항목이나 매뉴얼에 범위 능력을 실제로 어떻게 적는지는 후속 질문 q2-06 으로 보냈다.

#### 실행 2026-09-25-41 보강

실행 2026-09-25-41은 ECLASS·IEC CDD 자료를 한국어·영어로 다시 검색했으나, ECLASS 콘텐츠 데이터베이스(15.0·16.0)와 IEC CDD 트리는 네트워크 정책으로 열지 못해 질문의 핵심(범위 능력 항목의 존재 여부)은 여전히 미확인이다. 이번 실행에서 원문을 연 출처는 IDTA 02047 README 하나이고, 나머지는 검색 결과로 기관·제목·URL 을 확인한 원문 미열람 자료다. 교차 확인은 없으며, 모든 사실이 발행 기관 한 곳의 자료에 기댄다. 한국어 검색에서는 ECLASS 기반 물류로봇 분류·속성 사전을 다룬 국내 자료를 찾지 못했다.

**ECLASS 의 로봇 관련 작업.** ECLASS e.V. 는 Release 15.0 에서 그룹 27-38-01 '로봇(Roboter)'의 클래스를 재구성하고 산업용 로봇 구조에 속성을 추가했으며, 새로 만든 전문가 그룹 'Robotic'이 2024-04-30 첫 회의를 열었다고 알렸다(Release 15.0 발행 2024-11-30(검색 결과 기준), 확인일 2026-09-25). [사실][^ref-182] ECLASS Release 16.0 은 2025-11-28 발행되었고, 약 50,000개 클래스·23,000개 속성·140,000개 키워드를 담으며 새 분류 클래스 137개를 포함한다(단일 출처, 실행 2026-09-25-45 보강). [사실][^ref-185] 16.0 에 이동로봇 클래스가 들어 있는지는 미확인이다.

**ECLASS 분류 구조.** ECLASS 는 4단계 계층의 8자리 코드로 제품 클래스를 분류하며, 각 분류 클래스는 고유 식별자(International Registration Data Identifier, IRDI)·우선 명칭·코드를 갖는다(확인일 2026-09-25). [사실][^ref-184][^ref-392] IRDI 의 코드 공간 01 이 분류 클래스를 뜻한다는 점은 위 부분 답에 적은 것과 같다.

**이동로봇 클래스와 범위 능력 항목.** 이번 한·영 검색 범위에서는 ECLASS 에 무인운반차·자율이동로봇 자체를 가리키는 분류 클래스나 범위 능력(이동·계단·적재·도어 조작·충전)을 능력 단위로 가리키는 항목을 확인하지 못했고, 최근 판 공지에 드러난 로봇 관련 작업은 산업용 로봇 그룹 27-38-01 에 한정된 것으로 보인다(데이터베이스를 직접 조회하지 못한 검색 결과 기준의 관찰이며 부재 확정이 아니다). [추정][^ref-182][^ref-184]

**IEC CDD.** IEC TC 3 의 공통 데이터 사전(Common Data Dictionary, CDD) 안내 페이지는 제품 온톨로지 도메인으로 IEC 61987(공정 자동화), IEC 62683(저압 개폐장치·제어장치), IEC 63213(전기·전자기량 측정 장비)과 단위 도메인 IEC 62720 을 든다(확인일 2026-09-25). [사실][^ref-183] 안내에 든 도메인에 로봇 도메인이 없어 IEC CDD 에서 이동로봇 범위 능력을 가리키는 항목을 가져올 가능성은 낮아 보이지만, 이는 IEC TC 3 안내 페이지에 든 도메인 기준이며 CDD 데이터베이스는 조회하지 못했다. [추정][^ref-183]

**능력의 의미 식별자를 ECLASS 분류로 가리키는 방법.** Vieira da Silva 외(2023-07 프리프린트)는 DIN 8580·VDI 2860 공정 유형을 능력의 의미 식별자(semanticId)로 해당 ECLASS 분류를 써서 나타낼 수 있다고 적어 능력 단위 의미 식별자를 ECLASS 분류 클래스로 가리키는 방법을 제시하며, 그 대상은 제조 공정 유형이고 이동로봇 범위 능력 사례는 아니다(제3자 논문, 원문 미열람). [사실][^ref-037]

**IDTA 02047 README.** IDTA 02047 무인운반차 기술 데이터 1.0 README 는 이 서브모델을 IDTA 가 처음 공식 발행한 1.0 판(AAS 메타모델 3.0 호환)으로 소개하며, ECLASS 분류 클래스·IEC CDD 나 충전·계단·도어·리프트 같은 능력을 언급하지 않는다(발행일 표기 없음, 확인일 2026-09-25, README 기준의 부재 관찰). [사실][^ref-234]

**시사점.** 구축자 의견으로는 IDTA 02020·02047 이 능력 단위 사전을 지정하지 않고 ECLASS·IEC CDD 에서도 이동로봇 범위 능력 항목이 확인되지 않았으므로, ROP 는 당분간 범위 능력의 의미 식별자를 자체 네임스페이스로 정하고 ECLASS 클래스가 생기면 대응시키는 방식을 택하는 것이 현실적이라고 보며, 다만 근거가 된 ECLASS·IEC CDD 항목 부재는 검색 결과·안내 페이지 기준의 관찰이고 부재가 확정된 것은 아니다. [의견][^ref-182][^ref-183][^ref-037] 이 의견은 어느 출처도 권고하지 않은 규범적 판단이며, 네임스페이스·버전 규칙과 등록 제안 책임은 후속 질문 q6-06 으로 보냈다.

#### 실행 2026-09-25-45 보강

실행 2026-09-25-45도 ECLASS 콘텐츠 데이터베이스와 IEC CDD 트리를 네트워크 정책으로 열지 못해 질문의 핵심(범위 능력 항목의 존재 여부)은 여전히 미확인이고, 이 질문은 열림으로 둔다. 이번 실행에서 원문을 연 출처는 공식 저장소의 IDTA 02047 템플릿 JSON 하나인데, 열람 응답이 TechnicalParameters 의 DecelerationMax 요소에서 잘려(열람 응답 절단) 템플릿 전체의 요소를 확인하지 못했다. 나머지 출처는 검색 결과로 기관·제목·URL 을 확인한 원문 미열람 자료이며, 교차 확인은 없다. 한국어 검색에서도 ECLASS 기반 물류로봇 사전을 다룬 국내 자료는 찾지 못했다.

**IDTA 02047 명세의 대상.** IDTA 02047 무인운반차 기술 데이터 1.0 명세(2025-03)는 AGV 를 인트라로지스틱스의 무인 차량·로봇 전체를 가리키는 총칭으로 쓰며, 자율이동로봇이나 유도식 무인 지게차 같은 여러 무인 차량을 대상으로 한다(검색 요약 기준). [사실][^ref-198]

**충전 관련 요소.** IDTA 02047 명세는 제조사가 명시한 완전 방전에서 완전 충전까지의 충전 시간 속성(ChargingTimeAsSpecified), 충전 스테이션·인프라에 대한 무인운반차의 요구(전압 범위·최대 전류 등)를 담는 충전 장치 요구(ChargingDeviceRequirements), 배터리 종류·용량·최대 충전 횟수를 담는 배터리 정보(BatteryInformation) 요소를 두는 것으로 보이며, 충전 시간 속성에 붙는 ECLASS IRDI 는 미확인이다(IDTA 명세 PDF 검색 요약 기준, 원문 미열람). [추정][^ref-198]

**이전 관찰과의 충돌.** 이번에 연 템플릿 JSON 은 열람 응답이 DecelerationMax 에서 잘려 충전·배터리 문자열이 보이지 않았으므로, 실행 2026-09-25-35 가 같은 방식으로 적은 '충전·계단·도어 조작 속성은 템플릿에 없는 것으로 보인다'는 관찰은 위 명세 요약과 어긋나며, 적어도 충전에 대해서는 같은 절단 한계에 기댄 것일 수 있다(확인일 2026-09-25). [추정][^ref-245][^ref-198] 두 출처 가운데 한쪽을 고르지 않고 [열린 질문](../../open-questions.md)에 출처 충돌로 올렸다. 계단·도어 조작에 대해서는 새 근거가 없다.

**ECLASS 를 AAS 에 싣는 지침.** IDTA·ECLASS 공동 지침 'How to transport ECLASS in the Asset Administration Shell'(1.0, 2024-10)은 ECLASS 를 AAS 의 의미로 쓸 때 ECLASS 요소를 AAS 안에서 교환하는 방법을 범위로 하며, 예시는 ECLASS 14.0 기준이다. [사실][^ref-200] 이 지침이 AAS 요소의 semanticId 가 로컬 개념 기술이나 ECLASS·IEC CDD 같은 전역 사전을 가리킬 수 있다고 설명한다는 부분은 검색 요약 기준이다. [사실][^ref-200]

**AAS 능력 모델에서 계획 문제로.** Nabizada 외(arXiv 2606.02167, 2026-06, IEEE CASE 2026 채택(검색 결과 기준))는 VDI 3682 공정 기술, IEC 61360-1 의미 속성 한정, IDTA 02011 유형 계층, IDTA 02016 인스턴스 기술로 구조화한 AAS 능력 모델이 PDDL 계획 문제를 자동 생성하는 데 충분한 정보를 담는다고 보이고, PDDL 전용 서브모델 없이 자원 기능(능력)의 도메인 수준 기술에서 계획 요소를 도출했다. [사실][^ref-201] 이 연구는 생산 시스템 설계 대상이므로 물류 현장 적용 사례가 아니라 방법의 선례로만 쓴다.

**두 층 의미 식별자.** 실행 2026-09-25-35 에서 원문으로 확인한 IDTA 02047 의 속성 단위 ECLASS IRDI 사용(최대 적재 질량 등)과 IDTA 02020 능력 요소가 IDTA 일반 식별자만 둔다는 관찰, 그리고 semanticId 가 ECLASS·IEC CDD·로컬 개념 기술을 가리킬 수 있다는 지침 설명(검색 요약 기준)을 대응시키면, ROP 의 의미 식별자는 능력 단위(자체 네임스페이스 또는 아직 확인되지 않은 사전 항목)와 속성 단위(ECLASS IRDI·IDTA 식별자)의 두 층으로 나뉠 것으로 보인다. [추정][^ref-245][^ref-243][^ref-200] 이 추정은 이 위키의 추론이며, 위 실행 2026-09-25-41 보강의 구축자 의견(자체 네임스페이스)을 새 결론이 아니라 근거 보강으로 뒷받침한다. 충전 시간 속성 자체의 IRDI 는 확인하지 못했다.

#### 실행 2026-09-25-47 보강

실행 2026-09-25-47도 ECLASS 콘텐츠 데이터베이스와 IEC CDD 트리를 네트워크 정책으로 열지 못해, 네 번째 실행에서도 질문의 핵심(범위 능력 항목의 존재 여부)은 미확인이고 이 질문은 열림으로 둔다. 이번 실행에서 원문을 연 출처는 공식 저장소의 IDTA 02047 템플릿 JSON(열람 응답이 다시 잘림), IDTA 02047 README, 서브모델 템플릿 저장소 README 이며, 나머지는 검색 결과로 기관·제목·URL 을 확인한 원문 미열람 자료이고 교차 확인은 없다. 위 실행 2026-09-25-41 보강의 IDTA 02047 README 문장은 이번 실행에서 README 를 다시 열어 같은 내용을 확인했다(확인일 2026-09-25). [사실][^ref-234] 한국어 검색에서는 출처로 쓸 자료를 찾지 못했다.

**IDTA 02047 명세의 묶음 구성.** 명세 PDF 검색 요약 기준(원문 미열람)으로, IDTA 02047 무인운반차 기술 데이터 1.0 명세(2025-03)는 정보를 TypeAndApplicationInformation, TechnicalParameters, VDA5050Factsheet, EnergyAndCommunication(하위 Battery), Safety, TemporaryTechnicalData 서브모델 요소 묶음으로 구조화한다. [사실][^ref-198] 공식 저장소 템플릿 JSON 의 최상위는 GeneralInformation·SpecificDescriptions 이고, TechnicalParameters 는 SpecificDescriptions 아래에 있다(열람 응답이 잘리기 전 범위, 확인일 2026-09-25). [사실][^ref-245]

**충전·배터리 요소의 의미 식별자.** 명세 PDF 검색 요약 기준(원문 미열람)으로, 충전 장치 요구(ChargingDeviceRequirements, 전압 범위·최대 전류 등)와 배터리 정보(BatteryInformation, 배터리 종류·용량·최대 충전 횟수) 요소는 ECLASS IRDI 가 아니라 IDTA 자체 식별자(`https://admin-shell.io/idta/technicaldataagv/chargingdevicerequirements/1/0`, `…/batteryinformation/1/0`)를 의미 식별자로 가지는 것으로 보이며, 이 식별자 문자열은 검증 검색에서 다시 확인되지 않았다. [추정][^ref-198]

**템플릿 열람 절단과 출처 충돌.** 이번에도 템플릿 JSON 열람 응답은 TechnicalParameters 의 DecelerationMax 에서 잘렸고, 명세상 충전·배터리 요소가 속한 EnergyAndCommunication 묶음은 TechnicalParameters 뒤에 나열되므로, 이전 실행들의 '템플릿에 충전 속성 없음' 관찰은 열람 절단에서 생긴 것일 가능성이 높아 보이지만 템플릿 원문으로 확인된 것은 아니다(묶음 순서는 검색 요약의 나열 순서에 기댄 추론, 확인일 2026-09-25). [추정][^ref-245][^ref-198] 위 세 단락은 [열린 질문](../../open-questions.md) oq-060(출처 충돌)의 근거 보강일 뿐 해소가 아니며, oq-060 은 열림으로 둔다.

**게시된 판.** IDTA 공식 서브모델 템플릿 저장소 README 표 기준으로, 게시된 판은 Capability Description 1.0 과 Technical Data for Automated Guided Vehicles 1.0 이 하나씩이고, 기술 데이터 일반 틀(IDTA 02003)은 1.1 과 2.0.1 이 있다(저장소에는 README 표에 없는 published/Technical_Data/1/2 폴더의 PDF 도 있다(검증 검색 기준), 발행일 미확인, 확인일 2026-09-25). [사실][^ref-439]

**IEC 61360-7 교차 도메인 사전.** IEC 61360-7:2024 는 IEC CDD 에 게시된 교차 도메인 데이터 사전 'IEC 61360-7 – General items'를 정하며, 국가·언어 코드, 외함 보호 등급(IP 코드) 같은 모든 데이터 사전에서 쓸 일반 항목과 선택된 AAS 에 대한 참조를 제공한다(기준일 2024, 유럽 채택판 EN IEC 61360-7:2026 이 있다). [사실][^ref-437]

**IEC CDD·ECLASS 의 이동로봇 항목(재확인).** 네 번째 실행에서도 같은 관찰이다: IEC TC 3 안내 페이지의 CDD 도메인에 위 교차 도메인 사전을 합쳐도 확인된 도메인에 로봇 도메인은 없고 ISO 22166 계열 속성이 CDD 에 등록됐다는 자료도 나오지 않아, IEC CDD 에서 이동로봇 범위 능력 항목을 가져올 가능성은 낮아 보이지만, CDD 트리는 조회하지 못했고 CDD 범위가 모든 ISO·IEC 도메인으로 확장되고 있다는 기존 불확실성이 있어 부재 확정이 아니다. [추정][^ref-183][^ref-437] 영·독·한 검색에서도 ECLASS 에 무인운반차·자율이동로봇을 가리키는 분류 클래스 코드는 나오지 않았고, 드러난 로봇 관련 작업은 여전히 산업용 로봇 그룹 27-38-01 에 한정된 것으로 보인다(데이터베이스 미조회, 부재 확정 아님). [추정][^ref-182][^ref-184][^ref-185]

**제품 분류 항목.** IDTA 02003 1.2 판 기준(원문 미열람, 검색 요약 기준)으로, 기술 데이터 일반 틀은 제품 분류 항목(ProductClassificationItem) 묶음으로 제품을 특정 분류 체계·속성 사전의 제품 클래스와 연결하게 하고, 분류 체계 이름(ProductClassificationSystem)의 예로 'ECLASS'와 'IEC CDD'를 든다. [사실][^ref-438] 더 새 판(2.0.1 등)의 해당 요소는 미확인이다.

**세 층 의미 식별자.** 위 실행 2026-09-25-45 보강의 두 층 추정을 대체하지 않고 이 위키의 추론으로 세분하면, AAS 에서 의미 식별자는 제품 분류(IDTA 02003 제품 분류 항목의 ECLASS·IEC CDD 클래스), 능력(IDTA 02020 의 IDTA 일반 식별자), 속성(IDTA 02047 의 ECLASS IRDI 또는 IDTA 자체 식별자 — 충전·배터리 요소의 IDTA 자체 식별자 부분은 검색 요약 기준)의 서로 다른 층에 붙는 것으로 보여, ROP 가 범위 능력을 식별할 때 로봇 제품 클래스와 능력 식별자를 구분해 두어야 할 것으로 보인다. [추정][^ref-438][^ref-243][^ref-245][^ref-198]

## 4. 결론과 남은 불확실성

**결론**

- 로봇 능력을 표현하는 기존 모델로 IEEE 1872 계열 온톨로지, KnowRob·SOMA, PDDL, W3C SSN/SOSA가 확인됐고, 각각 공통 개념·관계, 조작 행동 추론·활동 맥락, 행동의 전제조건·효과, 센서·작동과 운용 범위를 표현한다. [사실][^ref-025][^ref-026][^ref-027][^ref-028][^ref-029][^ref-030]
- CSS 모델은 능력(구현 독립 명세)과 스킬(실행 가능한 구현)을 구분한다. [사실][^ref-035][^ref-036]
- 산업 규격 쪽 기능 기술은 VDA 5050 팩트시트(2.0.0 기준), Open-RMF 작업 유형·사용자 정의 동작 선언처럼 관제 연동 메시지·설정 안에 들어 있다. [추정][^ref-022][^ref-039][^ref-040] MassRobotics AMR 상호운용 표준 1.0은 setup·status 메시지로 제조사·모델, 위치·속도·방향, 상태, 작업·가용 상태를 공유하게 한다. [사실][^ref-033]
- VDA 5050 3.0.0(공식 저장소 main)의 오류 등급은 WARNING·URGENT·CRITICAL·FATAL 넷이고, 사전 정의 action 은 29종이며 dock·lift 라는 이름은 없다. [사실][^ref-051][^ref-031]
- 다섯 정보 항목은 여러 모델에 흩어져 담기며 한 모델이 모두 담는 경우는 확인되지 않았다. 원문을 연 학술 온톨로지 기준으로 전제조건·완료 확인·오류 의미는 SOMA 가, 파라미터 범위·환경 제약은 SSN System Capabilities 가 일부 담고, CORA·IEEE 1872.2 구현은 다섯 항목을 담지 않으며, 적재 제약은 산업 규격에만 있어 ROP 는 적재 제약과 오류의 조치 의미를 산업 규격 쪽에서 가져와야 할 것으로 보인다(q1-03). [추정][^ref-324][^ref-235][^ref-330][^ref-325][^ref-228]
- 능력 기술과 실행 인터페이스의 연결은 같은 프로토콜 안의 이름 맞물림, 능력–스킬–스킬 인터페이스 모델, 연결 없음의 세 방식으로 나뉘는 것으로 보이며, ROP는 둘을 잇는 매핑 계층이 따로 필요할 것으로 보인다(q1-04, 이 위키의 분류). [추정][^ref-228][^ref-036][^ref-230]
- 같은 이름 기능의 의미 차이는 공통 어휘, 사전 정의 동작, 속성 단위 외부 사전 식별자, 분류·일반화 관계로 다뤄지는 것으로 보이나, 동작 의미의 동일성을 판정하는 방법은 확인되지 않았다(q1-05, 이 위키의 분류). [추정][^ref-025][^ref-031][^ref-247][^ref-243]
- ROP용 능력 개념 요구 목록 초안은 아홉 후보로 정리되며, 그 첫 항목인 요구·제공 능력의 속성 단위 비교는 제조 분야 능력 매칭 연구가 의미 규칙으로 구현한 선례가 있다(q1-06). [추정][^ref-229][^ref-327][^ref-228]
- VDA 5050 팩트시트는 2.1.0 태그 기준의 2.x 와 3.0.0 사이에 필드 이름이 바뀌고 ZONE 범위·pauseAllowed·cancelAllowed·supportedZones·batteryCharging 이 더해졌으며, 적재 제약은 두 판 모두 적재 세트에 기술된다(q1-07). [사실][^ref-323][^ref-228]
- MassRobotics 식별 보고는 적재량을 화물 최대 중량·화물 최대 부피 필드로 담는다(q1-08). [사실][^ref-230] 지원 작업·부착 장비 필드는 없는 것으로 보여, ROP 는 적재 취급 방식·지원 동작·장착 장비 정보를 팩트시트·서브모델·매뉴얼 같은 다른 출처에서 보완해야 할 것으로 보인다(q1-08). [추정][^ref-230][^ref-228][^ref-245]
- IDTA 02047 은 ECLASS 식별자를 최대 적재 질량·실외 사용 적합 같은 속성 단위에만 쓰고 IDTA 02020 은 능력 단위 사전을 지정하지 않아, 범위 능력의 의미 식별자는 구현자가 정해야 할 것으로 보인다(q1-09 부분 답). [추정][^ref-247][^ref-243][^ref-245]
- [능력 온톨로지 초안](ontology-draft.md)은 v0.2 → v0.3으로 올랐다: 기능 속성 한정자(요구 / 제공), 개념 실행 상태, 장착 장비 속성 부착 인터페이스·적재 취급 장치 위치(장착 장비 확정)가 반영됐다. 로봇의 구성 버전 수정, 제약 종류 값 추가, 장착 관계와 CORA equippedWith 의 대응 메모는 근거 부족·충돌로 반영하지 않고 초안 6절 질문으로 두었다. 이전 버전의 변경은 v0.1(실행 2026-09-25-02)·v0.2(실행 2026-09-25-16)에 있다. 실행 2026-09-25-35에서는 온톨로지 변경 제안이 없어 v0.3을 유지했다. q1-09 가 부분 답이고 능력 단위 의미 식별자를 뒷받침할 사전 항목을 확인하지 못해, 초안 6절의 '기능의 의미 식별자 속성' 질문은 그대로 두며 이번 근거 보강은 다음 버전 갱신 때 반영한다.

**남은 불확실성**

- 실행 2026-09-25-02의 출처는 모두 원문 미열람이다. 실행 2026-09-25-16·2026-09-25-23·2026-09-25-35는 공식·공개 GitHub 저장소 원문을 열었으나 논문·ISO·KS·IDTA PDF 자료는 원문 미열람이며, 네 실행 모두 교차 확인은 0건이다. 표준·모델마다 발행 주체 한 곳의 자료이거나 같은 저장소의 서로 다른 판에만 기댄다.
- KnowRob 행의 판정은 README 범위에 그치며, KnowRob 자체의 다섯 정보 항목은 판정할 수 없어 SOMA 행에 기댄다.
- PDDL 행은 여전히 검색 요약 수준이며 원문 대조를 하지 않았다.
- 학술 온톨로지 행의 부재 관찰(SSN 의 전제조건·완료·오류·적재, SOMA 의 파라미터 범위·적재, IEEE 1872.2 구현·CORA 번역의 다섯 항목)은 열람 파일 기준이며 부재의 확정이 아니다. SOSA 핵심 모듈과 SOMA 의 다른 모듈, CORA 의 POS·CORAX·RPARTS 파일은 열지 않았다.
- IEEE 1872-2015·1872.2 는 제3자 OWL 번역·구현만 열었고 IEEE 표준 원문(유료)과의 차이는 미확인이다. SSN 파일은 작업반 편집본이라 /TR 판과 문구가 다를 수 있다.
- q1-07 의 2.x 비교는 2.1.0 태그 기준이며 2.0.0 게시판(PDF)과 필드 단위로 같은지는 미확인이다. 2.0.0 태그 명세의 localizationParameters 블록이 게시판에 있는지도 미확인이다. 3.0.0 변경 목록은 확인된 변화이며 완결 목록이 아니다.
- 능력 매칭 논문 2건(Järvenpää 외, Köcher 외)은 원문 미열람이며 검색 요약 범위다. 요구 목록 초안은 이 위키의 종합이며 단일 출처가 없다.
- IDTA 02020 요소 이름이 충돌한다: 공식 1.0 템플릿은 ConstraintSet·CapabilityRealizedBy 를 두지만, 이전 실행이 인용한 제3자 논문은 ConditionContainer·realizedBy 로 적었다. 제3자 논문 표기는 1.0 템플릿에서 확인되지 않으며, 판 차이 여부는 미확인이다.
- VDA 5050 3.0.0의 정확한 발행일이 미확인이다. 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 260421 계열이다.
- MassRobotics 표준 본문 PDF 는 실행 2026-09-25-35에서 압축된 본문을 읽지 못해 판 번호·메시지 의미 설명을 확인하지 못했고, 표준 설명 페이지는 원문 미열람이다. 표준 2.0의 현재 상태도 미확인이다.
- q1-08·q1-09 의 부재 관찰(MassRobotics 의 지원 작업·부착 장비 필드, IDTA 02047 의 충전·계단·도어 조작 속성)은 열람 도구가 나열한 필드·요소 기준이며 부재의 확정이 아니다.
- ECLASS 데이터베이스와 IEC CDD 를 조회하지 못해 무인운반차·이동로봇 분류 클래스와 범위 능력 속성의 존재 여부는 미확인이다(q1-09 열림). ECLASS IRDI 구조 설명 페이지는 원문 미열람이다.
- IDTA 02047 의 측경사 각(MaxLateralInclinationMaxLoad) 식별자는 열람 도구 응답이 한 번 ECLASS IRDI 로 답했다가 원문 인용에서 IDTA 자체 식별자로 확인됐다. 템플릿의 '주행 방식' 요소의 식별자는 확인하지 못했다.
- 실행 2026-09-25-16의 부재 관찰(팩트시트의 범위·전제조건 블록, 관제의 사전 검증 의무, Open-RMF 공통 어휘 장치)은 열람 범위 기준이며 부재의 확정이 아니다.
- CSS 계열 스킬의 FeasibilityCheck·PreconditionCheck 설명은 출처 미확정이다.
- OPC UA Robotics는 노드셋 문서(판 표기 v100)만 열었고 명세 본문과 Part 2 이후 부의 범위는 미확인이다.
- KS B 7321-2 와 ISO 22166-202 의 부합화 여부·제정일은 미확인이다([열린 질문](../../open-questions.md)의 oq-026).
- 국내 논문(신민종·한영석·정재윤, 2024)은 게재 사실만 확인했고 본문 내용은 미확인이다. 한국어 검색에서도 로봇 능력 온톨로지·능력 기반 할당을 다룬 국내 자료는 찾지 못했고, 실행 2026-09-25-35의 한국어 검색에서도 MassRobotics 표준 필드나 ECLASS 기반 이동로봇 속성 사전을 다룬 국내 자료는 찾지 못했다.
- ref-031·ref-034·ref-039·ref-040·ref-228~ref-245·ref-138·ref-323~ref-326·ref-329·ref-355·ref-391·ref-709의 발행일과 ref-236의 저자는 미확인이다.

**실행 2026-09-25-41 결론과 남은 불확실성**

- 결론: ECLASS 최근 판 공지에 드러난 로봇 관련 작업은 산업용 로봇 그룹 27-38-01 에 한정된 것으로 보이며, 무인운반차·자율이동로봇 클래스나 범위 능력 항목은 이번 검색 범위에서 확인되지 않았다(부재 확정 아님). [추정][^ref-182][^ref-184]
- 결론: IEC TC 3 안내 페이지에 든 CDD 도메인에는 로봇 도메인이 없다(안내 페이지 기준, CDD 데이터베이스 미조회). [추정][^ref-183]
- 온톨로지 변경 없음(v0.3 유지): 능력 단위 의미 식별자를 뒷받침할 사전 항목을 확인하지 못해 초안 6절의 '기능의 의미 식별자 속성' 질문을 그대로 두었다. 이번 ECLASS 분류 참조 방법(제조 공정 대상)과 구축자 의견은 그 질문의 근거 보강 후보로만 트랙 로그에 남긴다.
- 불확실성: ECLASS 콘텐츠 데이터베이스(15.0·16.0)와 IEC CDD 트리를 조회하지 못했다. ECLASS 공지·기술 명세 페이지와 IEC TC 3 페이지는 원문 미열람이며 발행일이 미확인이다. Release 15.0 발행일(2024-11-30)은 검색 결과 기준이다.
- 불확실성: 검증 검색 결과는 CDD 레지스트리 범위가 모든 ISO·IEC 도메인으로 확장되고 있다고 적어, 안내 페이지 목록만으로 로봇 도메인의 부재를 일반화할 수 없다.
- 불확실성: IDTA 02020 명세 PDF 는 압축 바이너리라 ECLASS 참조 규정을 읽지 못했다.

**실행 2026-09-25-45 결론과 남은 불확실성**

- 결론: IDTA 02047 명세는 AGV 를 인트라로지스틱스 무인 차량·로봇 전체의 총칭으로 쓴다(검색 요약 기준). [사실][^ref-198]
- 결론: ROP 의 의미 식별자는 능력 단위(자체 네임스페이스 또는 미확인 사전 항목)와 속성 단위(ECLASS IRDI·IDTA 식별자)의 두 층으로 나뉠 것으로 보인다(이 위키의 추론). [추정][^ref-245][^ref-243][^ref-200]
- 온톨로지 변경 없음(v0.3 유지): 능력 단위 의미 식별자 근거가 여전히 없고 충전 속성은 출처 충돌 상태라, 초안 6절의 '기능의 의미 식별자 속성'과 충전 조건 질문을 그대로 두었다.
- 불확실성(출처 충돌): IDTA 02047 명세 PDF 검색 요약은 충전 시간·충전 장치 요구·배터리 정보 요소를 전하지만, 공식 저장소 템플릿 JSON 의 열람 응답은 DecelerationMax 에서 잘려 이 요소를 확인하지 못했다. 실행 2026-09-25-35·2026-09-25-41 의 템플릿 부재 관찰도 같은 절단 한계일 수 있다. 명세 PDF 원문과 충전 시간 속성의 ECLASS IRDI 는 미확인이다.
- 불확실성: ECLASS 콘텐츠 데이터베이스(15.0·16.0)와 IEC CDD 트리는 이번에도 조회하지 못했고, ECLASS 16.0 에 이동로봇 클래스가 있는지와 IEC CDD 에 ISO 22166 계열 속성이 등록됐는지는 미확인이다.
- 불확실성: ECLASS-in-AAS 지침과 Nabizada 외(2026) 프리프린트는 원문 미열람이며, 모든 발견이 발행 기관 한 곳의 자료에 기대 교차 확인이 없다.

**실행 2026-09-25-47 결론과 남은 불확실성**

- 결론: IDTA 02047 명세는 정보를 TypeAndApplicationInformation·TechnicalParameters·VDA5050Factsheet·EnergyAndCommunication(하위 Battery)·Safety·TemporaryTechnicalData 묶음으로 구조화한다(명세 PDF 검색 요약 기준). [사실][^ref-198]
- 결론: IDTA 02003 1.2 판은 제품 분류 항목으로 제품을 ECLASS·IEC CDD 같은 분류 체계의 제품 클래스에 연결하게 한다. [사실][^ref-438]
- 결론: 의미 식별자는 제품 분류·능력·속성의 세 층으로 나뉘는 것으로 보여 로봇 제품 클래스와 능력 식별자를 구분해 두어야 할 것으로 보인다(이 위키의 추론, 실행 2026-09-25-45 두 층 추정의 세분). [추정][^ref-438][^ref-243][^ref-245]
- 온톨로지 변경 없음(v0.3 유지): 세 층 식별자는 추정이고 능력 단위 사전 항목 근거가 여전히 없으며 충전 요소는 출처 충돌(oq-060) 상태라, 초안 6절의 '기능의 의미 식별자 속성'과 충전 조건 질문을 그대로 두었다.
- 불확실성(출처 충돌): 템플릿 JSON 은 이번 실행과 검증자 재열람 모두 DecelerationMax 에서 잘려 충전·배터리 요소를 원문으로 확인하지 못했다. 열람 절단 설명은 근거 보강일 뿐 oq-060 은 열림이다. 충전·배터리 요소의 IDTA 자체 식별자 문자열은 검증 검색에서 다시 확인되지 않았고, 충전 시간 속성의 ECLASS IRDI 도 미확인이다.
- 불확실성: ECLASS 콘텐츠 데이터베이스와 IEC CDD 트리는 네 번째 실행에서도 조회하지 못했다. 사용자가 조회 결과를 inbox/sources 로 넣을지, q1-09 를 사유와 재개 조건을 적어 보류할지 결정이 필요하다.
- 불확실성: IDTA 02003 은 1.2 판, IEC 61360-7 은 2024 판 기준이며 더 새 판(2.0.1, EN IEC 61360-7:2026)의 내용은 미확인이다. IEC 61360-7 제목의 부제는 검색 결과 표기 기준이다. 모든 발견이 발행 기관 한 곳의 자료에 기대 교차 확인이 없다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q1-07 | VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f12 (실행 2026-09-25-02) | 답함 |
| q1-08 | MassRobotics AMR 상호운용 표준의 setup·status 메시지 스키마에는 로봇 능력(적재량, 지원 작업, 부착 장비)을 기술하는 필드가 있는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f13 (실행 2026-09-25-02) | 답함 |
| q4-06 | IDTA 02020 능력 서브모델의 속성·제약(ConditionContainer)과 VDA 5050 팩트시트의 적재 명세·지원 action 을 서로 매핑할 수 있는가, 매핑하면 무엇이 남는가? | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f17 (실행 2026-09-25-02) | 열림 |
| q5-05 | 제조사 매뉴얼에서 추출한 광고 능력과 현장 시험으로 확인한 운용 능력의 차이를 어떤 지표로 측정하고 온톨로지에 함께 기록할 것인가? | 단계 5. 완전성과 정확성을 검증하는 방법 조사 | f27 (실행 2026-09-25-02) | 열림 |
| q1-09 | ECLASS·IEC CDD 에 이동로봇의 범위 능력(이동·계단·적재·도어 조작·충전)과 그 속성을 기술하는 항목이 있는가, 있으면 능력 온톨로지의 의미 식별자로 쓸 수 있는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f30 (실행 2026-09-25-16) | 열림 |
| q4-09 | CSS 참조 모델의 스킬 상태 기계(SkillType·SkillStateMachine)와 VDA 5050 action 상태(WAITING~FAILED·RETRIABLE), Open-RMF execute_action 완료 신호를 하나의 스킬 실행 상태 모델로 대응시킬 수 있는가? | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f26 (실행 2026-09-25-16) | 열림 |
| q5-07 | 서로 다른 제조사가 정의한 사용자 정의 action(예: 도킹·리프트)이 같은 동작인지를 파라미터·완료 정의·효과 비교로 판정하는 시험 절차를 어떻게 둘 것인가? | 단계 5. 완전성과 정확성을 검증하는 방법 조사 | f35 (실행 2026-09-25-16) | 열림 |
| q6-05 | VDA 5050 2.x 와 3.0.0 팩트시트를 함께 받는 현장에서 판마다 다른 필드 이름(maxWeight→maximumWeight 등)을 능력 온톨로지의 판 무관 속성으로 정규화하고, 판이 바뀔 때 능력 정의를 어떻게 재검증하는가? (q1-07 에서 파생) | 단계 6. 변경 관리·운영·거버넌스 조사 | f6 (실행 2026-09-25-23) | 열림 |
| q4-13 | MassRobotics 식별 보고의 화물 최대 중량(문자열)·최대 부피(객체) 값을 VDA 5050 팩트시트 적재 세트의 수치 필드와 같은 단위·형식으로 정규화해 화물 요구와 비교하는 어댑터 규칙을 어떻게 둘 것인가? (q1-08 에서 파생) | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f6 (실행 2026-09-25-35) | 열림 |
| q2-06 | 제조사는 IDTA 02047 의 특수 능력(SpecialCapabilities) 같은 자유 텍스트 항목이나 매뉴얼에 계단·도어 조작·충전 같은 범위 능력을 실제로 어떻게 적는가? (q1-09 에서 파생) | 단계 2. 로봇 문서 유형과 정보 구조 조사 | f8 (실행 2026-09-25-35) | 열림 |
| q6-06 | ECLASS 에 이동로봇 범위 능력(이동·계단·적재·도어 조작·충전) 클래스·속성이 없을 때 ROP 는 자체 의미 식별자를 어떤 네임스페이스·버전 규칙으로 두고, ECLASS 변경 요청(전문가 그룹 'Robotic' 등)으로 등록을 제안하는 책임은 누가 지는가? (q1-09 에서 파생) | 단계 6. 변경 관리·운영·거버넌스 조사 | f8 (실행 2026-09-25-41) | 열림 |
| q4-14 | IDTA 02047 의 충전 관련 요소(충전 시간, 충전 장치 요구, 배터리 정보)를 VDA 5050 3.0.0 팩트시트의 batteryCharging(임계 저충전 수준·희망 최소·최대 충전 수준·최소 충전 시간)과 대응시켜 범위 능력 '충전'의 판 무관 속성으로 정규화할 수 있는가? (q1-09 에서 파생) | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f1 (실행 2026-09-25-45) | 열림 |
| q4-15 | IDTA 02047 이 서브모델 안에 VDA5050Factsheet 묶음을 둘 때 VDA 5050 팩트시트의 어느 판·필드를 담으며, 팩트시트와 AAS 서브모델이 같은 능력 값(적재·충전 등)을 이중으로 가질 때 능력 온톨로지는 어느 쪽을 근거 문서로 삼고 불일치를 어떻게 처리하는가? (q1-09 에서 파생) | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f1 (실행 2026-09-25-47) | 열림 |

같은 질문은 [질문 백로그](question-backlog.md)에 등록된다(백로그 반영은 퍼블리셔가 한다). 실행 2026-09-25-16에서 함께 제안된 "VDA 5050 팩트시트의 action 파라미터 범위를 IDTA 02020 범위 속성으로 보완할 수 있는가" 질문은 q4-06 과 중복이라 등록하지 않았다. 실행 2026-09-25-23에서 제안된 "작업 요구를 요구 능력 속성으로 표현해 로봇 적재 세트와 비교하는 규칙의 질의·규칙 형식" 질문은 q4-07 과 중복이라 등록하지 않았다. 백로그에 중복 등록된 q1-10(q1-09 와 같은 질문), q4-11(q4-09 와 같은 질문), q5-08(q5-07 과 같은 질문)은 실행 2026-09-25-23에서 폐기했다. 실행 2026-09-25-35의 새 질문 2건(q4-13, q2-06)은 1차 검증에서 백로그 중복이 없다고 판정됐다. 실행 2026-09-25-41의 새 질문 q6-06 은 1차 검증에서 q6-02·q6-03 과 초점이 달라 중복이 아니라고 판정됐다. 실행 2026-09-25-45의 새 질문 q4-14 는 1차 검증에서 q4-06(IDTA 02020 대 팩트시트)·q4-13(MassRobotics 대 팩트시트)과 대상이 달라 중복이 아니라고 판정됐다. 실행 2026-09-25-47의 새 질문 q4-15 는 1차 검증에서 q4-02(문서 대 실제 API)·q4-06(IDTA 02020 대 팩트시트)·q4-14(충전 요소 정규화)와 초점이 달라 중복이 아니라고 판정됐다.

## 6. 완료 조건 충족 현황

완료 조건은 트랙 정의의 문장을 옮기되 파일명은 페이지 링크로 바꾸고, 조건이 여러 항목이면 행을 나눴다. 트랙 정의의 문장은 아래 인용 블록에 그대로 두었고, [트랙 개요](index.md)의 단계 진행 현황 표에도 같은 조건이 링크를 붙인 형태로 있다. 충족 여부는 리서치 에이전트의 자체 평가와 1차 검증의 지시를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

> 완료 조건: 모델·표준 비교표(`model-standard-comparison.md`) 작성, ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 반영됨.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 모델·표준 비교표([model-standard-comparison.md](model-standard-comparison.md)) 작성 | 미충족 | [모델·표준 비교표](model-standard-comparison.md)의 후보 10행과 후보 밖 5행 모두에 조사 결과가 있으나, PDDL·OPC UA Robotics·MassRobotics·AAS·Open-RMF 행과 후보 밖 RCO·이종 자율 로봇 능력·스킬 모델 행에는 "미조사" 칸이 남아 있다(실행 2026-09-25-47 리서치 자체 평가와 1차 검증 기준). 학술 온톨로지 행은 실행 2026-09-25-23에서, MassRobotics 행의 일부 칸은 실행 2026-09-25-35에서 채웠고, 실행 2026-09-25-47에서는 IDTA 02047 행의 종류·출처 칸만 보강해 미조사 칸은 그대로다 | 미충족 · 미승인 |
| ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 반영됨 | 미충족 | 초안은 실었으나 일부만 개념에 반영: 아홉 후보 가운데 요구·제공 한정자, 실행 상태, 부착 인터페이스·적재 취급 장치 위치만 [능력 온톨로지 초안](ontology-draft.md) v0.3에 반영됐고 구성 버전·운용 구역·환경 조건·충전 조건은 6절 질문으로 남았다. 실행 2026-09-25-35·2026-09-25-41·2026-09-25-45·2026-09-25-47에서는 온톨로지 변경이 없다 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(모델·표준 비교표 미조사 칸 잔존, 요구 목록 일부 미반영, 막힌 질문 q1-09)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 각 항목 뒤에는 이 단계에서 확인된 사실을 그 영역 페이지의 어느 절에 반영하자고 제안할지를 적었다. 반영 제안은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안" 항목으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

**중심 영역**

- [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 트랙이 출발하는 영역이다. 실행 2026-09-25-02에서 "4. 핵심 개념과 용어"(능력·스킬 구분, 전제조건·효과, 광고 능력·운용 능력), "7. 관련 표준·프레임워크·오픈소스"(IEEE 1872 계열, SSN/SOSA, CSS, IDTA 02020), "8. 대표 연구와 자료"(KnowRob·SOMA, RCO, 서베이, 국내 논문) 절에 반영을 제안했다. 실행 2026-09-25-16에서 "4. 핵심 개념과 용어"(능력·스킬·스킬 인터페이스, 속성 제약, 의미 식별자), "6. 대표 접근법과 기술"(능력–명령 연결 방식과 이름 의미 차이 대응 방식), "7. 관련 표준·프레임워크·오픈소스"(VDA 5050 팩트시트, IDTA 02020·02047, MassRobotics 스키마, CaSkMan, SkiROS2) 절에 반영을 제안했다. 실행 2026-09-25-23에서 "4. 핵심 개념과 용어"(요구 능력·제공 능력, 능력 매칭), "7. 관련 표준·프레임워크·오픈소스"(CORA·SSN·SOMA 가 다섯 정보 항목을 담는 정도), "8. 대표 연구와 자료"(Järvenpää 외, Köcher 외의 능력 매칭 연구) 절에 반영을 제안했다. 실행 2026-09-25-35에서 "7. 관련 표준·프레임워크·오픈소스" 절에 MassRobotics 식별 보고의 능력 필드 범위와 지원 작업·부착 장비 필드 부재, IDTA 02020 이 능력 단위 사전을 지정하지 않는다는 점의 반영을 제안했다.

**연구 방법으로 연결되는 영역(분류 원문 8장의 교차 규칙)**

- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 매뉴얼 해석은 이 영역의 방법이 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 것으로 다룬다. 단계 1에서는 기존 모델·표준이 AI가 해석한 기능 정보(신뢰도, 근거 위치)를 담을 자리를 갖는지의 관점으로 연결한다. 실행 2026-09-25-02·2026-09-25-16·2026-09-25-23·2026-09-25-35에서는 이 영역에 해당하는 발견 사항이 없어 반영 제안을 내지 않았다.

**이 단계의 질문이 언급하는 영역(트랙 개요의 배정에 따른 추가 연결, [가정])**

- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — q1-04(능력 기술과 실행 인터페이스의 연결)와 q1-02의 Open-RMF Fleet Adapter 후보가 이 영역의 어댑터 문제에 닿는다. 실행 2026-09-25-02에서 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 팩트시트·오류 보고, MassRobotics 메시지, Open-RMF 작업 능력·사용자 정의 동작의 반영을 제안했다. 실행 2026-09-25-16에서 "6. 대표 접근법과 기술"·"7. 관련 표준·프레임워크·오픈소스" 절에 어댑터가 능력 선언을 명령으로 옮기는 방식, VDA 5050 3.0.0 오류 등급·action 상태, MassRobotics 보고 전용 구조의 반영을 제안했다. 실행 2026-09-25-23에서 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 2.x(2.1.0 태그)와 3.0.0 팩트시트의 필드 이름 변화와 추가 필드, 어댑터가 두 판을 함께 받을 때의 정규화 필요의 반영을 제안했다. 실행 2026-09-25-35에서 같은 절에 MassRobotics 식별·상태 보고 필드와 화물 최대 중량(문자열)·최대 부피(객체) 값의 어댑터 정규화 필요의 반영을 제안했다.
- [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 범위 능력 "충전"의 연결 영역이다. 실행 2026-09-25-23에서 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 3.0.0 팩트시트의 충전 설정(batteryCharging)이 충전 시점 계획의 입력이 될 수 있다는 점의 반영을 제안했다.
- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — q1-02의 산업 상호운용 규격 조사가 이 영역의 공통 규격·적합성 시험에 닿는다. 실행 2026-09-25-02에서 "7. 관련 표준·프레임워크·오픈소스" 절에 능력 기술 관련 표준·규격의 발행 기관과 현재 판의 반영을 제안했다. 실행 2026-09-25-16에서 같은 절에 공통 어휘(IEEE 1872), 의미 식별자(AAS IEC 61360·ECLASS), 서비스 로봇 모듈 정보 모델(ISO 22166-202, KS B 7321-2)의 반영을 제안했다. 실행 2026-09-25-35에서 같은 절에 IDTA 02047 의 ECLASS 속성 IRDI 사용 범위와 무인운반차 고유 속성의 IDTA 자체 식별자, 능력 단위 의미 식별자의 공백의 반영을 제안했다.

실행 2026-09-25-41에서는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)의 "7. 관련 표준·프레임워크·오픈소스" 절에 ECLASS Release 15.0 의 로봇 그룹 27-38-01 재구성과 전문가 그룹 'Robotic', Release 16.0 발행, IEC CDD 안내 도메인과 그 안에 로봇 도메인이 없다는 추정(안내 페이지 기준)의 반영을 제안했고, [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)의 같은 절에 ECLASS·IEC CDD 에서 이동로봇 범위 능력 항목이 확인되지 않았다는 추정의 반영을 제안했다.

실행 2026-09-25-45에서는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)의 "7. 관련 표준·프레임워크·오픈소스" 절에 IDTA 02047 이 AGV 를 인트라로지스틱스 무인 차량·로봇의 총칭으로 쓴다는 점, 충전 관련 요소(명세 PDF 검색 요약 기준의 [추정], 템플릿 열람과 출처 충돌), IDTA·ECLASS 의 ECLASS-in-AAS 지침의 반영을 제안했고, [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)의 같은 절에 IDTA 02047 의 충전 시간·충전 장치 요구·배터리 정보 요소가 충전기 배분·충전 시점 계획의 입력 후보가 될 수 있다는 [추정]의 반영을 제안했다.

실행 2026-09-25-47에서는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)의 "7. 관련 표준·프레임워크·오픈소스" 절에 IDTA 02047 의 서브모델 요소 묶음(VDA5050Factsheet 포함, 검색 요약 기준)과 충전·배터리 요소의 IDTA 자체 식별자([추정]), IDTA 02003 제품 분류 항목으로 ECLASS·IEC CDD 제품 클래스를 가리키는 방법의 반영을 제안했고, [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)의 같은 절에 IDTA 02047 의 EnergyAndCommunication/Battery 묶음과 충전 장치 요구·배터리 정보 요소가 충전기 배분·충전 시점 계획의 입력 후보라는 [추정]의 반영을, [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)의 같은 절에 IEC 61360-7 교차 도메인 사전, IEC CDD 에 로봇 도메인이 확인되지 않는다는 추정, IDTA 02003 제품 분류 항목의 ECLASS·IEC CDD 참조의 반영을 제안했다.

## 8. 출처

[^ref-022]: VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control, 2022-01, https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-025]: IEEE, 1872-2015 - IEEE Standard Ontologies for Robotics and Automation, 2015, https://ieeexplore.ieee.org/document/7084073/, 접근일 2026-09-25 (원문 미열람)
[^ref-026]: IEEE, IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology, 2022, https://standards.ieee.org/standard/1872_2-2021.html, 접근일 2026-09-25 (원문 미열람)
[^ref-027]: Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G., KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents, 2018, https://ai.uni-bremen.de/papers/beetz18knowrob.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-028]: Beßler, D. 외, Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents, 2021, https://arxiv.org/pdf/2011.11972, 접근일 2026-09-25 (원문 미열람)
[^ref-029]: McDermott, D. 외, PDDL - The Planning Domain Definition Language, 1998, https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language, 접근일 2026-09-25 (원문 미열람)
[^ref-030]: W3C / OGC, Semantic Sensor Network Ontology, 2017-10-19, https://www.w3.org/TR/vocab-ssn/, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-09-25 (원문 미열람)
[^ref-033]: MassRobotics, Autonomous Mobile Robot Standards Published by MassRobotics, 2021-05, https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/, 접근일 2026-09-25 (원문 미열람)
[^ref-034]: OPC Foundation / VDMA, OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration, 미확인, https://reference.opcfoundation.org/specs/OPC-40010-1, 접근일 2026-09-25 (원문 미열람)
[^ref-035]: Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services, 2022-11, https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html, 접근일 2026-09-25 (원문 미열람)
[^ref-036]: Köcher, A. 외, A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing, 2022, https://arxiv.org/abs/2209.09632, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-25 (원문 미열람)
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25 (원문 미열람)
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-042]: Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R., A survey of ontology-enabled processes for dependable robot autonomy, 2024-07, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full, 접근일 2026-09-25 (원문 미열람)
[^ref-043]: 신민종, 한영석, 정재윤, 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-25 (원문 미열람)
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25
[^ref-243]: IDTA (admin-shell-io/submodel-templates), IDTA 02020_Template_Capability_Description.json, 미확인, https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json, 접근일 2026-09-25
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-244]: OPC Foundation (UA-Nodeset GitHub), UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv, 미확인, https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv, 접근일 2026-09-25
[^ref-245]: IDTA (admin-shell-io/submodel-templates), IDTA 02047-1-0 Template_TechnicalDataForAGV.json, 미확인, https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json, 접근일 2026-09-25
[^ref-246]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M., An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021, https://www.sciencedirect.com/science/article/pii/S2351978921002249, 접근일 2026-09-25 (원문 미열람)
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-247]: IDTA(Industrial Digital Twin Association), Specification of the Asset Administration Shell Part 3a: Data Specification – IEC 61360 (IDTA-01003-a-3-0-2), 2024-07, https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-248]: ISO, ISO 22166-202:2025 - Robotics — Modularity for service robots — Part 202: Information model for software modules, 2025, https://www.iso.org/standard/84589.html, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)
[^ref-249]: Dussard, B. 외, Ontological Component-based Description of Robot Capabilities, 2023-06, https://arxiv.org/abs/2306.07569, 접근일 2026-09-25 (원문 미열람)
[^ref-250]: RVMI lab, Aalborg University (SkiROS2 GitHub), SkiROS2 — README (skill-based robot control platform), 미확인, https://github.com/RVMI/skiros2, 접근일 2026-09-25
[^ref-323]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 (tag 2.1.0) — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-329]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 (tag 2.0.0) — VDA5050_EN_V1.md, 미확인, https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md, 접근일 2026-09-25
[^ref-235]: W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub), ssn/integrated/ssn-system.ttl (SSN System Capabilities module), 미확인, https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl, 접근일 2026-09-25
[^ref-324]: EASE CRC (ease-crc/soma), SOMA — owl/SOMA-ACT.owl, 미확인, https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl, 접근일 2026-09-25
[^ref-325]: Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub), IndustrialStandard-ODP-IEEE1872-2 — AuR_IEEE1872-2.ttl, 미확인, https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2/blob/main/AuR_IEEE1872-2.ttl, 접근일 2026-09-25
[^ref-330]: srfiorini (IEEE1872-owl GitHub), IEEE1872-owl — cora-bare.owl (OWL specification of CORA), 미확인, https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl, 접근일 2026-09-25
[^ref-326]: KnowRob (knowrob GitHub), knowrob — README (dev branch), 미확인, https://github.com/knowrob/knowrob, 접근일 2026-09-25
[^ref-327]: Järvenpää, E., Siltala, N., Hylli, O., Nylund, H., & Lanz, M., Semantic rules for capability matchmaking in the context of manufacturing system design and reconfiguration, 2023, https://www.tandfonline.com/doi/full/10.1080/0951192X.2022.2081361, 접근일 2026-09-25 (원문 미열람)
[^ref-328]: Köcher, A., Vieira da Silva, L. M., & Fay, A., Automated Process Planning Based on a Semantic Capability Model and SMT, 2023-12, https://arxiv.org/abs/2312.08801, 접근일 2026-09-25 (원문 미열람)
[^ref-391]: MassRobotics, What Is the MassRobotics AMR Interoperability Standard?, 미확인, https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/, 접근일 2026-09-25 (원문 미열람)
[^ref-392]: ECLASS e.V., IRDI - ECLASS Technischer Support, 미확인, https://eclass.eu/support/technical-specification/structure-and-elements/irdi, 접근일 2026-09-25 (원문 미열람)

[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25
[^ref-182]: ECLASS e.V., Neuer Content für ECLASS Release 15.0, 미확인, https://eclass.eu/aktuelles/news/neuer-content-fuer-eclass-release-150, 접근일 2026-09-25 (원문 미열람)
[^ref-183]: IEC TC 3, Common Data Dictionary – CDD – TC 3, 미확인, https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/, 접근일 2026-09-25 (원문 미열람)
[^ref-184]: ECLASS e.V., Classification Class - ECLASS Technischer Support, 미확인, https://eclass.eu/support/technical-specification/structure-and-elements/classification-class, 접근일 2026-09-25 (원문 미열람)
[^ref-185]: ECLASS e.V., The latest ECLASS Release, 미확인, https://eclass.eu/en/eclass-standard/releases, 접근일 2026-09-25 (원문 미열람)

[^ref-198]: IDTA(Industrial Digital Twin Association), IDTA 02047-1-0 Technical Data for AGV in Intralogistics, 2025-03, https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-200]: IDTA / ECLASS e.V., GUIDELINE How to transport ECLASS in the Asset Administration Shell (IDTA ECLASS Semantic Transport, 1.0), 2024-10, https://industrialdigitaltwin.org/wp-content/uploads/2024/10/2024-10_IDTA_ECLASS_Semantic_Transport_ECLASS_in_AAS_1.0.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06, https://arxiv.org/abs/2606.02167, 접근일 2026-09-25 (원문 미열람)

[^ref-437]: IEC, IEC 61360-7:2024 — Standard data element types with associated classification scheme — Part 7: Data dictionary of cross-domain concepts, 2024, https://webstore.iec.ch/en/publication/72956, 접근일 2026-09-25 (원문 미열람)
[^ref-438]: IDTA(Industrial Digital Twin Association), IDTA 02003-1-2 Generic Frame for Technical Data for Industrial Equipment in Manufacturing, 미확인, https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-439]: IDTA (admin-shell-io/submodel-templates), admin-shell-io/submodel-templates — README (published Submodel Templates list), 미확인, https://github.com/admin-shell-io/submodel-templates, 접근일 2026-09-25

## 9. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 온톨로지 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-47 | 없음(q1-09 부분 답 보강) | 새 질문 1건(q4-15) | 온톨로지 변경 없음(v0.3 유지) | 8 |
| 2026-09-25 | 2026-09-25-45 | 없음(q1-09 부분 답 보강) | q4-14 | 없음(v0.3 유지) | 7 |
| 2026-09-25 | 2026-09-25-41 | 없음(q1-09 부분 답 보강) | q6-06 | 없음(v0.3 유지) | 6 |
| 2026-09-25 | 2026-09-25-35 | q1-08(q1-09 부분 답) | q4-13, q2-06 | 없음(v0.3 유지) | 5 |
| 2026-09-25 | 2026-09-25-23 | q1-03, q1-06, q1-07 | q6-05(중복 q1-10·q4-11·q5-08 폐기) | v0.2 → v0.3 | 4 |
| 2026-09-25 | 2026-09-25-16 | q1-04, q1-05(q1-03 부분 답 갱신) | q1-09, q4-09, q5-07 | v0.1 → v0.2 | 3 |
| 2026-09-25 | 2026-09-25-02 | q1-01, q1-02(q1-03 부분 답) | q1-07, q1-08, q4-06, q5-05 | v0 → v0.1 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 없음 | 시드 q1-01~q1-06(6건, 구축 시 [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [능력 온톨로지 초안](ontology-draft.md)에서 생성) | 1 |
