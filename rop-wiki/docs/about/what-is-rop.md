---
title: "SCM 관점의 ROP란 무엇인가"
type: about
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../index.md) › SCM 관점의 ROP란 무엇인가

# SCM 관점의 ROP란 무엇인가

이 페이지는 분류 원문 1장 "전체 관점"을 그대로 옮긴 것이다. ASCM(Association for Supply Chain Management)의 SCOR(Supply Chain Operations Reference)가 공급망 프로세스의 범위를, ISA-95 가 기업 업무와 제조 운영·제어의 통합 경계를 참고 기준으로 제시하는 가운데, 원문은 ROP를 "물리적인 작업이 발생하는 부분을 연결하는 역할"로 본다. 즉 ROP는 SCOR 오케스트레이션 전체를 대체하는 것이 아니라, 그 계획을 로봇과 현장 설비의 실제 행동으로 옮기고 결과를 업무 시스템에 되돌려 주는 실행 플랫폼이다. [의견]

아래 본문과 표는 원문 그대로이며 `[분류원문]`으로 표시한다. 원문의 `[n]` 표기는 원문 12장 참고 자료의 n번 항목이며, 이 위키의 참고문헌 `ref-00n` 페이지에 해당한다.

## 원문 1장. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다. [분류원문]

연구 범위는 다음과 같이 구분한다. [분류원문]

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

[분류원문]

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1] [분류원문]

## 원문 각주와 참고문헌

원문의 [1]은 참고문헌 [ref-001](../references/ref-001.md)에 해당한다.[^ref-001] 참고문헌 전체 목록은 [참고문헌](../references/index.md)에 있다.

## 관련 페이지

- [ROP가 직접 소유할 범위와 외부 연계 경계](scope-boundary.md)
- [SCM 관점의 연구 시작 방법](research-method.md)
- [논의한 아이디어의 연구영역 매핑](idea-mapping.md)
- 대분류 페이지: [A. 업무·공급망 설계](../categories/a-business-supply-chain-design/index.md), [B. 공통 정보·환경 모델](../categories/b-common-information-and-environment-model/index.md), [C. 연결·실행 기반](../categories/c-connectivity-and-execution-foundation/index.md), [D. 계획·최적화](../categories/d-planning-and-optimization/index.md), [E. 협업·현장 운영](../categories/e-collaboration-and-field-operations/index.md), [F. 도입·검증·유지관리](../categories/f-deployment-verification-and-maintenance/index.md), [G. 안전·보안·지능·거버넌스](../categories/g-safety-security-intelligence-and-governance/index.md)

## 참고 자료

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24
