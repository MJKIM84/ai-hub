---
title: "단계 1. 기존 능력 표현 모델과 표준 조사"
type: track-stage
track: manual-capability-ontology
stage: 1
related_areas: [5, 27, 9, 28, 16]
tags: [능력 온톨로지, 산업 상호운용 규격, 모델·표준 비교표, ROP용 능력 개념, VDA 5050 팩트시트]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-022, ref-025, ref-026, ref-027, ref-028, ref-029, ref-030, ref-031, ref-032, ref-033, ref-034, ref-035, ref-036, ref-037, ref-038, ref-039, ref-040, ref-041, ref-042, ref-043, ref-044, ref-045, ref-046, ref-047, ref-048]
last_run: 2026-09-25
version: 3
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 단계 1. 기존 능력 표현 모델과 표준 조사

# 단계 1. 기존 능력 표현 모델과 표준 조사

> 단계 상태: 진행 중 · 열린 질문: 6건 · 답한 질문: 3건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 로봇의 능력·스킬·작업을 표현하는 기존 온톨로지와 표준이 무엇을 담고 무엇을 못 담는가.

위 문장은 트랙 정의의 "밝힐 것"을 그대로 옮긴 것이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 이 단계는 트랙의 중심 영역인 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)에서 출발한다. 조사 결과는 [모델·표준 비교표](model-standard-comparison.md)와, 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)용 능력 개념 요구 목록 초안의 형태로 [능력 온톨로지 초안](ontology-draft.md)에 반영된다.

## 2. 질문 목록

이 단계의 시작 질문 6개와, 실행 2026-09-25-02에서 생겨 이 단계로 들어온 후속 질문 2개, 실행 2026-09-25-90에서 생긴 후속 질문 1개다. 시작 질문 문장은 괄호 안의 내용까지 트랙 정의 그대로다. 괄호 안의 이름은 리서치 에이전트가 실재·최신성을 확인해야 할 출처 후보이지 확인된 출처가 아니다. 후보 이름 속 약어(IEEE, PDDL, W3C, VDA, OPC UA 등)는 트랙 정의의 후보 이름 그대로 두며, 실재를 확인한 뒤 발행 기관의 공식 명칭으로 풀어 쓴다. 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. [가정] 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커(예: `#q1-01`) 또는 주제 페이지 링크를 적는다. 뒤 단계에서 되돌아온 질문은 이 단계 태그로 이 표에 추가하고 다음 트랙 실행에서 우선 처리한다. 제기 근거 칸의 값은 [질문 백로그](question-backlog.md)의 항목 형식과 같이 finding id(제안한 실행의 발견 사항 id) 또는 "사용자" 가운데 하나만 쓴다. 시드 질문은 사용자가 정의한 트랙 정의의 시작 질문이므로 백로그와 같게 "사용자"로 적는다.

페이지 상단의 단계 상태 줄(단계 상태 · 열린 질문 · 답한 질문 · 완료 조건 · 마지막 실행)은 퍼블리셔가 다시 쓰는 자동 갱신 영역이 아니라, 스토리텔러 에이전트가 이 페이지를 갱신할 때 [질문 백로그](question-backlog.md)와 맞추는 값이다. 기준값은 [트랙 개요](index.md)의 단계 진행 현황 자동 표(상태·열린 질문 수·완료 조건 충족 여부)와 최근 실행 자동 표(마지막 실행)이며, 이 줄과 그 표가 다르면 그 표를 따른다. [가정]

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q1-01 | 로봇 능력·작업을 표현하는 온톨로지·지식 모델에는 무엇이 있고 각각 무엇을 표현하는가? (후보: IEEE 1872 CORA, IEEE 1872.2 자율 로봇 온톨로지, KnowRob·SOMA, PDDL 계열 행동 모델, W3C SSN/SOSA) | 답함 | 사용자 | 2026-09-25-02 | [#q1-01](#q1-01) |
| q1-02 | 산업 상호운용 규격은 로봇 기능을 어떤 형식으로 기술하는가? (후보: VDA 5050의 팩트시트, MassRobotics AMR 상호운용 표준, OPC UA Robotics, Asset Administration Shell의 능력·스킬·서비스 모델, Open-RMF Fleet Adapter의 기능 기술) | 답함 | 사용자 | 2026-09-25-02 | [#q1-02](#q1-02) |
| q1-03 | 이 모델들은 ROP가 배정·실행·검증에 필요로 하는 정보 — 전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미 — 를 얼마나 담는가? 빠진 것은 무엇인가? | 열림 | 사용자 | | |
| q1-04 | 능력 기술과 실행 인터페이스(명령·상태)는 기존 표준에서 어떻게 연결되는가? | 열림 | 사용자 | | |
| q1-05 | 제조사마다 같은 이름의 기능('운반', '도킹', '리프트')이 다른 의미를 갖는 문제를 기존 모델은 어떻게 다루는가? | 열림 | 사용자 | | |
| q1-06 | 부록 A 5번 정의의 요소(제조사별 기능·제약·장착 장비·실행 조건, 작업 요구)를 기준으로 ROP용 능력 개념에 무엇을 더 추가해야 하는가? | 열림 | 사용자 | | |
| q1-07 | VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가? | 답함 | f12, 실행 2026-09-25-02 | 2026-09-25-90 | [#q1-07](#q1-07) |
| q1-08 | MassRobotics AMR 상호운용 표준의 setup·status 메시지 스키마에는 로봇 능력(적재량, 지원 작업, 부착 장비)을 기술하는 필드가 있는가? | 열림 | f13, 실행 2026-09-25-02 | | |
| q1-09 | q1-07 후속: VDA 5050 2.1.0→3.0.0에서 이름이 바뀐 팩트시트 필드(예: agvSpeedLimit→maximumSpeed, maxWeight→maximumWeight)는 설명문·단위·필수 여부까지 같은가, 의미가 바뀐 필드가 있다면 기존 2.x 로봇의 팩트시트를 3.0 능력 모델로 옮길 때 무엇을 다시 확인해야 하는가? | 열림 | f4, 실행 2026-09-25-90 | | |

표의 질문 문장은 트랙 정의(q1-01~q1-06)와 리서치 브리프(q1-07·q1-08·q1-09) 그대로 두었다. 다음은 구축자 보충이다. q1-06의 "부록 A 5번 정의"에서 5번은 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)를 가리킨다. "부록 A"는 이 위키의 분류 원문(`_source/ROP_SCM_연구분야_분류.md`)을 뜻한다. q1-02의 AMR은 자율이동로봇(Autonomous Mobile Robot, AMR)이다.

## 3. 조사 결과

q1-01·q1-02·q1-03은 실행 2026-09-25-02에서 페이지 열람이 차단된 환경으로 조사했다. 그 출처는 모두 검색 결과의 기관·제목·URL 일치로만 실재를 확인했고 원문을 열지 못했으며, 핵심 주장마다 독립 출처로 교차 확인된 것은 없다. q1-07은 실행 2026-09-25-90에서 VDA 5050 공식 GitHub 저장소의 태그별 원문을 열어 조사했다. 조사 결과를 모은 표는 [모델·표준 비교표](model-standard-comparison.md)에, 반영된 개념 변경은 [능력 온톨로지 초안](ontology-draft.md) v0.2에 있다.

### q1-01 로봇 능력·작업을 표현하는 온톨로지·지식 모델 {#q1-01}

로봇 분야의 공통 어휘로는 IEEE(Institute of Electrical and Electronics Engineers)의 표준 계열이 있다. IEEE 1872-2015는 로봇·자동화 분야의 가장 일반적인 개념·관계·공리를 정한 핵심 온톨로지 CORA(Core Ontology for Robotics and Automation)와 보조 온톨로지 CORAX·POS·RPARTS로 구성되며, 상위 온톨로지 SUMO에 연결된다(2015년 발행). [사실][^ref-025] IEEE 1872.2-2021은 CORA를 확장해 자율 로봇(Autonomous Robotics, AuR)의 설계 패턴·시스템 아키텍처를 표현하는 온톨로지 표준이다(2022년 발행). [사실][^ref-026]

로봇이 작업을 추론하는 데 쓰는 지식 모델도 있다. KnowRob 2.0은 Prolog로 구현된 로봇용 지식 처리 프레임워크로, 논리 표현의 일부를 실시간 센서·운동 데이터와 모션 계획 결과에서 필요할 때 만들어 조작 행동을 추론하게 한다(2018년 논문 기준). [사실][^ref-027] SOMA(Socio-physical Model of Activities)는 DUL 기반으로 일상 활동의 물리·사회적 맥락을 표현하는 로봇용 온톨로지이며, 행동·로봇·어포던스·실행 실패를 다루는 하위 온톨로지를 가진다(2021년 논문 기준). [사실][^ref-028]

행동을 계획 문제로 기술하는 모델로는 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)가 있다. PDDL은 1998년 AIPS-98 계획 경진대회를 위해 McDermott 등이 만든 언어로, 파라미터를 가진 행동을 전제조건(precondition)과 효과(effect)로 기술하고 도메인 기술과 문제 인스턴스를 분리한다. [사실][^ref-029] 센서·액추에이터 쪽에서는 W3C(World Wide Web Consortium)와 OGC(Open Geospatial Consortium)의 공동 표준인 Semantic Sensor Network Ontology(SSN)가 2017-10-19 W3C 권고안으로 발행되었고, 경량 핵심 모듈 SOSA와 확장 모듈 SSN으로 센서·액추에이터·샘플러와 관측·작동·샘플링 활동 및 사용된 절차(procedure)를 표현한다. [사실][^ref-030] SSN의 System Capabilities 모듈은 특정 조건(Condition) 아래의 시스템 성능(SystemCapability), 정상 운용 범위(OperatingRange), 손상 없이 견디는 범위(SurvivalRange)를 표현하는 클래스를 둔다. [사실][^ref-030]

후보 밖에서도 두 자료가 확인됐다. Robotic Capability Ontology(RCO)를 제안한 2025년 논문은 로봇 능력을 제조사가 명시한 광고 능력(advertised capability)과 실제 운용 성능을 반영한 운용 능력(operational capability)으로 구분한다. [사실][^ref-041] 자율 로봇의 신뢰성을 위한 온톨로지 활용을 조사한 2024년 서베이는 조사 대상 온톨로지가 주로 행동의 선택·배열(자율성·계획·행위 개념)과 비상 상황 극복(고장·적응 개념)에 관련된다고 정리한다. [사실][^ref-042]

### q1-02 산업 상호운용 규격의 로봇 기능 기술 형식 {#q1-02}

독일자동차산업협회(Verband der Automobilindustrie, VDA)의 VDA 5050 2.0.0(2022년 1월판) 기준으로, 차량은 팩트시트(factsheet) 토픽으로 자신의 기능(차량 유형, 구동 방식 등)을 상위 관제(master control)에 미리 알린다. [추정][^ref-022] 팩트시트는 유형 명세(typeSpecification), 물리 파라미터(physicalParameters), 프로토콜 한계(protocolLimits), 지원 기능(protocolFeatures, 지원 action 목록과 action 범위·결과 설명 포함), 차량 기하(agvGeometry), 적재 명세(loadSpecification) 블록으로 구성되는 것으로 보인다(판 미확인 — GitHub main 브랜치, 구현 라이브러리 문서 혼재). [추정][^ref-031] 이 문장은 실행 2026-09-25-02의 추정이다. 실행 2026-09-25-90에서 공식 저장소 태그의 스키마 원문을 열어 판별 구성을 확인했다: 팩트시트 JSON 스키마의 최상위 필드는 2.1.0과 3.0.0 모두 12개이고, 2.1.0의 agvGeometry·vehicleConfig가 3.0.0에서 mobileRobotGeometry·mobileRobotConfiguration으로 바뀌었다(자세한 비교는 [q1-07](#q1-07), 확인일 2026-09-25). [사실][^ref-044][^ref-045] 2.0.0 기준 상태 메시지는 오류를 유형(errorType)·등급(errorLevel: WARNING 또는 FATAL)·설명·참조로 보고하고, action 완료는 actionStatus 가 finished 로 바뀐 상태 메시지로 알린다. [사실][^ref-022]

VDA 5050은 3.0.0판이 2026년에 발행되어(3.0.0 발행 2026-03, 보도자료 2026-04) 자율도 높은 이동로봇 통합을 위해 인터페이스를 확장했다. [사실][^ref-032] 확장 내용으로 구역(zone) 개념, 경로 공유, 새 오류 등급 CRITICAL·URGENT, 절전 모드 action 추가와 기존 궤적·회랑 방식 유지가 거론되지만, 이 목록은 검색 요약 기준이며 원문 미열람이다. [추정][^ref-032] 공식 저장소 3.0.0 태그의 명세 본문은 AGV 대신 이동로봇(mobile robot) 용어를 쓰고, 팩트시트를 관제–로봇 사이의 필수(mandatory) 토픽으로 둔다(확인일 2026-09-25). [사실][^ref-046] 팩트시트 필드의 판별 변화는 q1-07에 정리했고, 오류 보고·완료 보고 같은 상태 메시지 쪽의 2.0.0 기준 서술이 3.0.0에서 어떻게 바뀌었는지는 미확인이다.

MassRobotics AMR 상호운용 표준 1.0(2021년 5월)은 식별·설정(setup) 메시지와 상태(status) 메시지 두 가지로 제조사·모델, 위치·속도·방향, 상태(health), 작업·가용 상태를 공유하게 한다. [사실][^ref-033] OPC UA(Open Platform Communications Unified Architecture) for Robotics Part 1: Vertical Integration(OPC 40010-1, 판·발행일 미확인)은 VDMA(Verband Deutscher Maschinen- und Anlagenbau)와 OPC Foundation이 만든 동반 규격으로, 모션 장치 시스템(컨트롤러 1대와 모션 장치 1..n대)의 자산 관리·상태 감시 데이터를 상위 시스템(공장 제어·제조 실행 시스템(Manufacturing Execution System, MES)·클라우드)에 제공하는 정보 모델을 정의한다. [사실][^ref-034]

Plattform Industrie 4.0의 능력·스킬·서비스(Capabilities, Skills and Services, CSS) 정보 모델 토론 문서(2022년 11월)는 능력(capability)을 구현과 무관한 기능 명세로, 스킬(skill)을 그 능력의 실행 가능한 구현으로 구분하고 서비스(service)와의 관계를 정한다. [사실][^ref-035][^ref-036] 이 위키의 [능력 온톨로지 초안](ontology-draft.md)에서는 CSS의 능력(capability)을 기능(Capability)으로 부른다. 자산관리셸(Asset Administration Shell, AAS) 쪽에서는 IDTA 02020 Capability Description 서브모델이 능력을 CapabilitySet 안의 CapabilityContainer로 표현하고, 속성(PropertySet), 제약(ConditionContainer), 속성과 스킬 파라미터를 잇는 realizedBy 관계를 두는 것으로 설명된다(IDTA 원문 미열람, 제3자 논문 경유). [추정][^ref-037] Vieira da Silva·Köcher·Fay(2022)는 제조 분야의 능력·스킬 모델을 이종 자율 로봇 팀에 적용·확장하고, AAS 서브모델과 능력·스킬 온톨로지 사이의 양방향 매핑 개념을 제시했다. [사실][^ref-038] 국내에서는 신민종·한영석·정재윤의 논문 「자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계」가 한국전자거래학회지 29권 4호 203-213쪽(2024)에 게재되었다(논문 본문 내용은 미확인). [사실][^ref-043]

Open-RMF는 청소(Clean)·배송(Delivery)·순회(Loop) 작업 유형을 지원하며, 플릿 어댑터 설정의 작업 능력(task capabilities) 항목으로 플릿이 수행할 수 있는 작업 유형을 선언한다(확인일 2026-09-25). [사실][^ref-039] 플릿 어댑터는 설정 파일에 수행 가능한 사용자 정의 동작(performable actions) 목록을 둘 수 있고, 해당 동작이 배정되면 execute_action 콜백이 호출되며 RMF는 완료 신호를 받을 때까지 로봇 제어를 어댑터에 넘긴다(확인일 2026-09-25). [사실][^ref-040]

### q1-03 ROP가 필요로 하는 다섯 정보의 담김 정도 (부분 답)

후보별로 다섯 정보 항목(전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미)의 충족 정도는 대부분 원문으로 확인하지 못해 항목별 판정표를 만들지 않았다. 아래는 주로 검색 요약에서 끌어낸 질적 추론이며, VDA 5050 팩트시트만 실행 2026-09-25-90에서 3.0.0 스키마 원문으로 보강했다.

조사한 모델 가운데 전제조건·효과는 PDDL이, 파라미터와 제약은 SSN 운용 범위가, 적재 제약은 VDA 5050 팩트시트 적재 명세가 각각 일부씩 담는 것으로 보이며, 다섯 정보 항목을 한 모델이 모두 담는 경우는 검색 범위에서 확인되지 않았다. [추정][^ref-029][^ref-030][^ref-031][^ref-044] VDA 5050 3.0.0 팩트시트 스키마에서는 적재 세트별 최소·최대 범위와 단위(파라미터 범위·적재 제약), 처리 가능한 구역 유형 선언(환경 제약), action별 결과 설명과 일시정지·취소 가능 여부를 확인했다([q1-07](#q1-07)). [사실][^ref-044] IDTA 02020 능력 서브모델의 제약(ConditionContainer)도 파라미터·제약의 일부를 담을 수 있는 것으로 보이나, 이 판단은 IDTA 원문이 아닌 제3자 논문 경유의 추정에 기댄다. [추정][^ref-037]

오류의 의미를 구조화해 담는 것은 SOMA의 실행 실패 하위 온톨로지와 VDA 5050(2.0.0 기준)의 오류 등급 정도이고, 능력 기술 안에 완료 확인 방법을 명시하는 항목은 조사한 모델에서 확인되지 않았다. [추정][^ref-028][^ref-022] VDA 5050 3.0.0 팩트시트는 action마다 결과 설명(actionResult)을 두지만 그 값은 자유 문장이어서, 완료 확인 방법을 구조화해 담는다고 보기는 어렵다. [추정][^ref-044] Open-RMF의 능력 선언은 작업 유형과 이름 붙은 사용자 정의 동작 수준에 머물러, 선언 자체에는 전제조건·파라미터 범위·오류의 의미가 담기지 않고 완료 판정은 어댑터 구현이 보내는 완료 신호에 맡겨지는 것으로 보인다(검색 범위 한정). [추정][^ref-039][^ref-040] OPC 40010-1은 자산 관리·상태 감시가 목적이어서, ROP의 작업 배정에 필요한 작업 단위 능력과 그 전제조건·완료 확인 방법은 이 규격의 범위 밖에 있을 가능성이 높다(Part 2 이후 부의 범위는 미확인). [추정][^ref-034]

단계 1의 시사점으로, 매뉴얼에서 가져온 능력 정보는 RCO의 구분으로는 제조사가 명시한 광고 능력에 해당하므로, ROP가 배정에 쓰려면 현장 운용 성능(운용 능력)으로 보완·검증하는 절차가 필요할 것으로 보인다. [추정][^ref-041] 이 추정은 트랙 가설 1의 판정 근거로 쓰지 않는다.

### q1-07 VDA 5050 팩트시트 필드의 판별 변화와 적재 제약 필드 {#q1-07}

실행 2026-09-25-90은 일반 웹 페이지 열람이 막힌 환경에서 VDA 5050 공식 GitHub 저장소의 태그별 원문(2.0.0·2.1.0·3.0.0)만 열어 확인했다. 원문은 열었지만 모든 출처가 같은 기관(VDA/VDMA)의 판별 산출물이어서 독립 출처 교차 확인은 0건이다. 문서에 발행일 표기가 없어 아래 사실의 기준일은 확인일 2026-09-25다.

**비교 기준.** 공식 저장소 2.0.0 태그에는 팩트시트 JSON 스키마 파일이 없어(HTTP 404) 질문의 "2.0 대비" 비교는 2.1.0 스키마 대비로 대신했고, 2.0.0의 적재 세트 필드는 미확인이다. [사용자 실험] 3.0.0 명세 본문은 팩트시트를 관제–로봇 사이의 필수 토픽으로 두고 그 구현을 7.10절에서 정한다. [사실][^ref-046] 2.1.0 명세는 6.15절 Topic "factsheet"에서 팩트시트를 정의한다. [사실][^ref-047] 공식 저장소 2.0.0 태그의 명세 마크다운은 7장 AGV Factsheet에서 팩트시트를 AGV 유형 시리즈의 기본 정보로 정의하고, AGV가 factsheet 하위 토픽으로 이를 알려야 한다고 적는다(공식 저장소 2.0.0 태그의 RELEASE CANDIDATE 문서 기준, VDA 게시 PDF([ref-022](../../references/ref-022.md))와 동일성 미확인). [사실][^ref-048]

**최상위 구조.** 팩트시트 스키마의 최상위 필드는 2.1.0과 3.0.0 모두 12개다. 2.1.0의 agvGeometry·vehicleConfig가 3.0.0에서 mobileRobotGeometry·mobileRobotConfiguration으로 바뀌었고, 나머지 10개(headerId, timestamp, version, manufacturer, serialNumber, typeSpecification, physicalParameters, protocolLimits, protocolFeatures, loadSpecification)는 이름이 같다. [사실][^ref-044][^ref-045]

**유형 명세.** 3.0.0 유형 명세(typeSpecification)는 시리즈 이름·설명, 기구학(mobileRobotKinematics: DIFFERENTIAL·OMNIDIRECTIONAL·THREE_WHEEL), 로봇 분류(mobileRobotClass: FORKLIFT·CONVEYOR·TUGGER·CARRIER), 최대 적재 질량(maximumLoadMass, kg), 위치추정·주행 방식(localizationTypes·navigationTypes), 지원 구역(supportedZones)을 둔다. 2.1.0의 같은 자리에는 agvKinematic(DIFF·OMNI·THREEWHEEL), agvClass, maxLoadMass가 있었고 supportedZones는 없었다. [사실][^ref-044][^ref-045] supportedZones는 로봇이 처리할 수 있는 구역 유형 10가지(BLOCKED, LINE_GUIDED, RELEASE, COORDINATED_REPLANNING, SPEED_LIMIT, ACTION, PRIORITY, PENALTY, DIRECTED, BIDIRECTED)를 선언하게 한다. [사실][^ref-044]

**적재 제약.** 3.0.0 팩트시트는 적재 제약을 loadSpecification.loadSets[]의 적재 세트마다 기술한다. 세트마다 세트 이름(setName), 적재 유형(loadType, 예: EPAL), 적용 적재 장치(loadPositions, 비어 있으면 모든 적재 장치에 적용), 기준 경계 상자(boundingBoxReference), 적재 치수(loadDimensions: 길이·폭 필수, 높이 선택), 최대 중량(maximumWeight, kg), 취급 높이·깊이의 최소·최대(m), 취급 기울기의 최소·최대(rad), 적재 시 최대 속도·가속·감속(maximumSpeed·maximumAcceleration·maximumDeceleration), 적재·하역 소요 시간(pickTime·dropTime, s), 설명을 둔다. [사실][^ref-044] 적재 세트의 필수 필드는 setName·loadType 둘뿐이다. [사실][^ref-044] 스키마는 적재 세트 maximumSpeed의 단위를 "m/s^2"로 적고 있어 이 위키는 이를 m/s로 바꾸지 않고 원문 그대로 두며, maximumDeceleration에는 단위 표기가 없다. [사실][^ref-044] 속도 필드에 가속도 단위를 적은 것은 스키마의 표기 오류로 보인다. [추정][^ref-044]

2.1.0 스키마의 loadSets[]도 같은 구조로 setName, loadType, loadPositions, boundingBoxReference, loadDimensions, maxWeight(kg), 취급 높이·깊이·기울기의 최소·최대(min/maxLoadhandlingHeight·Depth·Tilt), agvSpeedLimit·agvAccelerationLimit·agvDecelerationLimit, pickTime, dropTime, description을 두고, 유형 명세에는 maxLoadMass(kg)가 있다. [사실][^ref-045] 두 판을 대조하면 적재 제약 필드는 구조가 유지된 채 이름만 바뀐 것으로 보이며(max* → maximum*/minimum*, agvSpeedLimit·agvAccelerationLimit·agvDecelerationLimit → maximumSpeed·maximumAcceleration·maximumDeceleration, maxLoadMass → maximumLoadMass), 적재 세트에 새 종류의 제약 필드가 더해진 것은 대조 범위에서 확인되지 않았다. 이름이 바뀐 필드의 설명문·단위·필수 여부가 같은지는 확인하지 않았다(후속 질문 q1-09). [추정][^ref-044][^ref-045]

**지원 action.** 3.0.0 지원 action 목록(protocolFeatures.mobileRobotActions)은 action마다 유형(actionType), 설명(actionDescription), 적용 범위(actionScopes: INSTANT·NODE·EDGE·ZONE), 파라미터(key·valueDataType·description·isOptional), 결과 설명(actionResult), 차단 유형(blockingTypes: NONE·SOFT·SINGLE·HARD), 일시정지 가능 여부(pauseAllowed), 취소 가능 여부(cancelAllowed)를 둔다. 2.1.0의 agvActions에는 결과 설명(resultDescription)과 적용 범위 3종(INSTANT·NODE·EDGE)·차단 유형 3종(NONE·SOFT·HARD)이 있었고 pauseAllowed·cancelAllowed는 없었다. [사실][^ref-044][^ref-045] 3.0.0에서 pauseAllowed는 startPause로 그 action을 일시정지할 수 있는지, cancelAllowed는 cancelOrder로 취소할 수 있는지를 나타내며, 명세 본문은 pauseAllowed가 true인 action만 일시정지된다고 적는다. [사실][^ref-044][^ref-046]

**충전 설정.** 3.0.0 팩트시트는 mobileRobotConfiguration 아래 충전 설정(batteryCharging)으로 임계 저충전량(criticalLowChargingLevel, %, 이 값 이하이면 관제가 로봇을 충전으로 보낸다), 최저·최고 희망 충전량(%), 최소 충전 시간(minimumChargingTime, s)을 기술하게 한다. 원 스키마의 키 이름은 끝에 공백이 붙어 있다. 2.1.0의 vehicleConfig에는 이 항목이 없었다. [사실][^ref-044][^ref-045]

**2.0.0 명세 본문.** 2.0.0 태그 명세의 팩트시트 블록은 typeSpecification, physicalParameters, protocolLimits, protocolFeatures, agvGeometry, loadSpecification(적재 능력의 추상 명세) 등으로 설명되고 vehicleConfig는 보이지 않아, vehicleConfig는 2.1.0 이후 항목일 가능성이 있다. 열람 본문이 잘려 이 블록 목록은 완결 목록이 아니며, 공식 저장소 2.0.0 태그의 RELEASE CANDIDATE 문서 기준이어서 VDA 게시 PDF([ref-022](../../references/ref-022.md))와의 동일성은 미확인이다. [추정][^ref-048]

**사용자 실험.** 사용자 실험 `experiments/2026-09-25-vda5050-factsheet-field-diff/`는 2.1.0과 3.0.0 팩트시트 스키마의 필드 경로를 재귀로 비교해 경로 수 132개 대 144개, 3.0.0에만 있는 경로 104개·2.1.0에만 있는 경로 92개(대부분 이름 변경)를 보고했고, 2.0.0 태그에는 스키마 파일이 없어 2.1.0 대비로 비교했다. [사용자 실험] 경로 수는 이번 실행의 리서치·검증에서 재계산하지 않았다. 실험이 보고한 최상위 필드와 새 필드(supportedZones, actionResult·pauseAllowed·cancelAllowed, batteryCharging)는 공식 스키마 원문과 일치했다. [사실][^ref-044][^ref-045]

**ROP 관점.** 3.0.0 팩트시트의 적재 세트 필드는 같은 운반 로봇 가운데 누가 이 화물을 취급할 수 있는지를 판정할 재료(적재 유형별 중량·치수·취급 높이·기울기 범위, 적재 시 속도 한계, 적재·하역 시간)를 제조사 선언값으로 제공하므로, ROP 능력 온톨로지에서 적재 유형에 묶인 제약(최소·최대 범위와 단위)으로 옮길 수 있을 것으로 보인다. 값은 제조사가 채우는 광고 능력이며 현장 검증 여부는 별개다. [추정][^ref-044] 이 판단에 근거해 [능력 온톨로지 초안](ontology-draft.md)의 제약 개념에 속성 후보를 더했다(v0.2).

## 4. 결론과 남은 불확실성

**결론**

- 로봇 능력을 표현하는 기존 모델로 IEEE 1872 계열 온톨로지, KnowRob·SOMA, PDDL, W3C SSN/SOSA가 확인됐고, 각각 공통 개념·관계, 조작 행동 추론·활동 맥락, 행동의 전제조건·효과, 센서·작동과 운용 범위를 표현한다. [사실][^ref-025][^ref-026][^ref-027][^ref-028][^ref-029][^ref-030]
- CSS 모델은 능력(구현 독립 명세)과 스킬(실행 가능한 구현)을 구분한다. [사실][^ref-035][^ref-036]
- 산업 규격 쪽 기능 기술은 VDA 5050 팩트시트(2.0.0 기준), Open-RMF 작업 유형·사용자 정의 동작 선언처럼 관제 연동 메시지·설정 안에 들어 있다. [추정][^ref-022][^ref-039][^ref-040] MassRobotics AMR 상호운용 표준 1.0은 setup·status 메시지로 제조사·모델, 위치·속도·방향, 상태, 작업·가용 상태를 공유하게 한다. [사실][^ref-033] 이 메시지에 로봇 능력을 기술하는 필드가 있는지는 미확인이다(후속 질문 q1-08).
- VDA 5050 3.0.0 팩트시트는 적재 제약을 loadSpecification.loadSets[]의 적재 세트마다 최소·최대 범위와 단위로 기술하고, 2.1.0 대비 supportedZones, action별 actionResult·pauseAllowed·cancelAllowed, 충전 설정 batteryCharging이 더해졌다(공식 저장소 스키마 원문, 확인일 2026-09-25). [사실][^ref-044][^ref-045]
- 다섯 정보 항목을 한 모델이 모두 담는 경우는 검색 범위에서 확인되지 않았다. [추정][^ref-029][^ref-030][^ref-031]
- [능력 온톨로지 초안](ontology-draft.md)은 실행 2026-09-25-02에서 v0 → v0.1(효과·스킬·오류 개념, "기능 / 구현된다 / 스킬" 관계, 기능의 능력 출처 구분 속성), 실행 2026-09-25-90에서 v0.1 → v0.2(제약 개념에 적용 대상·최소값·최대값·단위 속성 후보를 더하고 확정)로 올랐다.

**남은 불확실성**

- 실행 2026-09-25-02의 출처는 모두 원문 미열람이다. 실행 2026-09-25-90의 VDA 5050 공식 저장소 출처는 원문을 열었으나 같은 기관의 판별 산출물이라 교차 확인은 0건이다.
- q1-03 부분 답: 후보별로 다섯 정보 항목의 충족 정도를 원문으로 확인한 것은 VDA 5050 팩트시트(3.0.0 스키마)뿐이어서 항목별 판정표를 만들 근거가 아직 없다.
- VDA 5050 팩트시트: 공식 저장소 2.0.0 태그에는 팩트시트 스키마가 없어(404) 비교 기준은 2.1.0이며, 2.0.0의 적재 세트 필드는 미확인이다. 2.0.0 태그 명세는 RELEASE CANDIDATE 문서여서 VDA 게시 PDF(ref-022)와 동일성이 미확인이다.
- 2.1.0→3.0.0에서 이름이 바뀐 팩트시트 필드의 설명문·단위·필수 여부 동일성은 미확인이다(q1-09). 적재 세트 속도 필드의 가속도 단위 표기가 표기 오류인지는 원문만으로 판단할 수 없다.
- 3.0.0 명세 7.10절 팩트시트 본문과 2.1.0 명세 6.15절의 필드 표는 열람 본문이 잘려 확인하지 못했고, 필드는 스키마로만 확인했다.
- VDA 5050 3.0.0의 정확한 발행일이 미확인이다. 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 260421 계열이다. 공식 저장소 3.0.0 명세에도 발행일 표기가 없다. 3.0.0의 기능 목록 가운데 상태 메시지 쪽 변경도 원문으로 확인하지 못했다.
- 온톨로지 v0.2에는 제약 수정만 반영했다. 기능에 일시정지·취소 가능 여부와 결과 설명을 더하는 제안은 기존 기능 정의와 충돌하고, 실행 조건에 임계 저충전량 예를 더하는 제안은 실행 조건·제약 경계 질문을 선취해 반영하지 않고 초안 6절 질문으로 두었다.
- MassRobotics setup·status 메시지의 필드 목록과 2.0의 현재 상태는 미확인이다.
- CSS 계열 스킬의 FeasibilityCheck·PreconditionCheck 설명은 출처 미확정이다.
- IDTA 02020 서브모델 구조는 IDTA 원문이 아니라 제3자 논문 경유로만 확인했다.
- OPC 40010-1의 판·발행일과 Part 2 이후 부의 범위는 미확인이다.
- 국내 논문(신민종·한영석·정재윤, 2024)은 게재 사실만 확인했고 본문 내용은 미확인이다.
- ref-031·ref-034·ref-039·ref-040·ref-044~ref-048의 발행일은 미확인이다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q1-07 | VDA 5050 3.0에서 팩트시트(유형 명세·적재 명세·지원 action)의 필드가 2.0 대비 어떻게 바뀌었으며, 적재 제약을 어떤 필드로 기술하는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f12 (실행 2026-09-25-02) | 답함 |
| q1-08 | MassRobotics AMR 상호운용 표준의 setup·status 메시지 스키마에는 로봇 능력(적재량, 지원 작업, 부착 장비)을 기술하는 필드가 있는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f13 (실행 2026-09-25-02) | 열림 |
| q4-06 | IDTA 02020 능력 서브모델의 속성·제약(ConditionContainer)과 VDA 5050 팩트시트의 적재 명세·지원 action 을 서로 매핑할 수 있는가, 매핑하면 무엇이 남는가? | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f17 (실행 2026-09-25-02) | 열림 |
| q5-05 | 제조사 매뉴얼에서 추출한 광고 능력과 현장 시험으로 확인한 운용 능력의 차이를 어떤 지표로 측정하고 온톨로지에 함께 기록할 것인가? | 단계 5. 완전성과 정확성을 검증하는 방법 조사 | f27 (실행 2026-09-25-02) | 열림 |
| q1-09 | q1-07 후속: VDA 5050 2.1.0→3.0.0에서 이름이 바뀐 팩트시트 필드(예: agvSpeedLimit→maximumSpeed, maxWeight→maximumWeight)는 설명문·단위·필수 여부까지 같은가, 의미가 바뀐 필드가 있다면 기존 2.x 로봇의 팩트시트를 3.0 능력 모델로 옮길 때 무엇을 다시 확인해야 하는가? | 단계 1. 기존 능력 표현 모델과 표준 조사 | f4 (실행 2026-09-25-90) | 열림 |

같은 질문은 [질문 백로그](question-backlog.md)에 등록된다(백로그 반영은 퍼블리셔가 한다).

## 6. 완료 조건 충족 현황

완료 조건은 트랙 정의의 문장을 옮기되 파일명은 페이지 링크로 바꾸고, 조건이 여러 항목이면 행을 나눴다. 트랙 정의의 문장은 아래 인용 블록에 그대로 두었고, [트랙 개요](index.md)의 단계 진행 현황 표에도 같은 조건이 링크를 붙인 형태로 있다. 충족 여부는 리서치 에이전트의 자체 평가(research.json 의 track 블록)를 스토리텔러 에이전트가 옮겨 적은 값이고, 최종 판정은 내용 검증 에이전트가 한다. 둘이 다르면 검증 판정을 따른다.

> 완료 조건: 모델·표준 비교표(`model-standard-comparison.md`) 작성, ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 반영됨.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 모델·표준 비교표([model-standard-comparison.md](model-standard-comparison.md)) 작성 | 미충족 | [모델·표준 비교표](model-standard-comparison.md)에 후보 10행의 발행 기관·종류를 채우고 후보 밖 2행을 더했으며, 실행 2026-09-25-90에서 VDA 5050 행의 정보 항목 칸을 3.0.0 스키마 원문 근거로 고쳤다. VDA 5050 행 외의 다섯 정보 항목 열은 대부분 미조사다 | 미충족 · 미승인 |
| ROP용 능력 개념 요구 목록 초안이 온톨로지 초안에 반영됨 | 미충족 | [능력 온톨로지 초안](ontology-draft.md) v0.2에 효과·스킬·오류 개념, 기능·제약 속성 수정이 반영됐으나, q1-06을 조사하지 않아 요구 목록 초안은 없다 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(모델·표준 비교표의 다섯 정보 항목 열이 VDA 5050 행 외 대부분 미조사, ROP용 능력 개념 요구 목록 초안 미반영 — q1-06 미조사, 막힌 질문 q1-03(조사 중), q1-04, q1-05, q1-06, q1-08)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 각 항목 뒤에는 이 단계에서 확인된 사실을 그 영역 페이지의 어느 절에 반영하자고 제안할지를 적었다. 반영 제안은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안" 항목으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

**중심 영역**

- [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 트랙이 출발하는 영역이다. 실행 2026-09-25-02에서 "4. 핵심 개념과 용어"(능력·스킬 구분, 전제조건·효과, 광고 능력·운용 능력), "7. 관련 표준·프레임워크·오픈소스"(IEEE 1872 계열, SSN/SOSA, CSS, IDTA 02020), "8. 대표 연구와 자료"(KnowRob·SOMA, RCO, 서베이, 국내 논문) 절에 반영을 제안했다. 실행 2026-09-25-90에서는 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 3.0.0 팩트시트의 적재 세트·유형 명세·지원 action 기술을 능력 기술 표준 사례로 반영하자고 제안했다.

**연구 방법으로 연결되는 영역(분류 원문 8장의 교차 규칙)**

- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 매뉴얼 해석은 이 영역의 방법이 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 것으로 다룬다. 단계 1에서는 기존 모델·표준이 AI가 해석한 기능 정보(신뢰도, 근거 위치)를 담을 자리를 갖는지의 관점으로 연결한다. 실행 2026-09-25-02와 2026-09-25-90에서는 이 영역에 해당하는 발견 사항이 없어 반영 제안을 내지 않았다.

**이 단계의 질문이 언급하는 영역(트랙 개요의 배정에 따른 추가 연결, [가정])**

- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — q1-04(능력 기술과 실행 인터페이스의 연결)와 q1-02의 Open-RMF Fleet Adapter 후보가 이 영역의 어댑터 문제에 닿는다. 실행 2026-09-25-02에서 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 팩트시트·오류 보고, MassRobotics 메시지, Open-RMF 작업 능력·사용자 정의 동작의 반영을 제안했다. 실행 2026-09-25-90에서는 같은 절에 VDA 5050 3.0.0의 팩트시트 필수 토픽, 2.1.0→3.0.0 필드 이름 변경(어댑터의 판 판별에 영향), pauseAllowed·cancelAllowed의 반영을 제안했다.
- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — q1-02의 산업 상호운용 규격 조사가 이 영역의 공통 규격·적합성 시험에 닿는다. 실행 2026-09-25-02에서 "7. 관련 표준·프레임워크·오픈소스" 절에 능력 기술 관련 표준·규격의 발행 기관과 현재 판의 반영을 제안했다.

**확장 아이디어 1의 범위 능력으로 연결되는 영역([가정])**

- [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) — 범위 능력 "충전". 실행 2026-09-25-90에서 "7. 관련 표준·프레임워크·오픈소스" 절에 VDA 5050 3.0.0 팩트시트의 충전 설정(임계 저충전량, 희망 충전량 범위, 최소 충전 시간)의 반영을 제안했다.

## 8. 출처

[^ref-022]: VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control, 2022-01, https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-025]: IEEE, 1872-2015 - IEEE Standard Ontologies for Robotics and Automation, 2015, https://ieeexplore.ieee.org/document/7084073/, 접근일 2026-09-25 (원문 미열람)
[^ref-026]: IEEE, IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology, 2022, https://standards.ieee.org/standard/1872_2-2021.html, 접근일 2026-09-25 (원문 미열람)
[^ref-027]: Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G., KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents, 2018, https://ai.uni-bremen.de/papers/beetz18knowrob.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-028]: Beßler, D. 외, Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents, 2021, https://arxiv.org/pdf/2011.11972, 접근일 2026-09-25 (원문 미열람)
[^ref-029]: McDermott, D. 외, PDDL - The Planning Domain Definition Language, 1998, https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language, 접근일 2026-09-25 (원문 미열람)
[^ref-030]: W3C / OGC, Semantic Sensor Network Ontology, 2017-10-19, https://www.w3.org/TR/vocab-ssn/, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25 (원문 미열람)
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-09-25 (원문 미열람)
[^ref-033]: MassRobotics, Autonomous Mobile Robot Standards Published by MassRobotics, 2021-05, https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/, 접근일 2026-09-25 (원문 미열람)
[^ref-034]: OPC Foundation / VDMA, OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration, 미확인, https://reference.opcfoundation.org/specs/OPC-40010-1, 접근일 2026-09-25 (원문 미열람)
[^ref-035]: Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services, 2022-11, https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html, 접근일 2026-09-25 (원문 미열람)
[^ref-036]: Köcher, A. 외, A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing, 2022, https://arxiv.org/abs/2209.09632, 접근일 2026-09-25 (원문 미열람)
[^ref-037]: Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A., Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies, 2023-07, https://arxiv.org/abs/2307.00827, 접근일 2026-09-25 (원문 미열람)
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-25 (원문 미열람)
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25 (원문 미열람)
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-042]: Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R., A survey of ontology-enabled processes for dependable robot autonomy, 2024-07, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full, 접근일 2026-09-25 (원문 미열람)
[^ref-043]: 신민종, 한영석, 정재윤, 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계, 2024, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560, 접근일 2026-09-25 (원문 미열람)
[^ref-044]: VDA / VDMA (VDA5050 GitHub), VDA5050/json_schemas/factsheet.schema (tag 3.0.0) — Mobile Robot Factsheet, 미확인, https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-045]: VDA / VDMA (VDA5050 GitHub), VDA5050/json_schemas/factsheet.schema (tag 2.1.0) — AGV Factsheet, 미확인, https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-046]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md (tag 3.0.0) — VDA 5050 Version 3.0.0 specification, 미확인, https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md, 접근일 2026-09-25
[^ref-047]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md (tag 2.1.0) — VDA 5050 Version 2.1.0 specification, 미확인, https://github.com/VDA5050/VDA5050/blob/2.1.0/VDA5050_EN.md, 접근일 2026-09-25
[^ref-048]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN_V1.md (tag 2.0.0) — VDA 5050 Version 2.0.0, 미확인, https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md, 접근일 2026-09-25

## 9. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 온톨로지 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-90 | q1-07 | q1-09 | v0.1 → v0.2 | 3 |
| 2026-09-25 | 2026-09-25-02 | q1-01, q1-02(q1-03 부분 답) | q1-07, q1-08, q4-06, q5-05 | v0 → v0.1 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 없음 | 시드 q1-01~q1-06(6건, 구축 시 [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [능력 온톨로지 초안](ontology-draft.md)에서 생성) | 1 |
