# 스토리텔러 산출 2026-09-25-83

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md | draft | q4-03 답함(명령 권한·감사 추적), 후속 질문 3건(q4-17·q4-18·q5-17), 결론·완료 조건·출처·이력 갱신. 2차: 단계 상태 줄을 열린 질문 15건·답한 질문 3건으로 맞추고 q4-03 시나리오 예외·성과 칸 문구를 배정 최적성 손실로 고침(전체 content) |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.8 → v0.9: 개념 '명령 권한' 추가(확정, 속성 구성·기본 거부는 후보), 지시 개념 입력자를 인증된 사용자 식별로 정리, 다이어그램·6절 질문 갱신. 2차: H1 을 (v0.9)로 맞춤(전체 content) |
| update | docs/ideas/nl-task-chatbot.md | draft | 5절에 '명령 권한과 감사 추적' 소절 신설(q4-03, 실행 2026-09-25-83, 신뢰도 low) |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 산출물 링크 갱신: 초안 v0.9(명령 권한 추가), 아이디어 5절 명령 권한 소절(q4-03) 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 4 | q4-03 답함(명령 권한·감사 추적), 업무 분해·배정 설계 초안 v0.8 → v0.9(개념 '명령 권한' 추가, 지시 입력자 정리), 후속 질문 3건 | run 2026-09-25-83
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 4: 채팅 사용자별 명령 권한과 감사 추적 구성(q4-03, 신뢰도 low), 업무 분해·배정 설계 초안 v0.9
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 자연어 업무 지시 챗봇이 사용자 명령 권한을 배정 전 후보 제약으로 넘기는 분담을 반영 제안(q4-03)
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 트랙 반영 제안 — 사용자 권한은 fleet_name 처럼 배정 전 후보를 거르는 제약, 선택 기준은 디스패처(6. 대표 접근법과 기술, 추정)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 역할 기반 접근 통제 | Role-Based Access Control (RBAC) | 사용자에게 역할을 주고 역할에 동작 권한을 묶어, 사용자가 가진 역할에 따라 어떤 자원에 어떤 동작을 할 수 있는지 정하는 접근 통제 방식이다. | 26, 13, 18 | ref-763 |
| new | 속성 기반 접근 통제 | Attribute-Based Access Control (ABAC) | 주체·객체·요청 동작의 속성과 시간·위치 같은 환경 조건을 정책에 대조해 허용 여부를 정하는 접근 통제 방식이다. | 26, 27, 13 | ref-769 |
| new | 혼란된 대리인 | Confused Deputy | 더 큰 권한을 가진 중개 프로그램이 요청자의 권한을 확인하지 않고 대신 행동해, 요청자가 원래 할 수 없는 동작이 실행되는 보안 문제다. | 26, 27 | ref-764 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-579 | Open Robotics (ros2/design GitHub) | ROS 2 Access Control Policies (design.ros2.org articles/ros2_access_control_policies) | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_access_control_policies.html |
| ref-763 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-764 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Basic: Authorization (docs/specification/2025-06-18/basic/authorization.mdx) | 표준 | medium | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/basic/authorization.mdx |
| ref-765 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 12: Record-Keeping \| EU Artificial Intelligence Act | 정부·연구기관 | medium | https://artificialintelligenceact.eu/article/12/ |
| ref-766 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 19: Automatically Generated Logs \| EU Artificial Intelligence Act | 정부·연구기관 | medium | https://artificialintelligenceact.eu/article/19/ |
| ref-767 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 정부·연구기관 | medium | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 |
| ref-768 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 표준 | medium | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 |
| ref-769 | NIST | Guide to Attribute Based Access Control (ABAC) Definition and Considerations (NIST SP 800-162) | 정부·연구기관 | medium | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf |
| ref-770 | Shi, T. 외(Progent 저자, 소속 미확인) | Progent: Programmable Privilege Control for LLM Agents | 논문 | medium | https://arxiv.org/abs/2504.11703 |
| ref-771 | South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. | Authenticated Delegation and Authorized AI Agents | 논문 | medium | https://arxiv.org/abs/2501.09674 |
| ref-772 | Tsai, L., & Bagdasarian, E.(Google, HotOS 2025) | Contextual Agent Security: A Policy for Every Purpose | 논문 | medium | https://arxiv.org/abs/2501.17070 |
| ref-773 | Luo, J. 외(Fudan University·Shanghai Innovation Institute) | AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent | 논문 | medium | https://arxiv.org/abs/2605.28071 |
| ref-774 | Zhu, J., Tseng, K., Vernik, G., Huang, X., Patil, S. G., Fang, V., & Popa, R. A.(arXiv 2512.11147) | MiniScope: A Least-Privilege Framework for Authorizing Tool-Calling Agents | 논문 | medium | https://arxiv.org/abs/2512.11147 |
| ref-775 | Mobile Industrial Robots(MiR) | MiR Fleet | 벤더 문서 | low | https://mobile-industrial-robots.com/products/software/mir-fleet |
| ref-776 | Automated Warehouse | MiR Fleet Enterprise includes scalability, cybersecurity features for mobile robots | 기사 | low | https://www.automatedwarehouseonline.com/mir-fleet-enterprise-includes-scalability-cybersecurity-features-mobile-robots/ |
| ref-777 | Wang, Y. 외(arXiv 2606.04990) | From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents | 논문 | medium | https://arxiv.org/abs/2606.04990 |
| ref-695 | OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub) | LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md) | 오픈소스 문서 | medium | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md |
| ref-696 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Server Features: Tools (docs/specification/2025-06-18/server/tools.mdx) | 표준 | medium | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇 관제 챗봇의 채팅 지시 기록에 작업자 식별 정보가 담길 때 그 시스템이 개인정보의 안전성 확보조치 기준의 개인정보처리시스템에 해당해 접근권한 기록·접속기록 보관 기준을 적용받는지 공식 해석이 있는가? (관련: oq-099) | 26, 18 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-03 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 수행 자원 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-03 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 제약 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-03 | 단계 4. 오해석 방지와 확인 절차 |
| 피킹 | 예외·성과 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-03 | 단계 4. 오해석 방지와 확인 절차 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Model Context Protocol 명세 2025-06-18 (Basic: Authorization) | 표준 | Model Context Protocol (modelcontextprotocol GitHub) | 26, 27 | ref-764 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/basic/authorization.mdx |
| NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 | 프레임워크 | NIST | 26 | ref-769 | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf |

## 추가 조사 요청

- q4-03 명령 권한: IEC 62443-3-3 SR 2.1·2.8·2.11·2.12 를 발행 기관(IEC) 자료로 재확인해야 한다(현재 제3자 요약 기준).
- q4-03 감사 추적: 개인정보의 안전성 확보조치 기준 현행판의 접속기록 보관 기간과 조문 번호를 국가법령정보센터 원문으로 확인해야 한다.
- q4-03: 물류 창고 로봇 관제·챗봇의 사용자별 명령 권한 구성이나 감사 기록을 공개한 국내외 사례가 필요하다(현재 종합은 일반 LLM 보안 지침·에이전트 연구에 기댐).
- q4-04 제한 운영 기준은 미조사이며 단계 4 완료 조건에 필요하다.

## 이행한 수정 지시

- f10 강등 — 단계 4 페이지 q4-03 '감사 기록에 대한 요구'와 아이디어 5절에서 [추정]으로 쓰고 'SR 번호·내용은 제3자 요약 기준이며 발행 기관 원문은 미확인이다(2013-08 판)'를 본문에 밝혔다.
- f12 강등 — [추정]으로 쓰고 0%만 쓰지 않고 AgentDojo 39.9% → 1.0%, ASB 70.3% → 3.9% 요약도 병기하며 '저자 보고값, 판 차이 미확인'으로 적었고, ref-770 기관을 'Shi, T. 외(Progent 저자, 소속 미확인)'로 고쳤다.
- f15 강등 — [추정]으로 쓰고 '감사 기능을 두는 것으로 보인다(세부 미확인)'로 줄였으며, ref-773 제목을 'AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent', 기관을 'Luo, J. 외(Fudan University·Shanghai Innovation Institute)'로 고쳤다.
- f17 강등 — [추정]으로 쓰고 네 요소 정의를 '서베이 요약 기준이며 원문 미확인'으로 밝혔으며 ref-777 기관을 'Wang, Y. 외(arXiv 2606.04990)'로 고쳤다.
- f19 분할 — 권한 부여·변경·말소 내역 3년 보관 문장은 [사실]로 두고 원문 미열람·현행판 미확인을 표시했고, 접속기록 보관 기간 문장은 [추정]으로 두고 '미확인'을 병기했다(단계 4 페이지·아이디어 5절).
- f14 — ref-774 기관을 'Zhu, J., Tseng, K., Vernik, G., Huang, X., Patil, S. G., Fang, V., & Popa, R. A.(arXiv 2512.11147)'로 고쳤고 태그는 [추정]을 유지했다.
- f22 — 감사 추적 보관 기간 문장에서 6개월·3년 수치를 빼고 '적용 법규의 최소 기준(미확인 포함)'으로 두었으며, 항목 근거 가운데 IEC 62443-3-3·출처 서베이가 [추정]임을 적고 문장 전체를 [추정]으로 유지했다.
- f7·f8 — MCP 인가 절의 OAuth 2.1 준수는 권고(SHOULD), 토큰 대상 검증·토큰 전달 금지는 필수(MUST), 도구 절의 클라이언트 확인·감사 기록은 권고(SHOULD), 도구 주석 불신은 필수(MUST)임을 본문에 밝혔다.
- 용어 — 본문의 audit trail 영문 병기를 '감사 추적(Audit Trail)'으로 쓰고 ../../glossary/audit-trail.md 링크를 걸었으며, RBAC·ABAC·혼란된 대리인을 glossary_updates 에 신규 등록했다.
- f11 — [추정] 벤더 주장을 병기하고 기사(ref-776)는 벤더 발표를 옮긴 것이라 독립 확인이 아님을 본문에 밝혔다.
- 각주 — ref-765~ref-777 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-579·763·764·695·696·125·031 은 원문 열람 출처로 두었다.
- 각주 재사용 — ref-695·ref-696·ref-031 은 단계 4 페이지의 기존 각주를, 초안의 ref-125·ref-031·ref-696 은 기존 정의를 재사용했다. 단계 4 페이지에 없던 ref-125 는 초안과 같은 정의 줄을 그대로 옮겼고 새 id 는 만들지 않았다.
- 온톨로지 — 개념 '명령 권한 (Command Authorization)'을 초안 2절에 확정 상태로 추가하고, 주체·동작·자원 그룹은 f2, 환경 조건은 f9, 집행 위치는 f6 근거로 적었으며, 속성 구성·기본 거부는 f21 추정 '후보', f1 은 로봇 미들웨어 참고 근거로 적고, 판정 결과 기록 위치를 정하지 않았음과 '사용자 확인'·'검증 기록' 질문과의 경계를 표 아래 설명에 적었다(다이어그램에 노드 추가, 6절 질문 추가).
- 온톨로지 — 개념 '지시' 속성 '입력자'를 '입력자(인증된 사용자 식별)'로 정리하고 requester 비인증 메모(f4, [사실])를 더했으며, ROP 경계 결합은 f23 [추정] 메모로, '위임 범위'는 f16 근거 후보 속성으로 두고 상태 확정을 유지했다.
- 버전 — 프런트매터 ontology_version 과 track_updates.ontology_draft_version 을 '0.9' 로 맞추고, 상태 줄은 auto 영역이라 프런트매터로 채워지게 했으며, 버전 이력 내용은 log_entry 의 '온톨로지 변경'에 적었다(H1 은 2차 수정에서 '(v0.9)'로 맞춤).
- 단계 4 페이지 — 2절 q4-03 을 '답함'으로 바꾸고 3절에 '### q4-03 … {#q4-03}' 소제목을 두었으며, 6절 '명령 권한' 행을 '미충족'으로 두고 '다음 단계로 전환: 아니오(제한 운영 기준 q4-04 미조사, 열린 질문 q4-04~q4-18)'로 썼다.
- 백로그 — 새 질문 q4-17(단계 4, origin f21), q4-18(단계 4, origin f22), q5-17(단계 5, origin f6)을 backlog_updates 에 finding id origin 으로 등록했고 q4-09·q4-10 상태는 바꾸지 않았다.
- 세부영역 반영 — 26. 사이버보안·접근권한·개인정보, 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 페이지는 고치지 않고 area_reflection_proposals 와 log_entry 로만 남겼으며, 27 제안에서 f12·f15·f17 은 [추정]으로 옮겼다.
- 열린 질문 — open_questions_new 1건을 질문 문장만 question 으로, areas [26, 18] 로 옮기고 문장 끝에 '(관련: oq-099)'를 붙였다.
- 2차: 초안 H1 — docs/tracks/nl-task-chatbot/task-model-draft.md 를 전체 content 로 보내며 H1 을 '업무 분해·배정 설계 초안 (v0.9)'로 고쳐 프런트매터 ontology_version '0.9'·track_updates.ontology_draft_version '0.9' 와 맞췄고(auto 마커와 그 안의 내용은 그대로 둠), additional_research_requests 의 H1 동기화 확인 요청 항목을 지웠다.
- 2차: 단계 상태 줄 — 단계 4 페이지를 전체 content 로 보내며 H1 아래 줄을 '> 단계 상태: 진행 중 · 열린 질문: 15건 · 답한 질문: 3건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25'로 고쳤고, additional_research_requests 의 해당 항목을 지웠다.
- 2차: 시나리오 문구 — 단계 4 페이지 q4-03 설명용 시나리오 예외·성과 칸의 '권한 제약이 처리량에 주는 영향을 잰 자료는 찾지 못했다'를 '권한 제약이 배정 최적성에 주는 손실을 잰 자료는 찾지 못했다'로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
- 온톨로지 초안 버전: 0.9
- 트랙 로그 항목: 답한 질문: q4-03(채팅 사용자별 명령 권한과 지시·확인의 감사 추적, 신뢰도 low) / 새 질문: q4-17(f21), q4-18(f22), q5-17(f6) / 온톨로지 변경: v0.8 → v0.9: 개념 '명령 권한' 추가(f2·f6·f9, 속성 구성·기본 거부는 f21 추정 후보, f1 참고), 개념 '지시' 입력자를 인증된 사용자 식별로 정리(f4·f16, ROP 경계 결합은 f23 추정 메모, 위임 범위 후보) — 버전 이력 행: 0.9 / 2026-09-25 / 명령 권한 추가(f2·f6·f9), 지시 입력자 정리(f4·f16) / 2026-09-25-83; 거부 없음 / 완료 조건 평가: 미충족(부족: 실행 전 검증 단계·명령 권한 확인 절차가 검증 승인 상태로 초안 6절·아이디어 5절에 반영되지 않음, 제한 운영 기준 q4-04 미조사) / 세부영역 반영 제안: 26. 사이버보안·접근권한·개인정보, 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 3건 / 다음 실행 제안: q4-04(제한 운영 기준), q4-09·q4-10 중복 정리
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 15, 답함 3, 완료 조건 미충족(단계 전환 미승인, 트랙 개요의 현재 단계 표시는 단계 3 유지)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-03 | 답함 | docs/tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md#q4-03 | — | — | — |
| q4-17 | 열림 | — | 교대 인계·부재 대리처럼 채팅 사용자가 다른 사람의 권한을 대신 쓰거나, 비상 시 권한 밖 지시를 먼저 실행하고 사후 검토하는 예외(긴급 권한)를 둘 때 위임 범위·유효 시간·사후 감사 기록을 어떻게 정하는가? (q4-03 에서 파생) (관련: q4-13) | 4 | f21 |
| q4-18 | 열림 | — | 채팅 지시 감사 기록을 Open-RMF 작업 요청 id·VDA 5050 orderId 와 어떤 키로 연결하고, 개인정보 보관 기준과 EU AI Act 로그 보관 기준이 함께 걸릴 때 보관 기간·접근 권한·위변조 방지(해시 연쇄 등)를 어떻게 정하는가? (q4-03 에서 파생) | 4 | f22 |
| q5-17 | 열림 | — | 권한 밖 지시와 프롬프트 주입이 섞인 물류 지시 시험 세트로, LLM 단의 거절과 ROP 인가 계층의 결정적 거부가 각각 권한 밖 작업 요청을 얼마나 막는지와 정상 지시의 오거부율을 어떻게 재는가? (q4-03 에서 파생) (관련: q5-13) | 5 | f6 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 26 | 6. 대표 접근법과 기술 | 채팅 지시의 명령 권한: 로봇 관제 구현은 역할·동작·인가 그룹(Open-RMF 웹 API 서버, [사실] ref-763)이나 인클레이브·노드별 기본 거부 규칙(SROS 2, [사실] ref-579)으로 권한을 표현하고, OWASP LLM06 은 LLM 이 아닌 하위 시스템에서 사용자 권한 맥락으로 인가를 집행하라고 권고한다([사실] ref-695). 권한을 역할·동작·자원 그룹·환경 조건(ABAC, ref-769) 기본 거부 규칙으로 두고 지시마다 사용자 식별·해석·권한 판정·확인·작업 요청 id·결과를 타임스탬프와 잇는 감사 추적 구성은 이 위키의 종합([추정], f21·f22). 인증된 위임 틀([사실] ref-771), 개인정보 권한 변경 기록 3년 보관([사실] ref-767, 접속기록 기간 미확인), IEC 62443-3-3 FR 2([추정] ref-768)를 함께 싣는다. |
| 13 | 6. 대표 접근법과 기술 | 사용자 권한이 지시할 수 있는 플릿·구역을 제한하면 가장 가까운 로봇이 후보에서 빠질 수 있으므로, 권한은 Open-RMF fleet_name 처럼 배정 전 후보를 거르는 제약으로 넘기고 후보 가운데 선택 기준은 디스패처가 지키는 분담이 선택지로 보인다([추정], f25). fleet_name 이 수행 가능 플릿을 지정하고 requester 는 인증 필드가 없는 선택 문자열이라는 점은 [사실](f4, ref-125). 권한 제약의 최적성 손실을 잰 자료는 없다. 교차 규칙에 따라 27. AI·학습·적응과 모델 운영과 함께 연결한다. |
| 27 | 6. 대표 접근법과 기술 | LLM 에이전트 권한 통제 연구: Conseca 의 과제별 즉시 정책과 결정적 집행([사실] ref-772), 인증된 위임([사실] ref-771), Progent 의 도구·인자 규칙 정책([추정] ref-770, 수치는 요약마다 다름), AgentGuard 의 속성 기반 접근 통제([추정] ref-773, 세부 미확인), LLM 생성 정책의 보장 부족을 지적한 MiniScope([추정] ref-774), 도구 호출 출처 기록 서베이([추정] ref-777). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결. |
