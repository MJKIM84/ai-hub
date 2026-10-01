# 스토리텔러 산출 2026-09-30-11

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md | draft | seed → draft: 3~11절 첫 작성(통신 인증·암호화, 위협 모델·IEC 62443, LLM 탈옥·프롬프트 주입 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 적용 사례, 책임 경계, 연결 19개 영역, 열린 질문), 13절 각주 17건. 2차 수정 6건 반영(5·8절 요약 태그, 6절 도식 안내 문장 분리·일반화 문장 한정, 3절 EU 규정 범위, 연계 대상 해석 태그 분리) |
| create | docs/topics/2026/2026-09-30-area52-s6.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "6. 대표 접근법과 기술" 절(2,109자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area52-s8.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "8. 대표 연구와 자료" 절(1,206자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area52-s10.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,102자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area52-s3.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "3. 왜 중요한가" 절(1,079자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area52-s11.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "11. 열린 질문" 절(1,063자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area52-s4.md | draft | 자동 분리: 52. 통신 보호·위협 관리·감사 의 "4. 핵심 개념과 용어" 절(1,031자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 52. 통신 보호·위협 관리·감사 | seed → draft: 3~11절 첫 작성(통신 인증·암호화, 위협 모델, LLM 입력 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 사례), 각주 17건 | run 2026-09-30-11
- 홈 최근 업데이트: 2026-09-30 — 52. 통신 보호·위협 관리·감사: 3~11절 첫 작성(SROS 2·Open-RMF 통신 보호, ROS 2 위협 모델·IEC 62443, LLM 탈옥·프롬프트 주입 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 사례)
- 대분류 최근 업데이트: 2026-09-30 — 52. 통신 보호·위협 관리·감사: seed → draft, 3~11절 첫 작성과 병원·가정·제조 공장 적용 사례, 열린 질문 5건 추가
- 세부영역 최근 업데이트: 2026-09-30 — 52. 통신 보호·위협 관리·감사: 3~11절 첫 작성, 각주 17건, 새 열린 질문 5건(oq-144 는 열림 유지)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | STRIDE 위협 분류 | STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) | 위조·변조·부인·정보 노출·서비스 거부·권한 상승 여섯 범주로 시스템 위협을 분류하는 위협 모델링 분류로, ROS 2 위협 모델이 로봇 시스템에 적용했다. | 52 | ref-010 |
| new | 간접 프롬프트 주입 | Indirect Prompt Injection | 프롬프트 주입(Prompt Injection)의 하위 유형으로, 사용자가 직접 입력하지 않은 웹 페이지·파일·인식 결과 같은 외부 내용에 숨은 지시가 언어 모델의 행동을 바꾸는 공격이다. | 52, 13 | ref-1108, ref-1115 |
| new | 보안 수준 | Security Level (SL, IEC 62443) | IEC 62443 에서 구역·도관이 견뎌야 할 공격자 역량에 따라 SL1~SL4 로 매기는 보호 등급으로, 일곱 기본 요구별 벡터로 표현할 수 있다. | 52, 22 | ref-1105 |
| new | 변조 탐지 로그 | Tamper-evident Log | 블록체인 같은 수단으로 기록이 나중에 고쳐지면 드러나게 만든 로그로, 책임 추적용 감사 기록의 무결성을 높이는 데 쓴다. | 52, 37 | ref-1112 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-009 | Open Robotics (ROS 2 Design, Kyle Fazzari) | ROS 2 DDS-Security integration | 오픈소스 문서 | high | https://design.ros2.org/articles/ros2_dds_security.html |
| ref-010 | Open Robotics (ROS 2 Design, Moulard·Hortala·Perez 외) | ROS 2 Robotic Systems Threat Model | 오픈소스 문서 | high | https://design.ros2.org/articles/ros2_threat_model.html |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 표준 | medium | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv) | Jailbreaking LLM-Controlled Robots | 논문 | medium | https://arxiv.org/abs/2410.13691 |
| ref-700 | Ravichandran, Z., Robey, A. 외 (arXiv) | Safety Guardrails for LLM-Enabled Robots | 논문 | medium | https://arxiv.org/abs/2503.07885 |
| ref-1108 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 업계 보고서 | medium | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| ref-1109 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 정부·연구기관 | high | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 |
| ref-1110 | Mayoral-Vilches, V. (Alias Robotics, arXiv) | The Cybersecurity of a Humanoid Robot | 논문 | medium | https://arxiv.org/abs/2509.14096 |
| ref-1111 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 업계 보고서 | medium | https://www.ies.co.uk/reference-library/machinery-regulation-guide |
| ref-1112 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 논문 | medium | https://arxiv.org/abs/2403.09567 |
| ref-969 | 바이라인네트워크 (곽중희) | ‘로봇청소기’ 다수 제품 보안 취약…대응방안은? | 기사 | medium | https://byline.network/2025/10/31-283/ |
| ref-1114 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 | 기사 | medium | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 |
| ref-1115 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 논문 | medium | https://arxiv.org/abs/2608.00747 |
| ref-1116 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 논문 | medium | https://arxiv.org/abs/2408.03515 |
| ref-031 | VDA / VDMA (VDA5050 공식 저장소) | VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-405 | Open Robotics (Programming Multiple Robots with ROS 2) | Security | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-1119 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 논문 | medium | https://files01.core.ac.uk/download/pdf/84891817.pdf |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? | 52, 20, 21 | 열림 | — |
| new | — | LLM 에이전트 여러 개가 로봇을 나눠 맡을 때 한 에이전트에 주입된 지시가 다른 에이전트로 퍼지지 않게 에이전트 간 메시지에 신뢰 경계를 두는 방어의 효과를 잰 연구가 있는가? | 52, 13, 12 | 열림 | — |
| new | — | 명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가? | 52, 37 | 열림 | — |
| new | — | EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? | 52, 59, 58 | 열림 | — |
| new | — | KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가? | 52, 59 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 작업 대상 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 병원 | 수행 자원 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 병원 | 제약 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 병원 | 예외·성과 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 가정 | 작업 대상 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 가정 | 수행 자원 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 가정 | 예외·성과 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 제조 공장 | 작업 대상 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |
| 제조 공장 | 예외·성과 | docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시 | 52. 통신 보호·위협 관리·감사 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) | 프레임워크 | OWASP GenAI Security Project | 52, 13 | ref-1108 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) | 프레임워크 | European Union (IES 해설 경유) | 52, 59, 50 | ref-1111 | https://www.ies.co.uk/reference-library/machinery-regulation-guide |
| KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 | 프레임워크 | 과학기술정보통신부·한국인터넷진흥원(KISA) | 52, 59 | ref-1114 | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 |

## 추가 조사 요청

- 13. 대화형 기능의 신뢰·기반 페이지(docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 6·8·11절 반영: 1차 검증 지시대로 현재 본문이 입력에 없어 이번 실행에서 갱신하지 않았다. 다음 실행에서 그 페이지 본문을 입력에 넣고 RoboPAIR·다중 에이전트 주입(ref-857·ref-1115), RoboGuard·보안 프롬프트 방어·OWASP LLM01(ref-700·ref-1116·ref-1108)과의 중복을 확인해 반영할 것.
- 5절 적용 사례: 물류창고·상업 시설·실외 현장의 로봇 통신 보호·위협·감사 사례(예: 물류창고 AMR 플릿 관리 소프트웨어 취약점 권고)를 찾지 못했다. 현장 유형 균형을 위해 필요하다.
- 4·6·7절: IEC 62443-3-3 의 감사 관련 요구(감사 대상 사건, 부인 방지, 감사 정보 보호 등)를 원문 또는 공식 자료로 확인해야 감사 기록 요구를 표준 근거로 쓸 수 있다.
- 5·8절: Quarta 외(ref-1119) 원문을 열어 공격 유형과 원격 장악 여부를 확인하면 [추정]을 [사실]로 되돌릴 근거가 된다.
- 6·7절: EU 기계류 규정 (EU) 2023/1230 원문(EUR-Lex)을 열어 변조 보호·개입 증거 기록·추적 로그 요구의 조항 번호와 문구를 확인할 것(현재 업계 해설 기준).
- 7·11절: KISA 로봇 보안모델 고도화판·사이버보안 요구사항 해설서 원문의 요구 항목(통신 암호화·감사 기록·원격 업데이트)과 대상 범위를 확인할 것.
- 퍼블리셔 확인 요청: 이번 브리프의 ref-1105~ref-1119 가 실행 2026-09-30-09 브리프의 다른 출처 id 와 겹칠 수 있고, ref-031(VDA 5050 3.0.0)은 실행 2026-09-30-10 의 ref-1079 와 URL 이 같다. id 병합·재부여 시 이 페이지의 각주 id 도 함께 바꿔야 한다.
- 분리 코드 담당 확인 요청: 이번 재실행은 세부영역 페이지를 3~11절 전체 본문으로 다시 냈으므로 분량 자동 분리가 다시 실행돼야 한다(이전 초안의 분리 주제 페이지 6건은 이 본문에서 새로 만들어야 2차 수정이 반영된다). 분리 주제 페이지의 '9. 검증 노트'가 2차 통과 전에 '1차·2차 검증을 거쳤다'로 적히는 문제는 2차 검증이 지적했다.

## 이행한 수정 지시

- f10 강등 — 5절 제조 공장 사례의 작업 대상·예외·성과 칸과 8절 Quarta 외 항목을 [추정]으로 쓰고, 검색 결과 요약으로 확인된 범위(소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음)만 남겼으며 '원격 완전 장악'·'펌웨어 백도어·인증 우회'는 뺐다.
- ref-1119 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 ref-1119 항목에 source_unopened: true 를 넣고 요약을 '원문 미열람.'으로 시작했다.
- f12 — '통신 암호화 부족'을 빼고 5절 가정 사례의 작업 대상·수행 자원·예외·성과 문장을 [추정]으로 강등했으며, 점검 주체·기간·6종·40개 항목과 나르왈·드리미·에코백스 제품의 사진 열람·카메라 강제 활성화, 미흡한 사용자 인증, 개인정보 조회만 남겼다.
- f6·ref-031 — 13절 각주와 reference_updates 의 제목을 'VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0)'으로 고쳤고, 본문(3·6·7절)에서 '플릿 관제–이동 로봇'으로 쓰며, 6절에서 원문 문장 그대로 '프로토콜 보안은 브로커 구성에서 고려해야 하지만 이 지침은 다루지 않는다'를 [사실]로, '운영자와 통합 사업자가 정해야 한다'는 별도 문장 [추정]으로 떼어 썼다.
- f4 — 6절에서 엄격 모드를 '보안 파일을 찾지 못한 참여자를 실행하지 않는 모드', 허용 모드를 '보안 파일이 없으면 보안 기능 없이 실행하는 기본 모드'로 고쳐 썼다.
- f21 — 3절 마지막 단락의 종합 문장에서 f10(제어기) 근거를 빼고 전면 제어 사례는 CISA 권고(ref-1109)에만 기대게 했으며, '높은 확률로 탈옥'을 '연구 환경에서 높은 공격 성공률이 보고됐다'로 바꿨다.
- f22 — 3절에서 '플릿 서버 취약점이 로봇 기능 전면 제어로 이어질 수 있음'으로 줄였고, KISA 해설서는 '제품 개발·수출 때 참고할 자료로 배포'로만 서술해 '제품 요건' 표현을 쓰지 않았다(EU 규정은 '요구한다'로만 썼다).
- 3·5·6·9절 — f9 의 방화벽·VPN·망 격리는 5절 제약 칸과 6절에서 '시설 IT/OT 쪽 연계 대상'으로 표시했고, f10·f11 의 제어기·펌웨어·제조사 원격 측정은 사례·위협 근거로만 쓰고 9절 표의 '연계 대상:' 칸에 짧게 두었다.
- f19 — 3·6·7절에서 근거가 업계 해설(IES, 2026-08-27 갱신)임을 밝히고, 6절에 규정 원문을 열지 못해 조항 번호는 적지 않는다고 적었다.
- 용어 후보 'STRIDE 위협 분류' — glossary_updates 정의에서 '빠짐없이 떠올리도록 돕는'을 빼고 '여섯 범주로 시스템 위협을 분류하는'으로 썼다.
- 용어 후보 '보안 수준' — glossary_updates 정의에서 '목표·역량·달성 수준을 구분하고'를 뺐다.
- 용어 후보 '변조 탐지 로그' — glossary_updates 정의에서 '앞 기록의 해시를 잇거나 외부에 고정해'를 빼고 '블록체인 같은 수단으로 기록이 고쳐지면 드러나게 만든 로그'로 줄였으며, 설명에 기존 용어 '감사 추적(Audit Trail)'과의 관계와 링크를 적었다.
- 용어 후보 '간접 프롬프트 주입' — glossary_updates 정의를 기존 용어 '프롬프트 주입(Prompt Injection)'의 하위 유형으로 표기하고 f18(OWASP)의 직접·간접 구분을 따랐으며, 설명에 상위 용어 링크를 적었다(4절 본문에서도 프롬프트 주입 항목 안에서 간접 주입을 설명했다).
- 두 번째 페이지 제안(13. 대화형 기능의 신뢰·기반) — 현재 본문이 입력에 없어 이번 실행에서 갱신하지 않았고, additional_research_requests 에 다음 실행 후보로 남겼다.
- 11절 — oq-144 를 '열림'으로 두고 f15·f17 을 시뮬레이션·실험실 수준의 부분 근거로만 적었으며, open_question_updates 에 해결 갱신을 넣지 않았다.
- 2차: 5절 첫 문장 — 태그를 [사실]에서 [추정]으로 바꾸고 각주를 [^ref-1109][^ref-969][^ref-1119]로 늘렸다(outline 5절 요약도 같게 고쳤다).
- 2차: 8절 첫 문장 — 태그를 [의견]으로 바꾸고 각주를 뗐다(분리 시 주제 페이지의 세 줄 요약과 본문 첫 문장에도 같은 문장이 옮겨진다. outline 8절 요약도 같게 고쳤다).
- 2차: 6절 — '아래 도식은 이번 자료를 종합한 다층 방어의 추정 구조다.'를 첫 단락에서 떼어 mermaid 블록 바로 앞의 별도 단락으로 옮겼다.
- 2차: 6절 '위협 모델과 취약점 관리' — 태그 없는 일반화 문장 '공개된 취약점에는 갱신과 망 격리로 대응한다.'를 지우고 'CISA는 TUG 서버 취약점의 완화책으로 버전 갱신, 방화벽 뒤 격리, 원격 접속 시 VPN을 권고했다. [사실][^ref-1109]'로 이 사례 하나에 한정해 썼다.
- 2차: 3절 셋째 단락 — EU 기계류 규정 문장을 '규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호와, 기계가 안전 관련 소프트웨어를 식별하고 개입 증거를 기록하는 것을 요구한다'로 고쳤다(standards_updates 요약도 같게 맞췄다).
- 2차: 5절 병원 표 '제약' 칸의 괄호를 빼고 '… VPN이다. [사실][^ref-1109] 이 가운데 망 조치는 시설 IT/OT 쪽 연계 대상이다. [추정][^ref-1109]'로 태그를 나눴고, 8절 Mayoral-Vilches 항목 끝을 '… 외부 서버로 간다고 보고했다. [사실][^ref-1110] 이는 로봇 제조사 쪽 연계 대상의 위협 근거로 보인다. [추정][^ref-1110]'로 나눴다.
- 분량 초과 자동 분리: 52. 통신 보호·위협 관리·감사 본문 10,696자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,895자
