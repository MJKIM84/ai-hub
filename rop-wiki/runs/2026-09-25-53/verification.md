# 1차 검증(브리프) 2026-09-25-53

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw.githubusercontent.com 의 템플릿 JSON 을 다시 열어 ProductImages(0173-1#02-ABM220#001/0173-1#01-AHY911#001)와 SpecificDescriptions(0173-1#02-ABM221#001/0173-1#01-AHY912#001)의 복합 식별자를 확인했다. 열람 응답은 이번에도 DecelerationMax 에서 잘렸다. GeneralInformation(ABK161/AHX838)은 이번 검증 열람 응답에 나오지 않았다. 다만 실행 2026-09-25-35 의 원문 확인(단계 1 페이지 3절 q1-09 부분 답에 이미 실림)과 일치한다. 새로 더해지는 것은 AHY911·AHY912 두 식별자뿐이다. 단일 발행 기관 자료이며 발행일은 미확인이다. |
| f2 | 예 | 예 | 아니오 | 유지 | 부분 확인: 검증 열람에서도 DecelerationMax 에서 잘렸고 Charg·Battery·Energy 문자열은 보이지 않았다. 그러나 'VDA5050' 문자열은 잘리기 전 범위에서 보였다(기구학 유형·차량 등급·위치추정·주행 방식 값 설명). 주장 가운데 'VDA5050 문자열이 보이지 않았다'는 부분은 검증 결과와 맞지 않는다(required_fixes). ref-198 은 원문 미열람이다. oq-060 은 해소되지 않았으며 [추정]을 유지한다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 저장소 README 를 raw 경로로 열었다. Technical Data 1.1·2.0.1, Capability Description 1.0, Technical Data for AGV 1.0, Digital Battery Passport Part 1~7(1.0 또는 1.0.1)을 확인했다. 이름에 Robot·Skill·Charging·Mobile 이 들어간 템플릿은 없다. 브리프는 ref-439 를 fetched=false·source_unopened=true 로 적었지만 self_check.limits 에는 raw 로 열었다고 적어 표시가 서로 어긋난다. evidence_excerpt 의 영어 문장은 열람 도구의 요약이며 원문 인용이 아니다. 목록 이름 기준의 부재 관찰이다. |
| f4 | 예 | 예 | 아니오 | 유지 | Digital Battery Passport Part 1~7 이 있다는 점은 README 로 확인했다. 템플릿 본문은 미열람이다. 충전 능력과의 관련성은 추론이므로 [추정] low 를 유지한다. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: 2.0.1 README 를 raw 로 열었다. 2.0 의 버그 수정판이며 이슈 #190·#178·#174·#173·#168·#161(6건)을 다룬다. ProductImages→ProductImage 개명, TechnicalPropertyAreas 카디널리티 0..1, 중복 semanticId 제거가 있다. ProductClassifications·ECLASS·IEC CDD 언급은 없다. 발행일은 미확인이다. |
| f6 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 검색 결과로 ZVEI URL·문서와 ProductClassificationItem 의 식별자 https://admin-shell.io/ZVEI/TechnicalData/ProductClassificationItem/1/1 및 설명(분류 체계·속성 사전의 제품 클래스와 연결)을 확인했다. …/ProductClassificationSystem/1/1 식별자는 검증 검색 요약에서 확인하지 못했다(required_fixes). 검색 결과의 문서 제목은 'Generic Frame for Technical Data for Industrial Equipment in Manufacturing (Version 1.1)'이다. 같은 식별자가 IDTA 02003-1-2 에도 나오지만 승계 관계라 독립 교차 확인이 아니다. 기준일 2020-11. |
| f7 | 예 | 예 | 아니오 | 유지 | 검색 결과 기준의 부재 관찰이며 데이터베이스는 미조회다. 실행 2026-09-25-41·45·47 의 같은 관찰을 되풀이한다. [추정] low 를 유지한다. ref-183·184·185 는 원문 미열람이다. |
| f8 | 예 | 예 | 아니오 | 유지 | f1(원문)과 f6(검색 요약)을 대응시킨 이 위키의 추론이다. [추정] low 를 유지한다. 실행 2026-09-25-47 의 '세 층 의미 식별자' 추정과 겹치므로 새 결론이 아니라 보강으로 쓴다. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | f1 의 GeneralInformation 복합 식별자(0173-1#02-ABK161#002/0173-1#01-AHX838#002)는 단계 1 페이지 3절 q1-09 부분 답(실행 2026-09-25-35)에 이미 있다. 새 내용은 AHY911·AHY912 두 식별자뿐이다, f7 은 실행 2026-09-25-41·45·47 의 ECLASS·IEC CDD 미검출 관찰을 되풀이한다, f8 은 실행 2026-09-25-47 의 '세 층 의미 식별자' 추정과 겹친다, f6 은 실행 2026-09-25-47 의 IDTA 02003 제품 분류 항목(ref-438) 서술을 식별자 수준으로 보강한다(승계 관계), f2 는 oq-060 출처 충돌의 근거 보강이며 해소가 아니다 |
| 용어 일관성 | 예 | — |
| 인용 길이·저작권 | 예 | f3 evidence_excerpt 의 'No templates matching Robot, Charging, Skill, or Mobile' 은 열람 도구 요약문이며 원문 인용이 아니다. 페이지에서 직접 인용으로 쓰지 않는다 |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f1: 3절 '실행 2026-09-25-53 보강' 소절에서는 새로 확인된 ProductImages(0173-1#02-ABM220#001/0173-1#01-AHY911#001)와 SpecificDescriptions(0173-1#02-ABM221#001/0173-1#01-AHY912#001) 복합 식별자만 새 사실로 적는다. GeneralInformation(ABK161/AHX838)은 실행 2026-09-25-35 의 기존 문장을 가리키는 데 그친다. 이유: 같은 주장이 이미 페이지에 있다.
- f2: 'Charg·Battery·Energy·VDA5050 문자열이 보이지 않았다'에서 'VDA5050'을 뺀다. 태그는 [추정], 두 출처(ref-245, ref-198)는 한쪽을 고르지 않고 병기하며 oq-060 은 열림으로 둔다. 이유: 검증 재열람에서 VDA5050 문자열은 잘리기 전 범위의 값 설명에 나타났다.
- f6: ProductClassificationItem 의 식별자(…/ProductClassificationItem/1/1)만 [사실]로 쓴다. ProductClassificationSystem 의 식별자(…/ProductClassificationSystem/1/1)는 '미확인'으로 두거나 뺀다. 이유: 검증 검색 요약에서 이 식별자가 확인되지 않았다.
- ref-660: 각주 제목을 검색 결과 기준 'Submodel Templates of the Asset Administration Shell — Generic Frame for Technical Data for Industrial Equipment in Manufacturing (Version 1.1)'로 쓰고, 발행일 2020-11, 접근일 뒤에 ' (원문 미열람)'을 붙인다. reference_updates[].source_unopened 는 true 로 둔다.
- ref-659: 각주 발행일 자리에 '미확인'을 쓰고 '(원문 미열람)'은 붙이지 않는다. 이유: raw 원문을 열었다.
- ref-439: 단계 1 페이지의 기존 각주 형식('(원문 미열람)' 없음)을 유지한다. 이유: 검증자가 raw 경로로 README 를 열어 f3·f4 를 확인했다. 브리프의 fetched=false 표시는 과소 표기다.
- ref-198·ref-183·ref-184·ref-185·ref-438: 각주 접근일 뒤의 ' (원문 미열람)' 표기를 유지한다.
- f7·f8: 새 결론처럼 쓰지 않는다. f7 은 '다섯 번째 실행에서도 같은 관찰(부재 확정 아님)', f8 은 실행 2026-09-25-47 세 층 추정의 보강으로 [추정] 태그와 함께 짧게 쓴다.
- f3: 3절에 쓸 때 evidence_excerpt 의 영어 문장을 직접 인용하지 않고 'README 게시 목록 이름 기준의 부재 관찰'로 재서술한다.
- q1-09 는 '답함'으로 바꾸지 않는다. 백로그는 '조사 중', 단계 페이지 2절은 '열림', answer_link 는 null 로 둔다. 3절 소제목 '(부분 답)'에 명시 id 를 붙이지 않는다. 4절에는 다섯 실행이 같은 벽(ECLASS·IEC CDD 데이터베이스 미조회)에 막혔고 사용자 결정(조회 결과를 inbox/sources 로 제공하거나, 사유·재개 조건을 적어 보류)이 필요하다는 점을 적는다. 이유: 답이 되는 finding 이 없다.
- 새 질문(Digital Battery Passport 배터리 요소 재사용, 단계 4, f4)을 backlog_updates 에 등록한다. origin 은 f4 이며 5절 표에 추가한다. 이유: q4-14(IDTA 02047 충전 요소 ↔ VDA 5050 batteryCharging)와 대상 출처가 달라 중복이 아니다.
- 단계 페이지 6절: 두 완료 조건 모두 '미충족 · 미승인'을 유지한다. 전환 줄은 '다음 단계로 전환: 아니오(모델·표준 비교표 미조사 칸 잔존, 요구 목록 일부 미반영, 막힌 질문 q1-09)'로 적는다. 9절 이력에 실행 2026-09-25-53 행을 추가한다(온톨로지 변경 없음, v0.3 유지).
- model-standard-comparison.md IDTA 02047 행: 종류 칸의 ECLASS 분류 클래스 코드 메모에 제품 이미지(AHY911)·SpecificDescriptions(AHY912) 복합 식별자를 [사실]로 더한다. 상태 칸에는 '실행 2026-09-25-53 재열람도 DecelerationMax 에서 절단'을 더한다. 이력 표에 행을 추가한다.

## 검증 노트

판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. GitHub 원문(ref-245 템플릿 JSON, ref-439 저장소 README, ref-659 IDTA 02003 2.0.1 README)은 검증자가 raw 경로로 직접 열어 대조했다. 확인 8건, 미확인 0건, 교차 확인 0건(모든 사실이 발행 기관 한 곳의 자료에 기댄다). 강등: 없음. 두 finding 은 부분 수정만 지시했다: f2 에서 VDA5050 문자열 부재 표현을 빼고, f6 의 ProductClassificationSystem 식별자는 미확인으로 둔다. 원문 미열람 출처: ref-660, ref-438, ref-198, ref-183, ref-184, ref-185. 브리프는 ref-439 를 fetched=false 로 적었으나 self_check 에는 열었다고 적어 표시가 어긋난다. 검증자가 원문으로 f3·f4 를 확인했다. 주의: 템플릿 JSON 은 다섯 번째 열람에서도 DecelerationMax 에서 잘려 충전 요소 유무를 원문으로 판정할 수 없다. oq-060 은 열림이다. ECLASS·IEC CDD 에 이동로봇 범위 능력 항목이 있는지는 여전히 미확인이며 부재 확정이 아니다. 정정 요청 없음. 미사용 출처 없음. 온톨로지 변경 승인: 없음 / 거부: 없음(제안 없음, v0.3 유지). 새 질문 1건(f4, 단계 4)은 q4-14 와 대상이 달라 등록한다. 단계 완료 조건: 미충족(부족: 모델·표준 비교표의 PDDL·OPC UA Robotics·MassRobotics·AAS·Open-RMF 행 미조사 칸, ROP용 능력 개념 요구 목록 가운데 구성 버전·운용 구역·환경 조건·충전 조건 미반영). 답한 질문이 0개인 것은 출처 부재(네트워크 정책으로 데이터베이스 미조회)에 따른 부분 결과로 보고 반려하지 않는다. 사양서 8.2 (1)은 미충족이다. 단계 전환: 미승인(막힌 질문 q1-09, 조사 중). 다섯 실행(2026-09-25-35·41·45·47·53)이 같은 이유로 막혔다. q1-09 를 계속 두면 단계 1 전환이 막힌다. 사용자가 ECLASS·IEC CDD 조회 결과를 inbox/sources 로 제공하거나, 사유와 재개 조건을 적어 q1-09 를 보류할지 결정해야 한다.

## 트랙 추가 검증

| 항목 | 결과 |
|---|---|
| 표준 출처(발행 기관 자료) | 예 |
| 벤더 주장 표기 | 예 |
| 온톨로지 변경 근거 | 예 |
| 백로그 중복 질문 | — |
| 단계 태그 문제 | — |
| 완전성 표현 | 예 |
| 단계 완료 판정 | 미충족 |
| 단계 전환 승인 | 아니오 |
