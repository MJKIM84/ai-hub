---
area: 24
title: "24. 작업·워크플로 모델링"
researched: 2026-10-10
researcher: "Codex (GPT-6)"
---

# 24. 작업·워크플로 모델링 — 보완 조사

## 요약
- 로봇 하역 완료를 GS1 업무 단계에 바로 대응시키는 표현을 좁힌다. 동작 완료와 업무 완료의 구분은 유지한다.
- 메시지 수신·상관·시간 초과의 근거를 벤더 설명에서 BPMN 2.0.2 규범 원문으로 보강한다.
- FaMe의 농업·지상 로봇 협업 예제와 Open-RMF의 취소 후 단계 처리를 구체화한다.
- 2026년 형식 비교 연구와 2026-09-26 Open-RMF 단계 건너뛰기 수정 이력을 추가한다.

## 보완 항목

### 3. 왜 중요한가 — 수정
- 대상 문장(수정·교차 확인일 때): "로봇 관제 규격의 완료 신호(VDA 5050 drop 완료, Open-RMF IngestorResult SUCCESS)는 GS1 CBV의 arriving 수준의 물리적 인도만 나타내고 수령자 재고 반영(receiving)과 점유·소유 변경(accepting)은 다른 규격이 정의하므로, 공정 모델은 ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 서로 다른 단계와 완료 조건으로 두고 둘을 잇는 식별 키를 명시해야 할 것으로 보인다(이 구성을 적용한 표준·사례는 확인하지 못했다)."
- 새 내용: GS1 핵심 업무 어휘(Core Business Vocabulary, CBV)는 `arriving`을 위치 도착, `accepting`을 점유 또는 소유 변경, `receiving`을 수령과 수령자 재고 편입으로 구분한다. [사실][^n1] VDA 5050의 `drop` 완료는 화물이 로봇을 떠나고 새 적재 상태가 보고된 때이며, Open-RMF의 `IngestorResult`에는 재고 편입 여부를 나타내는 필드가 없다. [사실][^n2][^n3] 따라서 하역 완료를 특정 CBV 단계와 자동으로 동일시하지 말고, 해당 업무의 인수·재고 확정 조건을 별도 완료 조건으로 모델링하는 편이 타당하다. [의견][^n1][^n2][^n3]
- 근거 메모: CBV.ttl의 `BizStep-arriving`, `BizStep-accepting`, `BizStep-receiving`; VDA 5050 3.0.0 §6.2.3의 동작 상태 표 `drop/FINISHED`; IngestorResult.msg 전체 필드. 서로 다른 규격의 의미를 대조한 것으로, 공식 변환 매핑을 발견한 것은 아니다. CBV는 `receiving`과 `arriving`·`accepting`의 사용을 상호 배타적으로 설명하므로 한 이벤트에 세 의미를 동시에 붙이는 근거로 쓰지 않는다.

### 6. 대표 접근법과 기술 — 교차 확인
- 대상 문장(수정·교차 확인일 때): "이 구조를 쓰면 로봇 운반 뒤 인수 확인을 기다리는 단계를 둘 수 있을 것으로 보이며, 아래 도식은 이 추정 구성을 그린 것이다(적용 사례 미확인)."
- 새 내용: 업무 프로세스 모델 및 표기법(Business Process Model and Notation, BPMN) 2.0.2는 외부 메시지가 도착하면 완료되는 수신 작업(Receive Task), 메시지를 인스턴스에 연결하는 상관 키(Correlation Key), 시간 조건을 표현하는 타이머 이벤트(Timer Event)를 정의한다. [사실][^n4] 따라서 운반 뒤 인수 확인 대기와 시간 초과 분기를 표현하는 구조는 특정 벤더에 한정되지 않지만, 로봇 작업 식별자를 어떤 상관 키로 쓸지는 구현에서 정해야 한다. [추정][^n4][^n5]
- 근거 메모: 기존 6절 분리 페이지의 BPMN 문장. OMG 규범 PDF §8.4.2, §10.3.3의 Receive Task(인쇄 p.159), §10.5 Timer Event. FaMe 공식 지침 G5와 구성 절은 타이머·ROS 메시지 연결을 실제 모델링 지침으로 제시한다. OMG와 대학 연구팀 자료는 독립 출처다. Camunda 고유 TTL·중복 제거 동작까지 BPMN 표준의 보장으로 확대하지 않는다.

### 5. 적용 사례 (현장 유형 명시) — 추가
- 새 내용: 현장 유형은 농업과 지상 로봇 협업 실험이며, FaMe 연구팀은 두 시나리오의 시뮬레이션 패키지와 재현 명령을 공개한다. [사실][^n5] 로봇을 풀(Pool), 임무를 프로세스(Process), 동작을 활동(Activity)으로 나타내고, 병렬 실행·조건 분기·시간 대기·오류 처리를 BPMN 요소로 구성한다. [사실][^n5] 이 예제는 창고 밖의 작업 모델링 사례로 추가할 수 있지만, 국내 상용 운영 실적으로 분류할 근거는 확인 못 함이다. [의견][^n5]
- 근거 메모: FaMe 공식 페이지의 Reproducing the simulation, MODELING 지침 G1–G7, CONFIGURATION. 지상 로봇 협업·농업 패키지 링크와 실행 절차를 확인했다. 연구팀의 실물 실험 사진도 있으나 시뮬레이션 성능을 현장 성능으로 환산하지 않았다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: Open-RMF 작업 인터페이스에서 `cancel()`은 취소 후에도 로봇의 짐 등을 정리하는 단계를 수행할 수 있고, 완료 콜백이 호출되어야 취소 처리가 끝난다. [사실][^n6] BPMN은 이미 완료한 활동의 효과를 다루는 보상(Compensation)을 별도 활동으로 표현한다. [사실][^n4] 따라서 워크플로에는 취소 요청과 취소 후 정리 완료를 나누고, 실제 물건의 이동을 되돌릴 수 있는지에 따라 보상 단계를 정의하는 편이 좋다. [의견][^n4][^n6]
- 근거 메모: Task.hpp의 `Task::Active::cancel()`·`kill()` 주석; BPMN §10.7 Compensation. 두 자료가 같은 상태 체계를 공유한다는 뜻은 아니다. 공통으로 취소와 사후 처리를 구별한다는 설계 근거다.

### 6. 대표 접근법과 기술 — 추가
- 새 내용: Open-RMF의 `rmf_task_sequence::Task`는 순서대로 수행할 단계(Phase)의 연쇄이며, 각 단계는 이벤트(Event)들로 구성된다. [사실][^n7] 현재 README가 열거하는 이벤트에는 `GoToPlace`, `PickUp`, `DropOff`, `PerformAction`, `WaitFor`, `Bundle`이 있다. [사실][^n7] 이 목록만으로 임의의 업무 병렬 분기와 합류를 모두 실행하는 범용 BPMN 엔진이라고 보기는 어렵다. [추정][^n4][^n7]
- 근거 메모: rmf_task README의 rmf_task_sequence 및 Usage 절. 모델과 실제 동작 구현이 각각 rmf_task_sequence와 rmf_fleet_adapter에 놓인다고 설명한다. 지원 이벤트의 존재와 임의 업무 그래프 지원은 구분했다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가
- 새 내용: VDA 5050 3.0.0은 2026-03-19 발표판이며, 동작의 병행 가능성을 정하는 `blockingType`에 `SINGLE`을 추가했다. [사실][^n2][^n10] `SINGLE`은 주행을 허용하면서 다른 동작의 병렬 실행을 막으므로, 주행과 작업 활동의 동시 수행 가능성을 모델링할 때 `HARD`와 구별해야 한다. [사실][^n2]
- 근거 메모: 공식 3.0.0 릴리스의 발표일·변경 목록과 태그 고정 명세 §6.2.2, 표 3. 두 링크는 같은 표준 발행 계열이므로 독립 교차 검증으로 세지 않는다. 기존 페이지도 3.0.0을 사용한다. 새 판이 발견된 것이 아니라 워크플로 관련 변경점과 고정판 근거를 보충한 것이다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가
- 새 내용: `rmf_fleet_adapter` 2.14.0의 2026-09-26 변경 이력에는 단계 건너뛰기 요청의 `phase` 키 수정이 포함되어 있다. [사실][^n9] 따라서 단계 건너뛰기를 운영 정책에 넣는 구현은 패키지 버전과 요청 스키마를 함께 기록하는 편이 좋다. [의견][^n9]
- 근거 메모: rmf_ros2의 `2.14.0` 태그, rmf_fleet_adapter/CHANGELOG.rst, “Fix phase key for skip requests” 항목 #543. 2026-09-25 조사 이후의 변경이다. 개별 패키지 버전이며 Open-RMF 전체의 단일 버전이나 모든 ROS 배포판의 설치 버전을 뜻하지 않는다.

### 8. 대표 연구와 자료 — 수정
- 대상 문장(수정·교차 확인일 때): "Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis(2026) — 행동 트리(Behavior Tree), 상태 기계, 계층적 작업 네트워크(HTN), BPMN 네 가지 로봇 임무 기술 형식을 임무 수준에서 제어 구조·표현력·한계·도구 지원 기준으로 비교했다."
- 새 내용: Filippone 외의 2026-08-17 개정 프리프린트(v2)는 행동 트리(Behavior Tree), 상태 기계(State Machine), 계층적 작업 네트워크(Hierarchical Task Network, HTN), BPMN을 제어 구조·임무 표현·도구 지원으로 비교한다. [사실][^n8] 연구는 83명에게 설문을 요청해 29개 완성 응답을 얻고 후속 인터뷰를 수행했으며, 형식별 처리량을 같은 로봇 현장에서 측정한 성능 대회는 아니다. [사실][^n8] 따라서 형식 선택의 검토 자료로 쓰되 특정 형식이 항상 우수하다는 결론으로 옮기지 않는 편이 좋다. [의견][^n8]
- 근거 메모: 8절 분리 페이지의 기존 문장을 원문으로 확인하고, 기존 2026-03 초판 표기를 실제 열람한 v2 정보로 보강했다. 원문 §III 연구 방법, §IV–VI 비교, §VII 타당성 위협. 표 II·IV·VI·VII를 확인했으며 비교 연구의 참여자 근거와 현장 실험을 구분했다. 같은 논문의 재열람이며 독립 교차 검증은 아니다.

## 답한 열린 질문
- 질문: "업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가?" → 부분 답변: FaMe는 BPMN과 ROS 2를 연결하는 공개 실행 프레임워크를 제공한다. [사실][^n5] 다만 이것을 Open-RMF·VDA 5050 상태와 BPMN 사이의 표준 매핑으로 볼 근거는 확인 못 했으므로 원 질문은 열린 상태로 유지해야 한다. [의견][^n2][^n5][^n7]
- 질문: "로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가?" → 부분 답변: 확인한 원문들은 로봇 동작 완료와 업무 단계의 정의까지만 제공하며, 그 사이의 표준 변환은 확인 못 함이다. [추정][^n1][^n2][^n3] `drop` 완료를 곧바로 `arriving` 또는 `receiving`으로 단정하지 않는 수준까지만 답을 보강한다. [의견][^n1][^n2]

## 새로 생긴 열린 질문
- 로봇이 이미 하역한 뒤 작업이 취소되면, 정리 단계와 업무상 인수 취소를 어떤 완료 조건으로 나눠야 하는가?
- Open-RMF `Bundle`과 BPMN 병렬 합류의 의미 차이를 자동 검사하는 공개 변환기가 있는가?
- 정책 버전이 바뀔 때 이미 시작한 워크플로가 이전 정책을 유지하는지, 새 정책으로 옮기는지 공개 운영 기준이 있는가?

## 출처
집계: 총 10개, 기존 영역·분리 주제 페이지 대비 새 출처 6개(n4·n5·n6·n7·n9·n10), 원문 열람 10/10. 같은 문서의 다른 호스트는 새 출처로 세지 않았으며 BPMN 2.0.2 규범판은 기존 2.0 소개 페이지와 구별했다.

[^n1]: GS1, CBV ontology 2.0 — CBV.ttl, 2021-09-30, [공식 원문](https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl), 접근일 2026-10-10, 원문 열람.
[^n2]: VDA / VDMA, VDA 5050 Version 3.0.0, 2026-03-19, [3.0.0 태그 명세](https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md), 접근일 2026-10-10, 원문 열람.
[^n3]: Open-RMF, IngestorResult.msg, 발행일 미확인, [공식 메시지 정의](https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg), 접근일 2026-10-10, 원문 열람.
[^n4]: OMG, Business Process Model and Notation Version 2.0.2, 2014-01, [규범 PDF](https://www.omg.org/spec/BPMN/2.0.2/PDF), 접근일 2026-10-10, 원문 열람(PDF 본문·관련 페이지 렌더 확인).
[^n5]: University of Camerino PROS Lab, FaMe — A BPMN-driven Framework for Multi-Robot System Development, 2022-05-03(페이지 게시일), [공식 사용·모델링 지침](https://pros.unicam.it/fame/), 접근일 2026-10-10, 원문 열람.
[^n6]: Open-RMF, rmf_task — Task.hpp, 발행일 미확인, [공식 API 원문](https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp), 접근일 2026-10-10, 원문 열람.
[^n7]: Open-RMF, rmf_task — README, 발행일 미확인, [공식 README](https://github.com/open-rmf/rmf_task/blob/main/README.md), 접근일 2026-10-10, 원문 열람.
[^n8]: Gianluca Filippone, Sara Pettinari, Patrizio Pelliccione, Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-08-17(v2; 초판 2026-03), [v2 프리프린트 본문](https://arxiv.org/html/2603.15427v2), 접근일 2026-10-10, 원문 열람.
[^n9]: Open-RMF, rmf_fleet_adapter Changelog — 2.14.0, 2026-09-26, [태그 고정 변경 이력](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst), 접근일 2026-10-10, 원문 열람.
[^n10]: VDA / VDMA, VDA 5050 3.0.0 release notes, 2026-03-19(표준 발표일), [공식 릴리스](https://github.com/VDA5050/VDA5050/releases/tag/3.0.0), 접근일 2026-10-10, 원문 열람.
