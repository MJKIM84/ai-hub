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
sources: [ref-022, ref-025, ref-026, ref-027, ref-028, ref-029, ref-030, ref-031, ref-034, ref-035, ref-036, ref-038, ref-039, ref-040, ref-041, ref-136, ref-051, ref-137, ref-138, ref-139, ref-140, ref-141, ref-142, ref-143, ref-115, ref-144, ref-145]
last_run: 2026-09-25
version: 3
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 모델·표준 비교표

# 모델·표준 비교표

> 산출 단계: [단계 1. 기존 능력 표현 모델과 표준 조사](stage-1-existing-models-and-standards.md) · 상태: 초안 · 조사된 후보: 10 / 10(후보 밖 4행 추가, 확인 3행·나머지 원문 미열람) · 마지막 실행: 2026-09-25

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
| IEEE 1872 CORA | q1-01 | IEEE | 온톨로지 표준(1872-2015, 핵심 온톨로지 CORA와 보조 온톨로지 CORAX·POS·RPARTS) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-025] | 원문 미열람 |
| IEEE 1872.2 자율 로봇 온톨로지 | q1-01 | IEEE | 온톨로지 표준(1872.2-2021, 2022년 발행, CORA 확장) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-026] | 원문 미열람 |
| KnowRob·SOMA | q1-01 | Beetz 외(KnowRob 2.0 논문, 2018) / Beßler 외(SOMA 논문, 2021), EASE CRC(SOMA 공식 저장소) | 지식 처리 프레임워크(KnowRob) / 활동 온톨로지(SOMA) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 부분: SOMA-ACT가 실행 상태(실패·성공·진행 중·취소·일시정지·대기)와, 충족되지 않은 사후조건 같은 기대 불일치 클래스(NonmanifestedSituation)를 정의 [사실][^ref-141] | 미조사 | [^ref-027][^ref-028][^ref-141] | 원문 미열람(오류의 의미 칸은 SOMA-ACT 원문 확인) |
| PDDL 계열 행동 모델 | q1-01 | McDermott 등(AIPS-98 계획 경진대회용, 1998) | 행동 계획 언어 [사실] | 담음(형식): 행동의 전제조건·효과 [사실]. ROP 요구 대비 충족 정도는 미확인 | 부분: 행동 파라미터는 있음 [사실], 허용 범위 표현은 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-029] | 원문 미열람 |
| W3C SSN/SOSA | q1-01 | W3C·OGC | 온톨로지 표준(W3C 권고안 2017-10-19) [사실] | 미조사 | 부분: 조건 아래 시스템 성능(SystemCapability)·정상 운용 범위(OperatingRange) [추정] | 부분: 조건(Condition)·손상 없이 견디는 범위(SurvivalRange), 적재 제약은 미조사 [추정] | 미조사 | 미조사 | 미조사 | [^ref-030] | 원문 미열람 |
| VDA 5050의 팩트시트 (3.0.0 기준) | q1-02 | VDA·VDMA(공식 GitHub 저장소) | 산업 인터페이스 규격. 이 행은 공식 저장소 main(3.0.0판) 기준, 기준일 2026-09-25 [사실][^ref-136] | 없음: 동작 파라미터 기술에 실행 전제조건 필드가 없음 [추정][^ref-136] | 부분: 동작 파라미터는 이름·자료형·설명·선택 여부만 담음 [사실][^ref-136]; 범위 정보는 물리 파라미터·적재 명세의 최소·최대 필드에 흩어진 것으로 보임 [추정][^ref-136] | 담음(형식): 적재 명세 loadSets 의 적재 유형·위치·치수·최대 중량, 적재 처리 높이·깊이·기울기 최소·최대, 적재 시 최대 속도·가감속, 픽·드롭 소요 시간 [사실][^ref-136] | 팩트시트 밖에서 담음: 명세 본문이 사전 정의 동작마다 완료·실패 판정을 상태 필드로 정의(예: pick, startCharging) [사실][^ref-031], 상태 메시지 동작 상태 일곱 값 [사실][^ref-051] | 담음(형식): 오류 유형·등급 필수, 참조·설명·조치 힌트 선택, 등급 WARNING·URGENT·CRITICAL·FATAL 은 현재 주문 계속·새 주문 수락 가능 여부로 구분 [사실][^ref-051] | 팩트시트 지원 동작 목록(mobileRobotActions)에 선언한 동작을 주문·상태 메시지에서 같은 이름으로 사용, 제조사 추가 동작도 같은 형식으로 선언 [사실][^ref-031][^ref-136]; 수행할 수 없는 동작 주문은 INVALID_ORDER_ACTION(등급 WARNING)으로 보고 [사실][^ref-031] | [^ref-031][^ref-136][^ref-051] | 확인 |
| MassRobotics AMR 상호운용 표준 | q1-02 | MassRobotics | AMR 상호운용 표준 공식 JSON 스키마(식별 보고 identityReport·상태 보고 statusReport, 스키마 판 미확인) [사실][^ref-139] | 미조사 | 부분: 식별 보고의 최대 속도·예상 가동 시간 [사실][^ref-139] | 부분: 화물 설명·화물 최대 부피·최대 중량, 상태 보고의 남은 적재 용량 비율 [사실][^ref-139] | 미조사 | 미조사 | 미조사 | [^ref-139] | 확인 |
| OPC UA Robotics | q1-02 | OPC Foundation·VDMA | OPC UA 동반 규격(OPC 40010-1 Part 1: Vertical Integration, 판·발행일 미확인) [사실]; 공식 노드셋에 MotionDeviceSystemType·MotionDeviceType·ControllerType·TaskControlType·SafetyStateType·LoadType 형식과 운전 모드·실행 모드 열거형 [사실][^ref-142] | 미조사 | 미조사 | 부분: 부하 형식(LoadType)이 정의되어 있으나 내용은 미조사 [사실][^ref-142] | 미조사 | 미조사 | 미조사 | [^ref-034][^ref-142] | 원문 미열람(노드셋 형식 이름만 원문 확인) |
| Asset Administration Shell의 능력·스킬·서비스 모델 | q1-02 | Plattform Industrie 4.0(CSS 토론 문서, 2022-11) / IDTA(02020 Capability Description 서브모델 1.0) | 정보 모델(CSS) [사실] / AAS 서브모델(IDTA 02020 1.0, IDTA 첫 공식 판) [사실][^ref-137] | 담음(형식): 속성 제약(PropertyConstraintContainer)이 전제조건·불변조건·사후조건을, 전이 제약(TransitionConstraintContainer)이 순서 요구를 담음 [사실][^ref-137][^ref-138] | 부분: 능력 속성(PropertySet — 최대 속도·허용 오차·온도 범위 등) [사실][^ref-137] | 부분: 제약 집합(ConstraintSet)과 속성으로 표현할 자리가 있음, 적재 항목은 미조사 [추정][^ref-137][^ref-138] | 미조사 | 미조사 | 능력을 구현하는 스킬로 연결(CapabilityRealizedBy) [사실][^ref-138]; 스킬은 OPC UA 같은 호출 인터페이스로 상태 기계 전이·파라미터를 다룸(CSS 참조 모델, 2022) [사실][^ref-036] | [^ref-035][^ref-036][^ref-137][^ref-138] | 원문 미열람 |
| Open-RMF Fleet Adapter의 기능 기술 | q1-02 | Open Robotics | 오픈소스 다중 로봇 조율 프레임워크의 플릿 어댑터 설정(작업 유형 Clean·Delivery·Loop, 사용자 정의 동작) [사실] | 없음: 동작 선언은 이름 목록뿐이며 전제조건 항목이 없음 [사실][^ref-040] | 없음(선언 기준): 파라미터 스키마 항목이 없고 호출 시 JSON description 으로 전달 [사실][^ref-040] | 미조사 | 능력 선언 안에서는 확인되지 않음 [추정]; 실행 콜백이 execution.finished() 로 완료를 알림 [사실][^ref-040] | 없음(선언 기준): 오류 의미 항목이 없음 [사실][^ref-040] | 설정 rmf_fleet actions 에 동작 이름 선언 → 작업 요청이 category(동작 이름)·JSON description 으로 호출 → execute_action 콜백 실행 [사실][^ref-040] | [^ref-039][^ref-040] | 원문 미열람(ref-039; ref-040 은 원문 확인) |
| Robotic Capability Ontology(RCO) (후보 밖) | 후보 밖 — finding f8, 실행 2026-09-25-02 | Naqvi 외(Scientific Reports, 2025-10-02) | 온톨로지(광고 능력·운용 능력 구분) [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-041] | 원문 미열람 |
| 이종 자율 로봇 능력·스킬 모델 (후보 밖) | 후보 밖 — finding f18, 실행 2026-09-25-02 | Vieira da Silva·Köcher·Fay(2022-09) | 능력·스킬 모델, AAS 서브모델–온톨로지 양방향 매핑 개념 [사실] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | [^ref-038] | 원문 미열람 |
| CaSkMan (후보 밖) | 후보 밖 — finding f19·f24, 실행 2026-09-25-06 | CaSkade-Automation(GitHub) | OWL 정렬 온톨로지: 제조 설비의 능력·스킬·스킬 인터페이스를 VDI 3682·VDI 2860·DIN 8580·ISA 88·DIN EN 61360 과 연결, 능력은 표준 분류의 하위 클래스로 기술 권장 [사실][^ref-140] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 스킬이 상태 기계를 갖고 REST·OPC UA 스킬 인터페이스로 메서드·전이를 노출 [사실][^ref-140] | [^ref-140] | 확인 |
| OPC 30050 OPC UA for PackML (후보 밖) | 후보 밖 — finding f18, 실행 2026-09-25-06 | OPC Foundation·OMAC | OPC UA 동반 규격, ISA-88 기반 상태 기계 정보 모델(판·발행일 미확인) [사실][^ref-145] | 미조사 | 미조사 | 미조사 | 미조사 | 미조사 | 장비 내부 상태·명령을 표준 상태 모델·표준 명령 집합으로 옮기고, 인스턴스마다 가능한 상태·전이(AvailableStates·AvailableTransitions)를 제공 [사실][^ref-145] | [^ref-145] | 원문 미열람 |

표는 요약이며, 태그가 붙은 근거 문장은 [단계 1. 기존 능력 표현 모델과 표준 조사](stage-1-existing-models-and-standards.md)의 3절에 있다. 칸의 [사실]·[추정]은 근거 문장의 태그 수준이다. 실행 2026-09-25-02는 원문을 열지 못한 환경에서 검색 결과로만 행을 채웠고, 실행 2026-09-25-06은 GitHub 공식 저장소 원문을 읽어 VDA 5050·MassRobotics·CaSkMan 행을 원문으로 채워 상태를 "확인"으로 바꿨다. 다른 행은 원문을 열지 못한 출처가 섞여 있어 "원문 미열람"을 유지하고, 원문을 읽은 칸은 괄호로 밝혔다. VDA 5050 행은 3.0.0 main 기준으로 다시 썼으며, 2.0.0(2022-01)의 오류 등급은 WARNING·FATAL 두 값이었다. [사실][^ref-022] 2.0.0 팩트시트와 3.0.0의 필드 대조는 하지 않았다(후속 질문 q1-07). AAS 행의 제약 요소는 이전 실행의 제3자 논문 경유 표기(ConditionContainer)를 IDTA 02020 템플릿의 요소 이름으로 바꿨다. 다섯 정보 항목 칸은 근거 발견 사항이 직접 뒷받침하는 칸만 채웠고, 나머지는 "미조사"로 두었다.

## 5. 빠진 정보 요약

실행 2026-09-25-06까지의 요약이다. IEEE 1872 계열·SSN·PDDL·KnowRob 행은 여전히 원문 미열람이라 단계 1의 q1-03은 부분 답 상태다.

- **종합**: 공식 원문으로 확인한 범위에서 다섯 정보 항목은 여러 규격에 흩어져 있고, 한 규격의 능력 기술 안에 다섯 항목이 모두 구조화된 경우는 확인되지 않았다. [추정][^ref-136][^ref-051][^ref-031][^ref-137]
- **전제조건**: 형식으로 담는 것은 IDTA 02020의 속성 제약(원문 미열람 표시)과 PDDL의 행동 전제조건(원문 미열람)이다. [사실][^ref-137][^ref-029] VDA 5050 팩트시트와 Open-RMF 동작 선언에는 전제조건 항목이 없다. [추정][^ref-136][^ref-040]
- **파라미터 범위**: VDA 5050 3.0.0의 동작 파라미터에는 허용 범위 필드가 없고, 범위 정보는 물리 파라미터·적재 명세의 최소·최대 필드에 흩어져 있는 것으로 보인다. [추정][^ref-136]
- **적재·환경 제약**: VDA 5050 3.0.0 적재 명세가 가장 자세하고(적재 유형·치수·최대 중량·처리 높이·기울기 등), MassRobotics는 화물 최대 부피·중량을 담는다. [사실][^ref-136][^ref-139]
- **완료 확인 방법**: VDA 5050은 완료 판정을 능력 기술(팩트시트)이 아니라 명세 본문의 동작별 정의와 상태 메시지 동작 상태에 둔다. [추정][^ref-031][^ref-051] Open-RMF는 어댑터 구현이 완료를 알린다. [사실][^ref-040]
- **오류의 의미**: VDA 5050 3.0.0의 오류 등급 네 값과 SOMA-ACT의 실행 상태·기대 불일치 클래스가 구조화된 표현이다. [사실][^ref-051][^ref-141]
- **실행 인터페이스 연결**: 선언한 동작 이름을 명령·상태에 그대로 쓰는 방식(VDA 5050·Open-RMF)과 별도 능력 모델을 스킬·상태 기계로 잇는 방식(CSS·IDTA 02020·CaSkMan·PackML)으로 나뉘는 것으로 보이며, 두 방식을 매핑한 표준은 찾지 못했다. [추정][^ref-136][^ref-040][^ref-137][^ref-140][^ref-036]
- **같은 이름 기능의 의미**: 고정 어휘(VDA 5050 사전 정의 동작), 외부 사전 식별자(AAS semanticId), 표준 분류 하위 클래스(CaSkMan), 능력 계층(IDTA 02020), 핵심 온톨로지(SWARMs), 구성요소 기반 추론으로 다뤄지는 것으로 보이나, 제조사 추가 동작의 의미는 자유 문장 설명에 남는다. [추정][^ref-031][^ref-144][^ref-140][^ref-138][^ref-115][^ref-143]

ROP용 능력 개념 요구 목록 초안은 아직 없다(q1-06 미조사). 이번 실행에서 승인된 개념 변경(실행 상태 개념, 오류·기능 속성, 관계 3건)은 [능력 온톨로지 초안](ontology-draft.md) v0.2에 반영됐다.

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
[^ref-034]: OPC Foundation / VDMA, OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration, 미확인, https://reference.opcfoundation.org/specs/OPC-40010-1, 접근일 2026-09-25 (원문 미열람)
[^ref-035]: Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services, 2022-11, https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html, 접근일 2026-09-25 (원문 미열람)
[^ref-036]: Köcher, A. 외, A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing, 2022, https://arxiv.org/abs/2209.09632, 접근일 2026-09-25 (원문 미열람)
[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots, 2022-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-25 (원문 미열람)
[^ref-039]: Open Robotics, Currently supported Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_types.html, 접근일 2026-09-25 (원문 미열람)
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-136]: VDA / VDMA (VDA5050 GitHub), VDA5050/json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-137]: IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description/1/0, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: IDTA(Industrial Digital Twin Association), IDTA 02020_Template_Capability_Description.json, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description/1/0, 접근일 2026-09-25 (원문 미열람)
[^ref-139]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25
[^ref-140]: CaSkade-Automation (GitHub), CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README), 미확인, https://github.com/CaSkade-Automation/CaSkMan, 접근일 2026-09-25
[^ref-141]: EASE CRC (ease-crc/soma), SOMA — owl/SOMA-ACT.owl, 미확인, https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl, 접근일 2026-09-25
[^ref-142]: OPC Foundation / VDMA, UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv, 미확인, https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv, 접근일 2026-09-25
[^ref-143]: Dussard, B. 외, Ontological Component-based Description of Robot Capabilities, 2023-06, https://arxiv.org/abs/2306.07569, 접근일 2026-09-25 (원문 미열람)
[^ref-115]: Li, X. 외(Sensors, MDPI), SWARMs Ontology: A Common Information Model for the Cooperation of Underwater Robots, 2017, https://doi.org/10.3390/s17030569, 접근일 2026-09-25 (원문 미열람)
[^ref-144]: IDTA(Industrial Digital Twin Association), Specification of the Asset Administration Shell Part 1: Metamodel (IDTA-01001-3-0-1), 2024, https://industrialdigitaltwin.org/wp-content/uploads/2024/06/IDTA-01001-3-0-1_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-145]: OPC Foundation / OMAC, OPC-30050 – OPC UA for PackML - Common Object Model: PackML, 미확인, https://reference.opcfoundation.org/specs/OPC-30050, 접근일 2026-09-25 (원문 미열람)

## 8. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| 2026-09-25 | 2026-09-25-06 | VDA 5050(3.0.0 main 기준)·MassRobotics 행을 공식 저장소 원문으로 채워 상태 "확인", AAS 행의 제약 요소 이름을 IDTA 02020 템플릿 기준으로 교체(원문 미열람 유지), SOMA·OPC UA Robotics·Open-RMF 칸 보강, 후보 밖 2행(CaSkMan, OPC 30050 PackML) 추가, 빠진 정보 요약 갱신 | 3 |
| 2026-09-25 | 2026-09-25-02 | 초안 작성: 후보 10행의 발행 기관·종류 채움, 근거가 있는 정보 항목 칸만 태그와 함께 채움, 모든 행 원문 미열람, 후보 밖 2행(RCO, 이종 자율 로봇 능력·스킬 모델) 추가, 빠진 정보 요약 작성 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 빈 틀 생성: 후보 10행, 비교 열 12개(후보 열 포함) 정의, 모든 칸 미조사 | 1 |
