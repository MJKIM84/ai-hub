---
title: "모델·표준 비교표"
type: track
subtype: comparison
track: manual-capability-ontology
related_areas: [5, 9, 28]
tags: [모델·표준 비교표, 능력 온톨로지, 산업 상호운용 규격, 단계 1 산출물]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-022, ref-025, ref-026, ref-027, ref-028, ref-029, ref-030, ref-031, ref-032, ref-033, ref-034, ref-035, ref-036, ref-037, ref-038, ref-039, ref-040, ref-041, ref-051, ref-228, ref-229, ref-243, ref-231, ref-230, ref-244, ref-245, ref-250, ref-323, ref-329, ref-235, ref-324, ref-325, ref-330, ref-326, ref-391, ref-392]
last_run: 2026-09-25
version: 5
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 모델·표준 비교표

# 모델·표준 비교표

> 산출 단계: [단계 1. 기존 능력 표현 모델과 표준 조사](stage-1-existing-models-and-standards.md) · 상태: 초안 · 조사된 후보: 10 / 10(후보 밖 5행 추가. 산업 규격·서브모델·오픈소스 행은 일부 원문 열람, 학술 온톨로지 행은 제3자 구현·작업반 편집본·공식 저장소 원문 열람, PDDL 행은 원문 미열람) · 마지막 실행: 2026-09-25

## 1. 목적과 쓰임

이 페이지는 중점 연구 트랙 [매뉴얼 기반 로봇 기능 온톨로지](index.md)의 단계 1 산출물이다. 로봇의 능력·스킬·작업을 표현하는 기존 온톨로지(ontology)·지식 모델과 산업 상호운용 규격이, 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP)이 배정·실행·검증에 필요로 하는 정보를 얼마나 담는지를 같은 열로 비교한다.

단계 1의 완료 조건 첫 항목("모델·표준 비교표 작성")이 이 표다. 표에서 드러난 빠진 정보는 ROP용 능력 개념 요구 목록 초안의 입력이 되고, 요구 목록 자체는 근거 finding id와 함께 [능력 온톨로지 초안](ontology-draft.md)에 반영된다.

구축 시점에는 빈 틀이다. 단계 1 트랙 실행에서 스토리텔러 에이전트가 내용 검증 에이전트의 승인을 받은 발견 사항만으로 채운다. 이후 단계에서도 보강할 수 있다. 예를 들어 단계 4(온톨로지를 실행에 연결하는 방법 조사)의 능력→명령 매핑 결과는 "실행 인터페이스 연결" 열을, 단계 6(변경 관리·운영·거버넌스 조사)의 표준·책임 조사는 "출처"와 "상태" 열을 보강할 수 있다. [가정]

## 2. 비교 대상 후보

행의 열 개는 트랙 정의에 있는 단계 1의 시작 질문 q1-01과 q1-02가 괄호 안에 든 후보를 그대로 옮긴 것이다. 후보는 리서치 에이전트가 실재·최신성(발행 기관, 현재 버전, 대체·폐기 여부, 원문 접근 가능 여부)을 확인해야 할 조사 대상이지, 확인된 출처가 아니다. 이 페이지의 어떤 행도 그 모델·표준이 실재하거나 현재 유효하다는 주장이 아니다. 후보 이름 속 약어(IEEE, PDDL, W3C, VDA, OPC UA 등)는 트랙 정의의 후보 이름 그대로 두며, 실재를 확인한 뒤 발행 기관의 공식 명칭으로 풀어 쓴다(6절). 후보 이름 속 AMR은 자율이동로봇(Autonomous Mobile Robot, AMR)을 뜻한다.

확인 결과 실재하지 않거나, 다른 것으로 대체되었거나, 트랙 범위 밖이면 행을 지우지 않고 상태를 "제외"로 바꾸고 이유를 적는다. 후보 밖의 모델·표준이 조사에서 나오면 근거 finding id와 함께 행을 추가할 수 있다. [가정]

두 질문의 원문은 [단계 1. 기존 능력 표현 모델과 표준 조사](stage-1-existing-models-and-standards.md)의 2절과 [질문 백로그](question-backlog.md)에 있다.

## 3. 열의 뜻

비교 열 가운데 전제조건, 파라미터 범위, 적재·환경 제약, 완료 확인 방법, 오류의 의미 다섯 개는 시작 질문 q1-03이 "ROP가 배정·실행·검증에 필요로 하는 정보"로 든 항목을 그대로 열 이름으로 쓴 것이다. 나머지 열(후보, 제시한 질문, 발행 기관, 종류, 실행 인터페이스 연결, 출처, 상태)은 행을 식별하고 근거를 남기기 위한 것이다. 열은 모두 12개다. 각 열의 뜻과 값은 구축자가 정했다. [가정]

| 열 | 뜻 | 값 |
|---|---|---|
| 후보 | 비교 대상 모델·표준의 이름. 2절의 후보 목록과 같다 | 트랙 정의의 후보 이름. 조사 후 공식 명칭으로 고쳐 쓰면 원래 이름을 괄호로 남긴다(6절) |
| 제시한 질문 | 이 후보를 든 시작 질문의 id | q1-01 / q1-02 |
| 발행 기관 | 모델·규격을 발행하거나 유지하는 기관·프로젝트 | 기관명. 확인 전에는 "미조사" |
| 종류 | 온톨로지, 지식 모델, 행동 모델, 산업 규격, 오픈소스 인터페이스 등 | 확인 전에는 "미조사" |
| 전제조건 | 기능을 실행하기 전에 충족돼야 하는 조건을 표현하는가, 어떤 형식인가 | 담음(형식) / 부분(무엇이 빠지는지) / 없음 / 미조사 |
| 파라미터 범위 | 기능의 파라미터와 허용 범위(값·단위)를 표현하는가 | 같음 |
| 적재·환경 제약 | 적재량·치수·바닥·경사·온도 같은 적재·환경 제약을 표현하는가 | 같음 |
| 완료 확인 방법 | 기능 수행의 완료를 무엇으로 확인하는지 표현하는가 | 같음 |
| 오류의 의미 | 오류·실패 상태와 그 의미(원인, 복구 가능성)를 표현하는가 | 같음 |
| 실행 인터페이스 연결 | 능력 기술이 명령·상태 인터페이스와 어떻게 이어지는가(q1-04) | 짧은 설명. 확인 전에는 "미조사" |
| 출처 | 발행 기관의 공식 자료 각주 id. 원문을 못 열었으면 "원문 미열람" 병기 | `[^ref-NNN]` 형식 |
| 상태 | 행의 조사 상태 | 미조사 / 조사 중 / 확인 / 원문 미열람 / 제외(이유) |

## 4. 비교표

| 후보 | 제시한 질문 | 발행 기관 | 종류 | 전제조건 | 파라미터 범위 | 적재·환경 제약 | 완료 확인 방법 | 오류의 의미 | 실행 인터페이스 연결 | 출처 | 상태 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IEEE 1872 CORA | q1-01 | IEEE | 온톨로지 표준(1872-2015, 핵심 온톨로지 CORA와 보조 온톨로지 CORAX·POS·RPARTS) [사실]. 공개 OWL 번역(cora-bare.owl, 제3자, IEEE 표준 본문 아님)은 Robot·RoboticSystem 등 7개 클래스, 부품 관계(robotPart), 로봇 환경이 로봇 시스템을 갖춘다는 관계(equippedWith), 자율성 수준 속성을 둠 [사실] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 미조사 | [^ref-025][^ref-330] | 확인(제3자 구현/편집본 원문 열람). IEEE 표준 원문은 미열람 |
| IEEE 1872.2 자율 로봇 온톨로지 | q1-01 | IEEE | 온톨로지 표준(1872.2-2021, 2022년 발행, CORA 확장) [사실]. 헬무트 슈미트 대학의 OWL 구현(제3자, IEEE 표준 본문 아님)은 기능·기능 실행, 행동 분류, 물리·정보 상호작용, 환경 기술 클래스와 isPlayedBy 속성을 둠 [사실] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 미조사 | [^ref-026][^ref-325] | 확인(제3자 구현/편집본 원문 열람). IEEE 표준 원문은 미열람 |
| KnowRob·SOMA | q1-01 | Beetz 외(KnowRob 2.0 논문, 2018)·KnowRob 공식 저장소 / Beßler 외(SOMA 논문, 2021)·EASE CRC | 지식 처리 프레임워크(KnowRob) / 활동 온톨로지(SOMA) [사실]. KnowRob 2.0(2018 논문)은 Prolog 구현 [사실], 현재 dev 브랜치는 RDF·OWL 기반 하이브리드 지식 베이스이며 C++ 구현·Prolog 선택 지원 [사실] | SOMA: 담음(형식): 요구 초기 상황(hasRequiredInitialSituation) [사실] / KnowRob: README 범위에서 판정 불가 — SOMA 행 참조 | SOMA: 없음(열람 파일 기준, 부재 확정 아님) [추정] / KnowRob: README 범위에서 판정 불가 — SOMA 행 참조 | SOMA: 없음(열람 파일 기준, 부재 확정 아님) [추정] / KnowRob: README 범위에서 판정 불가 — SOMA 행 참조 | SOMA: 담음(형식): 기대 종료 상황(hasExpectedTerminalSituation)과 실행 상태 Succeeded [사실] / KnowRob: README 범위에서 판정 불가 — SOMA 행 참조 | SOMA: 부분: 실행 상태 Failed, 충족되지 않은 사후조건 같은 기대 불일치 상황(NonmanifestedSituation) [사실], 실행 실패 하위 온톨로지(2021 논문) [추정] / KnowRob: README 범위에서 판정 불가 — SOMA 행 참조 | 미조사 | [^ref-027][^ref-028][^ref-324][^ref-326] | 확인(SOMA-ACT·KnowRob README 공식 저장소 원문 열람). 2018·2021 논문은 원문 미열람 |
| PDDL 계열 행동 모델 | q1-01 | McDermott 등(AIPS-98 계획 경진대회용, 1998) | 행동 계획 언어 [사실] | 담음(형식): 행동의 전제조건·효과 [사실]. ROP 요구 대비 충족 정도는 미확인 | 부분: 행동 파라미터는 있음 [사실], 허용 범위 표현은 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-029] | 원문 미열람(검색 요약 수준) |
| W3C SSN/SOSA | q1-01 | W3C·OGC | 온톨로지 표준(W3C 권고안 2017-10-19) [사실]. System Capabilities 모듈(작업반 편집본)은 SystemCapability·OperatingRange·SurvivalRange·Condition 과 하위 성질을 둠 [사실] | 없음(열람 파일 기준, 부재 확정 아님 — SOSA 핵심 모듈 미열람) [추정] | 부분: 조건 아래 시스템 성능(SystemCapability)과 하위 성질 ActuationRange·MeasurementRange·Accuracy 등, 정상 운용 범위(OperatingRange) [사실] | 부분: 환경 조건(Condition)·운용 범위(OperatingRange)·손상 없이 견디는 범위(SurvivalRange)는 담음 [사실], 적재 제약은 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 없음(열람 파일 기준, 부재 확정 아님) [추정] | 미조사 | [^ref-030][^ref-235] | 확인(제3자 구현/편집본 원문 열람). /TR 권고안 원문은 미열람 |
| VDA 5050의 팩트시트 | q1-02 | VDA | 산업 인터페이스 규격. 2.0.0(2022-01)과 3.0.0(2026년 발행, 발행 2026-03, 보도자료 2026-04) [사실]. 공식 저장소 main 브랜치는 3.0.0 판. 2.x 비교 기준은 공식 저장소 2.1.0 태그 스키마(2.0.0 태그의 팩트시트 스키마 경로는 열리지 않았고 2.0.0 태그 명세는 RELEASE CANDIDATE 표기) | 팩트시트 action 정의에 전제조건 블록은 확인되지 않음(부재 확정 아님) [추정] | 부분: action 파라미터는 키·데이터형·설명·선택 여부만 두고 허용 범위는 없음 [추정], 물리 파라미터·프로토콜 한계 블록 [추정]. 지원·필수 선택 파라미터 목록(optionalParameters)은 2.1.0 태그·main 모두 둠 [사실] | 담음(형식): 적재 명세의 적재 세트별 적재 유형·치수·최대 중량·취급 높이·깊이·기울기 최소·최대, 적재 시 최대 속도·가감속, 적재·하역 소요 시간(main 스키마) [사실]. 2.1.0 태그는 같은 구조를 maxWeight·agvSpeedLimit 등 2.x 이름으로 두고, 로봇 전체 최대 적재 질량은 유형 명세(maxLoadMass→maximumLoadMass) [사실] | 3.0.0 pick·drop 완료 = 적재물이 들어오거나 떠나고 로봇이 새 적재 상태를 보고한 때 [사실]. 2.0.0 상태 메시지의 actionStatus finished 로 완료 보고 [추정] | 부분: 3.0.0 오류 등급 WARNING·URGENT·CRITICAL·FATAL, 설명·해결 힌트, action 상태 RETRIABLE [사실] / 2.0.0 오류 유형·등급(WARNING·FATAL)·설명·참조 [사실] | 팩트시트 action 정의와 주문·즉시 action 의 action 유형·파라미터가 같은 이름으로 맞물림, 관제의 사전 검증 의무는 확인되지 않음 [추정]. 사전 정의 action 29종 밖 동작은 제조사 정의 action [사실]. 2.1.0 태그 대비 main 에서 확인된 변화(완결 목록 아님): agvGeometry→mobileRobotGeometry·agvActions→mobileRobotActions 등 이름 변경, action 범위 ZONE·필수 pauseAllowed·cancelAllowed·supportedZones·batteryCharging 추가 [사실] | [^ref-022][^ref-031][^ref-032][^ref-051][^ref-228][^ref-323][^ref-329] | 확인(3.0.0 main 명세·스키마와 2.1.0 태그 스키마 원문 열람, 교차 확인 없음). 2.0.0 태그 명세는 RELEASE CANDIDATE 표기 문서, 2.0.0 게시 PDF·보도자료는 원문 미열람 |
| MassRobotics AMR 상호운용 표준 | q1-02 | MassRobotics | AMR 상호운용 표준 1.0(2021-05), 공식 JSON 스키마의 식별 보고·상태 보고 [사실]. 표준 설명 페이지(원문 미열람)는 로봇이 위치·속도·방향·상태·작업·가용 상태를 공유하고 관찰 용도로 쓰이는 보고 전용 구조로 설명 [사실]. 식별·상태 보고에 지원 작업·부착 장비를 기술하는 필드는 없는 것으로 보임(필드 목록 기준, 부재 확정 아님) [추정] | 미조사 | 미조사 | 부분: 식별 보고의 화물 최대 부피·화물 최대 중량(kg), 자유 서술 화물 유형 [사실]. 화물 최대 중량은 문자열, 최대 부피는 객체로 정의되어 화물과 수치로 비교하려면 어댑터에서 형식·단위 정규화가 필요할 것으로 보임 [추정] | 미조사 | 부분: 상태 보고의 문자열 오류 코드 배열 [사실] | 없음: 식별·상태 보고 두 메시지만 두고 명령 메시지는 없음(스키마 기준) [사실] | [^ref-033][^ref-230][^ref-391] | 확인(스키마 원문 열람, 실행 2026-09-25-35 재열람). 발표 자료·표준 설명 페이지는 원문 미열람 |
| OPC UA Robotics | q1-02 | OPC Foundation·VDMA | OPC UA 동반 규격(OPC 40010-1 Part 1: Vertical Integration, 판·발행일 미확인, 노드셋 판 표기 v100) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 프로그램을 이름·노드로 적재하고 시작·정지하는 작업 제어와 운영 상태 기계, 능력·스킬 유형은 노드셋 목록에서 확인되지 않음 [사실] | [^ref-034][^ref-244] | 확인(노드셋 문서 원문 열람, 명세 본문 미열람) |
| Asset Administration Shell의 능력·스킬·서비스 모델 | q1-02 | Plattform Industrie 4.0(CSS 토론 문서, 2022-11) / IDTA(02020 Capability Description 1.0 서브모델) | 정보 모델(CSS) [사실] / AAS 서브모델(IDTA 02020 1.0) [사실] | 담음(형식): 속성 제약(전제조건·불변조건·사후조건)과 능력 사이 전이 제약 [사실] | 부분: 속성 묶음(PropertySet)의 범위(Range) 요소 [사실] | 미조사 | 부분: 사후조건(속성 제약)이 완료 확인에 쓰일 수 있음 [추정] | 미조사 | 능력과 스킬 구현을 CapabilityRealizedBy 관계로만 잇고 실행 인터페이스는 정하지 않음 [사실]. CSS 참조 모델은 스킬 상태 기계를 스킬 인터페이스로 노출 [사실]. 제3자 논문 표기(ConditionContainer·realizedBy)는 1.0 템플릿에서 확인되지 않음 — 판 차이 여부 미확인 | [^ref-035][^ref-036][^ref-037][^ref-229][^ref-243] | 확인(IDTA 02020 템플릿·README 원문 열람). CSS 문서·논문은 원문 미열람 |
| Open-RMF Fleet Adapter의 기능 기술 | q1-02 | Open Robotics | 오픈소스 다중 로봇 조율 프레임워크의 플릿 어댑터 설정(작업 유형 Clean·Delivery·Loop, 사용자 정의 동작) [사실] | 문서가 설명하지 않음 [사실] | 동작별 내용(description)을 넘기되 파라미터 스키마는 문서가 설명하지 않음 [사실] | 미조사 | execution.finished() 로 완료를 알림 [사실] | 구조화된 실패 보고는 문서가 설명하지 않음 [사실] | 선언한 동작 이름(category)을 어댑터의 execute_action 이 받아 처리, 완료 신호까지 로봇 제어를 어댑터에 넘김 [사실] | [^ref-039][^ref-040] | 확인(ref-040 튜토리얼 원문 열람). ref-039는 원문 미열람 |
| Robotic Capability Ontology(RCO) (후보 밖) | 후보 밖 — finding f8, 실행 2026-09-25-02 | Naqvi 외(Scientific Reports, 2025-10-02) | 온톨로지(광고 능력·운용 능력 구분) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-041] | 원문 미열람 |
| 이종 자율 로봇 능력·스킬 모델 (후보 밖) | 후보 밖 — finding f18, 실행 2026-09-25-02 | Vieira da Silva·Köcher·Fay(2022-09) | 능력·스킬 모델, AAS 서브모델–온톨로지 양방향 매핑 개념 [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-038] | 원문 미열람 |
| IDTA 02047 무인운반차 기술 데이터 (후보 밖) | 후보 밖 — finding f9, 실행 2026-09-25-16 | IDTA | AAS 서브모델 템플릿 1.0 [사실]. 특수 능력(SpecialCapabilities)은 IDTA 자체 식별자를 가진 다국어 자유 텍스트 속성 [사실]. 제조사명·최대 적재 질량·실외 사용 적합 같은 속성에는 ECLASS 속성 IRDI, 측경사 각·기구학 유형 같은 무인운반차 고유 속성에는 IDTA 자체 식별자를 쓰고, ECLASS 분류 클래스 코드(0173-1#01-…)는 제조사명·제조사 제품 명칭 등 일반 정보 요소와 제품 이미지의 복합 semanticId 에만 나타남 [사실] | 미조사 | 부분: 최대 속도·가동 시간의 명세값(AsSpecified)·운용값(AsOperated), 위치추정·정위치 정확도 [사실] | 담음(형식): 최대 적재 질량, 적재·무적재 등판·측경사 각, 실외 사용 적합 여부와 요구 환경 조건 [사실] | 미조사 | 미조사 | 미조사 | [^ref-245][^ref-392] | 확인(실행 2026-09-25-16·2026-09-25-35 템플릿 원문 열람). ECLASS IRDI 설명 페이지는 원문 미열람 |
| SkiROS2 (후보 밖) | 후보 밖 — finding f10, 실행 2026-09-25-16 | RVMI lab, Aalborg University | 스킬을 행동 트리로 조합하는 ROS 기반 플랫폼 [사실]. 로봇 내부 실행 플랫폼(연계 대상)이며 스킬 조건 표현 사례로만 비교 | 담음(형식): 스킬마다 전제조건·유지조건·사후조건 [사실] | 부분: 의미 데이터베이스 세계 모델로 스킬 파라미터 자동 추론 [사실] | 미조사 | 부분: 사후조건이 완료 확인에 쓰일 수 있음 [추정] | 미조사 | 미조사 | [^ref-250] | 확인(README 원문 열람) |
| CaSkMan (후보 밖) | 후보 밖 — finding f20, 실행 2026-09-25-16 | CaSkade-Automation(Köcher 외) | 제조 기계의 능력·스킬 OWL 온톨로지(이동로봇 사례 없음) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 기계가 능력을 제공하고 능력이 스킬로 실현되며 스킬이 ISA 88 상태 기계와 REST·OPC UA 스킬 인터페이스로 실행됨 [사실] | [^ref-231] | 확인(README 원문 열람) |

표는 요약이며, 태그가 붙은 근거 문장은 [단계 1. 기존 능력 표현 모델과 표준 조사](stage-1-existing-models-and-standards.md)의 3절에 있다. 칸의 [사실]·[추정]은 근거 문장의 태그 수준이다. 실행 2026-09-25-02는 원문을 열지 못한 환경에서 검색 결과로만 채웠고, 실행 2026-09-25-16은 공식 GitHub 저장소 원문을 열 수 있는 행(VDA 5050, MassRobotics, OPC UA Robotics 노드셋 문서, IDTA 02020·02047, Open-RMF 튜토리얼, SkiROS2, CaSkMan)을 원문으로 보강했다. 실행 2026-09-25-23은 학술 온톨로지 행을 공개 저장소 원문으로 채웠다: IEEE 1872 CORA 와 IEEE 1872.2 는 제3자 OWL 번역·구현(IEEE 표준 본문 아님), SSN 은 작업반 편집본, SOMA 와 KnowRob 은 공식 저장소 파일이다. KnowRob 칸은 README 범위에서 판정할 수 없어 SOMA 칸을 참조하게 했고, PDDL 행은 여전히 검색 요약 수준이다. 실행 2026-09-25-35는 MassRobotics 행의 종류·적재·환경 제약 칸과 IDTA 02047 행의 종류 칸을 원문으로 보강했다(단계 1의 q1-08 답과 q1-09 부분 답). MassRobotics 행의 전제조건·파라미터 범위·완료 확인 방법 칸은 근거 finding 이 없어 미조사로 남았다. "없음"으로 적은 칸은 열람 파일 기준의 부재 관찰이며 부재의 확정이 아니다. 원문을 연 행도 발행 주체 한 곳의 자료에 기대며 교차 확인은 없다. VDA 5050 팩트시트의 2.x 대비 변화는 2.1.0 태그 기준이고 2.0.0 게시판과의 필드 대조는 미확인이며, 3.0.0 변경 목록은 확인된 변화일 뿐 완결 목록이 아니다(단계 1의 q1-07 답).

## 5. 빠진 정보 요약

아래는 원문을 연 모델 기준의 종합이다. 단계 1의 q1-03 은 실행 2026-09-25-23에서 학술 온톨로지 행 대조를 더해 답함으로 처리했다.

- **전제조건**: 형식으로 담는 것은 IDTA 02020 속성 제약(전제·불변·사후조건), SkiROS2 스킬 조건, SOMA 요구 초기 상황, PDDL 행동 전제조건이다. VDA 5050 팩트시트의 action 정의에서는 전제조건 블록이 확인되지 않았다. [추정][^ref-229][^ref-250][^ref-324][^ref-029][^ref-228]
- **파라미터 범위**: IDTA 02020 범위(Range) 속성과 SSN 시스템 능력(ActuationRange 등)이 담고, VDA 5050 팩트시트는 데이터형만 둔다. [추정][^ref-243][^ref-235][^ref-228]
- **적재·환경 제약**: 적재 제약은 VDA 5050 적재 세트, IDTA 02047, MassRobotics 화물 최대값 같은 산업 규격에만 있고 원문을 연 학술 온톨로지에서는 확인되지 않았다. 환경 제약은 SSN 의 Condition·OperatingRange·SurvivalRange 와 IDTA 02047 의 요구 환경 조건이 담는다. [추정][^ref-228][^ref-245][^ref-230][^ref-235]
- **완료 확인 방법**: VDA 5050 3.0.0 pick·drop 완료 정의, IDTA 02020 사후조건, SkiROS2 사후조건, SOMA 기대 종료 상황·Succeeded 상태가 담는 것으로 보인다. [추정][^ref-031][^ref-229][^ref-250][^ref-324]
- **오류의 의미**: VDA 5050 오류 등급·해결 힌트와 SOMA 의 Failed 상태·기대 불일치 상황이 담으며, 오류 복구 절차를 구조화한 모델은 RETRIABLE 상태와 자유 서술 힌트 외에 확인하지 못했다. [추정][^ref-051][^ref-324]
- **학술 온톨로지 종합**: 원문을 연 학술 온톨로지 기준으로 전제조건·완료 확인·오류 의미는 SOMA 가, 파라미터 범위·환경 제약은 SSN System Capabilities 가 일부 담고, CORA·IEEE 1872.2 구현은 다섯 항목을 담지 않으며, 적재 제약은 산업 규격에만 있어 ROP 는 적재 제약과 오류의 조치 의미(등급·재시도)를 산업 규격 쪽에서 가져와야 할 것으로 보인다. [추정][^ref-324][^ref-235][^ref-330][^ref-325][^ref-228]
- **종합**: 다섯 정보 항목을 한 모델이 모두 담는 경우는 확인되지 않았다. [추정][^ref-228][^ref-031][^ref-051][^ref-243][^ref-245][^ref-230][^ref-250][^ref-324][^ref-235]

ROP용 능력 개념 요구 목록 초안(아홉 후보)은 실행 2026-09-25-23에서 [능력 온톨로지 초안](ontology-draft.md) 6절에 실렸고, 그 가운데 요구·제공 한정자, 실행 상태, 장착 장비의 부착 인터페이스·적재 취급 장치 위치가 v0.3에 반영됐다.

실행 2026-09-25-35 보강:

- **MassRobotics 의 적재 정보**: VDA 5050 팩트시트가 적재 세트별 치수·최대 중량·취급 높이와 지원 action 을, IDTA 02047 이 부착 장비 인터페이스를 두는 것과 달리 MassRobotics 식별 보고는 로봇 전체 수준의 최대값(화물 최대 중량·부피, 최대 속도, 가동 시간, 충전기 유형)만 두므로, 분류 원문 질문(누가 이 화물을 실제로 취급할 수 있는가)에 답하려면 ROP 는 적재 취급 방식·지원 동작·장착 장비 정보를 팩트시트·서브모델·매뉴얼 같은 다른 출처에서 보완해야 할 것으로 보인다. [추정][^ref-230][^ref-228][^ref-245]

## 6. 갱신 규칙

- 갱신 주체는 스토리텔러 에이전트이며, 내용 검증 에이전트가 승인한 발견 사항만 반영한다(갱신 주체 규칙은 [에이전트 소개](../../about/agents.md)의 "트랙 실행이 일반 실행과 다른 점" 절에 있다).
- 표준·규격은 발행 기관의 공식 자료를 우선한다. 유료라 원문을 못 열면 공식 요약·공개 초안·발행 기관 소개 자료를 쓰고 "원문 미열람"을 표시한다. 벤더 문서에서 가져온 기능·성능은 `[추정]`에 "벤더 주장"을 병기한다.
- 후보 이름은 조사 후 발행 기관의 공식 명칭과 현재 버전으로 고쳐 쓸 수 있다. 그 경우 트랙 정의의 원래 후보 이름을 괄호로 남긴다. [가정]
- 행은 지우지 않는다. 제외는 상태로 표시하고 이유를 적는다.
- 이 페이지에는 퍼블리셔가 다시 쓰는 자동 갱신 영역(auto 마커)이 없다. 상단 상태 줄의 숫자는 갱신할 때 스토리텔러가 이 페이지의 표와 맞춘다. 상태 줄의 "마지막 실행"은 [트랙 개요](index.md)의 최근 실행 자동 표를, 산출 단계의 완료 조건 충족 여부는 같은 페이지의 단계 진행 현황 자동 표를 기준값으로 삼고, 이 줄과 그 표가 다르면 그 표를 따른다. [가정]
- 변경 요약은 8절 이력과 [트랙 로그](log.md)에 남긴다.

## 7. 출처

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
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-229]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-25
[^ref-243]: IDTA (admin-shell-io/submodel-templates), IDTA 02020_Template_Capability_Description.json, 미확인, https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json, 접근일 2026-09-25
[^ref-231]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-244]: OPC Foundation (UA-Nodeset GitHub), UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv, 미확인, https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv, 접근일 2026-09-25
[^ref-245]: IDTA (admin-shell-io/submodel-templates), IDTA 02047-1-0 Template_TechnicalDataForAGV.json, 미확인, https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json, 접근일 2026-09-25
[^ref-250]: RVMI lab, Aalborg University (SkiROS2 GitHub), SkiROS2 — README (skill-based robot control platform), 미확인, https://github.com/RVMI/skiros2, 접근일 2026-09-25
[^ref-323]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 (tag 2.1.0) — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-329]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 (tag 2.0.0) — VDA5050_EN_V1.md, 미확인, https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md, 접근일 2026-09-25
[^ref-235]: W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub), ssn/integrated/ssn-system.ttl (SSN System Capabilities module), 미확인, https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl, 접근일 2026-09-25
[^ref-324]: EASE CRC (ease-crc/soma), SOMA — owl/SOMA-ACT.owl, 미확인, https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl, 접근일 2026-09-25
[^ref-325]: Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub), IndustrialStandard-ODP-IEEE1872-2 — AuR_IEEE1872-2.ttl, 미확인, https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2/blob/main/AuR_IEEE1872-2.ttl, 접근일 2026-09-25
[^ref-330]: srfiorini (IEEE1872-owl GitHub), IEEE1872-owl — cora-bare.owl (OWL specification of CORA), 미확인, https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl, 접근일 2026-09-25
[^ref-326]: KnowRob (knowrob GitHub), knowrob — README (dev branch), 미확인, https://github.com/knowrob/knowrob, 접근일 2026-09-25
[^ref-391]: MassRobotics, What Is the MassRobotics AMR Interoperability Standard?, 미확인, https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/, 접근일 2026-09-25 (원문 미열람)
[^ref-392]: ECLASS e.V., IRDI - ECLASS Technischer Support, 미확인, https://eclass.eu/support/technical-specification/structure-and-elements/irdi, 접근일 2026-09-25 (원문 미열람)

## 8. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-09-25 | 2026-09-25-35 | MassRobotics 행 보강(화물 최대 중량 문자열·최대 부피 객체와 정규화 필요, 보고 전용 구조, 지원 작업·부착 장비 필드 부재 [추정], 전제조건·파라미터 범위·완료 확인 방법 칸은 미조사 유지), IDTA 02047 행에 특수 능력 자유 텍스트와 ECLASS 식별자 사용 범위 메모, 빠진 정보 요약에 MassRobotics 적재 정보 보완 필요 추가, 출처 갱신 | 5 |
| 2026-09-25 | 2026-09-25-23 | 학술 온톨로지 행(IEEE 1872 CORA, IEEE 1872.2, KnowRob·SOMA, SSN/SOSA)의 다섯 정보 항목을 제3자 구현·작업반 편집본·공식 저장소 원문으로 채움(KnowRob 칸은 README 범위에서 판정 불가 — SOMA 행 참조), VDA 5050 행에 2.x 기준(2.1.0 태그)과 3.0.0 확인된 필드 변화 반영, 빠진 정보 요약 갱신 | 4 |
| 2026-09-25 | 2026-09-25-16 | VDA 5050(3.0.0 main 명세·스키마)·MassRobotics(공식 스키마)·OPC UA Robotics(노드셋 문서)·AAS(IDTA 02020 템플릿)·Open-RMF(튜토리얼 원본) 행을 원문 근거로 보강, 실행 인터페이스 연결 열 채움, 후보 밖 3행(IDTA 02047, SkiROS2, CaSkMan) 추가, IDTA 02020 표기 충돌 병기, 빠진 정보 요약 갱신 | 3 |
| 2026-09-25 | 2026-09-25-02 | 초안 작성: 후보 10행의 발행 기관·종류 채움, 근거가 있는 정보 항목 칸만 태그와 함께 채움, 모든 행 원문 미열람, 후보 밖 2행(RCO, 이종 자율 로봇 능력·스킬 모델) 추가, 빠진 정보 요약 작성 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 빈 틀 생성: 후보 10행, 비교 열 12개(후보 열 포함) 정의, 모든 칸 미조사 | 1 |
