# 스토리텔러 산출 2026-09-29-06

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md | draft | 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-869 신규, ref-351·ref-840·ref-165·ref-753 재사용), 상업 시설 사례 1건, 열린 질문 4건 추가, 1차 조건부 승인 수정 7건 이행 |
| create | docs/topics/2026/2026-09-29-area13-s6.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "6. 대표 접근법과 기술" 절(3,607자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s8.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "8. 대표 연구와 자료" 절(1,988자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s11.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "11. 열린 질문" 절(1,562자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s4.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "4. 핵심 개념과 용어" 절(1,495자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s10.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,267자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s7.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,256자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area13-s3.md | draft | 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "3. 왜 중요한가" 절(1,085자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 13. 대화형 기능의 신뢰·기반 | 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-869 신규, 4건 재사용), 상업 시설 사례 1건, 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 7건 이행 | run 2026-09-29-06
- 홈 최근 업데이트: 2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성(seed → draft). 프롬프트 주입·탈옥 위협, 불확실도 보정 되묻기, 호스트 쪽 승인 관문, 모델 대체 감사, 대화 기록 규제를 정리하고 상업 시설 사례 1건·열린 질문 4건·용어 4건을 더했다
- 대분류 최근 업데이트: 2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성(seed → draft), 출처 19건, 상업 시설(네덜란드 슈퍼마켓) 사례 1건, 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-06)
- 세부영역 최근 업데이트: 2026-09-29 — 13. 대화형 기능의 신뢰·기반: 3~11절 신규 작성. 위협(OWASP·RoboPAIR·Huang 외), 되묻기·자동 검증(KnowNo·LBAP·VerifyLLM), 승인 관문·권한(MCP·Michael·Roesner), 모델 대체 감사(IRIS), 기록 규제(EU AI Act 제12조·국내 안내서), 평가(Embodied Agent Interface·τ-bench), 화면 연동·음성 사례를 정리 (실행 2026-09-29-06)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 프롬프트 주입 | Prompt Injection | 사용자 입력이나 모델이 읽는 문서·도구 설명에 숨긴 지시로 언어 모델의 행동을 의도치 않게 바꾸는 공격으로, 도구를 부르는 에이전트에서는 무단 동작으로 이어질 수 있다. | 13, 52, 12 | ref-855, ref-856 |
| new | 탈옥 | Jailbreak | 언어 모델의 안전 제한을 우회하도록 유도하는 입력 기법으로, 로봇을 제어하는 언어 모델에서는 유해한 물리 동작을 끌어내는 데 쓰일 수 있다. | 13, 48, 52, 44 | ref-857, ref-859 |
| new | 승인 피로 | Approval Fatigue (Consent Fatigue) | 에이전트의 동작마다 사람에게 승인을 묻는 방식이 반복되어 사용자가 검토 없이 허용하거나 자동 승인으로 바꾸게 되는 현상으로, 실시간 승인 관문의 실효성을 떨어뜨린다. | 13, 12, 51 | ref-868, ref-165 |
| new | 모델 대체·라우팅 희석 | Model Substitution / Routing Dilution | 언어 모델 게이트웨이가 요청한 모델 대신 다른 모델로 응답하거나(대체) 요청의 일부만 약속한 모델로 보내는(희석) 현상으로, 재현성과 모델 교체 정책의 통제를 어렵게 한다. | 13, 47, 57 | ref-865 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-855 | OWASP GenAI Security Project | OWASP Top 10 for LLM Applications 2025 | 업계 보고서 | medium | https://genai.owasp.org/llm-top-10/ |
| ref-856 | Model Context Protocol (Anthropic 주도 오픈소스 프로젝트) | Specification — Model Context Protocol (2025-06-18) | 오픈소스 문서 | high | https://modelcontextprotocol.io/specification/2025-06-18 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 논문 | medium | https://arxiv.org/abs/2410.13691 |
| ref-858 | Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks) | Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making | 논문 | medium | https://arxiv.org/abs/2410.07166 |
| ref-859 | Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R. | Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges | 논문 | medium | https://arxiv.org/abs/2601.02377 |
| ref-860 | 과학기술정보통신부·한국정보통신기술협회(TTA) | 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기) | 정부·연구기관 | high | https://tta-trustworthy-ai.gitbook.io/general |
| ref-861 | van Dam, H. G. W. | A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants | 논문 | medium | https://arxiv.org/abs/2510.06223 |
| ref-862 | 개인정보보호위원회 | 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) | 정부·연구기관 | medium | https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 |
| ref-864 | Mullen, J. F., Jr., & Manocha, D. | Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2403.13198 |
| ref-865 | Zhang, Y., Zhang, Z.-H., & Qin, H. | Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways | 논문 | medium | https://arxiv.org/abs/2607.20860 |
| ref-866 | Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E. | Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems | 논문 | medium | https://arxiv.org/abs/2607.11792 |
| ref-738 | Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (Sierra) | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 논문 | medium | https://arxiv.org/abs/2406.12045 |
| ref-868 | Michael, A. E., & Roesner, F. | How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement | 논문 | medium | https://arxiv.org/abs/2607.13718 |
| ref-869 | Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI | Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/ |
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 논문 | medium | https://arxiv.org/abs/2307.01928 |
| ref-840 | Laban, P., Hayashi, H., Zhou, Y., & Neville, J. | LLMs Get Lost In Multi-Turn Conversation | 논문 | medium | https://arxiv.org/abs/2505.06120 |
| ref-165 | Li, P., An, Z., Abrar, S., & Zhou, L. | Large Language Models for Multi-Robot Systems: A Survey | 논문 | medium | https://arxiv.org/abs/2502.03814 |
| ref-753 | Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 논문 | medium | https://arxiv.org/abs/2507.05118 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? | 13, 59, 53 | 열림 | — |
| new | — | 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? | 13, 52, 48 | 열림 | — |
| new | — | 언어 모델 게이트웨이의 모델 대체·라우팅 희석을 ROP 운영에서 탐지·기록하고 계약으로 막는 실무 절차나 사례가 있는가? | 13, 57, 58 | 열림 | — |
| new | — | 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? | 13, 60, 61 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 상업 시설 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |
| 상업 시설 | 작업 대상 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |
| 상업 시설 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |
| 상업 시설 | 제약 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |
| 상업 시설 | 완료·인계 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |
| 상업 시설 | 예외·성과 | docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md#5-적용-사례-현장-유형-명시 | 13. 대화형 기능의 신뢰·기반 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) | 프레임워크 | European Union (유럽위원회 AI Act Service Desk 게재) | 13, 52, 53, 59 | ref-863 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 |
| 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) | 프레임워크 | 개인정보보호위원회 | 13, 53 | ref-862 | https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20836 |
| 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 | 프레임워크 | 과학기술정보통신부·한국정보통신기술협회(TTA) | 13, 47, 54 | ref-860 | https://tta-trustworthy-ai.gitbook.io/general |
| Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) | 평가 프로그램 | Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) | 13, 44, 54 | ref-858 | https://arxiv.org/abs/2410.07166 |
| langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) | 오픈소스 | van Dam, H. G. W. | 13, 8, 9 | ref-861 | https://arxiv.org/abs/2510.06223 |

## 추가 조사 요청

- 5절에 물류창고·병원·제조 공장·가정·실외의 대화 기능 실제 사례와 국내 현장 자료가 필요하다. 이번 브리프에는 상업 시설(네덜란드 슈퍼마켓 연구) 하나뿐이어서 다른 현장 유형 사례를 쓰지 못했다.
- 6·8절(대화형 기능 평가)에 로봇 지도 작성·로봇 구성 대화에 특화된 벤치마크나 지표(oq-125·oq-127)가 필요하다. 이번 브리프는 일반 체화 벤치마크(Embodied Agent Interface)와 도구 에이전트 벤치마크(τ-bench)만 확인했다.
- 6절(대화 권한과 승인 관문)에 로봇 대수·계획 크기에 따른 승인 단위를 정한 연구나 지침(oq-139)과, MCP 도구 호출 경로에서 승인 관문을 둔 공개 구현·운영 사례(oq-141. 브리프가 언급한 OSRA Interop SIG MCP 세션 포함)가 필요하다.
- 6절(대화 기록의 보존·보호)에 대화·도구 호출·제공 모델 기록 형식의 근거(브리프가 출처 상한으로 넣지 못한 OpenTelemetry GenAI 시맨틱 규약)와 개인정보보호위원회 안내서 PDF 본문(4단계 구성, AI 에이전트 관련 내용)이 필요하다.
- 6절(음성·다국어)에 산업 현장 음성 제어 사례(브리프가 403·인증 리다이렉트로 열지 못한 ScienceDirect·SSRN 게재 논문과 SMaRTAban)와 소음·한국어 조건 인식률 수치가 필요하다.
- 참고문헌 id 확인 요청: 브리프와 1차 검증은 ref-840 을 Laban 외(2025) 'LLMs Get Lost In Multi-Turn Conversation'(arXiv 2505.06120)으로 쓰지만, 입력의 C. 채팅 기반 구성·운영 대분류 페이지 자료 목록에는 ref-840 이 Tack·Laban·Neville 'LLMs Get Lost in Evolving User Intent'(2026-07-22)로 실려 있다. 퍼블리셔가 URL 기준으로 합칠 때 두 논문이 다른 id 를 갖는지 확인해야 한다.
- 참고문헌 번호 충돌 확인 요청: 1차 검증 지적대로 ref-855~ref-862 가 이전 실행 2026-09-29-05 의 출처와 번호가 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 새 번호를 배정해야 하며, 본문 각주도 그에 맞춰 바뀌어야 한다.

## 이행한 수정 지시

- ref-866 제목 정정 — 13절 각주 정의와 reference_updates 의 제목을 'Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems'로 고쳤고, 8절 목록에서도 이 제목으로 적었다.
- f22 표현 정정 — 6절 '언어 모델 연결·교체와 대체 감사'의 IRIS 문장을 '같은 모델을 내는 제공자 쌍 15개 중 14개를 실제 양자화·커널 차이로 표시했다'로 썼고 reference_updates 요약도 같은 표현으로 맞췄다.
- f15 강제 방식 다섯째 항목 정정 — 6절 '대화 권한과 실행 전 승인 관문'에서 강제 방식을 '다섯 가지 강제 방식(에이전트 자율 준수·언어 모델 가드레일·결정적 위반 탐지·실시간 사용자 승인·AI 생성 강제 코드)'로 적어 '형식 검증 강제'를 쓰지 않았다.
- f3 표현 정정 — 3절과 8절의 RoboPAIR 문장을 '세 설정에서 종종(often) 100%에 이르는 공격 성공률을 보고했고'로 썼고, 4절 탈옥 용어와 용어집 설명에서도 무조건 100%로 읽히지 않게 했다.
- f16 기준일 정정 — 3절과 8절의 Li 외 서베이 문장에 'v5, 2026-05-03 개정 기준'을 적고, 13절 각주 ref-165 정의의 제목 뒤에 '(v5, 2026-05-03 개정)'을 병기했으며 reference_updates 요약에도 같은 판을 적었다.
- ref-863 발행일 정정 — 13절 각주와 reference_updates 의 발행일을 '미확인' 대신 2024-06-13 으로 적었고, 6절 EU AI Act 제12조 문장에 '규정 공식본 2024-06-13 기준'을 남겼다.
- 원문 미열람 표기 유지 — ref-351·ref-840·ref-165·ref-753 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true, summary 를 '원문 미열람. '으로 시작하게 했다. 나머지 15건은 false 로 두었다.
- 분량 초과 자동 분리: 13. 대화형 기능의 신뢰·기반 본문 14,247자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,311자
